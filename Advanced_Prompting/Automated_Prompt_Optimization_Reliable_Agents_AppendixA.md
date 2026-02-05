# Appendix A: Automated Prompt Optimization Script

## Overview

This script implements the automated I/T/E optimization workflow described in Section 5.5. It
takes a failing prompt, runs diagnostic analysis, generates variations, tests them systematically,
and returns the optimized prompt.

### Automated Prompt Optimization Flow

1. **Human provides failing prompt + test cases with failures**
2. **Meta-Agent diagnoses which variable (I/T/E) is broken**
3. **Meta-Agent generates 3 variations locking 2 variables, varying 1**
4. **Test Runner executes all variations against the test set**
5. **Judge LLM scores results (accuracy, format compliance, etc.)**
6. **Meta-Agent picks winner, reports final optimized prompt to human**

### What this script does

1. Accepts a failing prompt + test cases from the user
2. Uses a reasoning model (Claude Opus) to diagnose which variable (I/T/E) is broken
3. Generates 3 variations (changing only the diagnosed variable)
4. Runs all variations against your test set
5. Uses LLM-as-Judge to score results
6. Returns the winning variation with performance metrics

### Requirements

- Python 3.8+
- Anthropic API key
- Libraries: `anthropic`, `json`, `typing`

**Installation:**

```bash
pip install anthropic
```

**Set your API key:**

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

---

## The Complete Script

```python
#!/usr/bin/env python3
"""
Automated I/T/E Prompt Optimizer
Implements the optimization framework from Section 5.5

Usage:
    python optimize_prompt.py --prompt "your_prompt.txt" --tests "test_cases.json"
"""

import argparse
import json
import os
import time
import random
from typing import List, Dict, Tuple, Optional
from anthropic import Anthropic, APIError, APITimeoutError, RateLimitError

# Initialize Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Configuration - Current as of January 2026
META_MODEL = "claude-opus-4-5-20251101"      # Opus 4.5 - Most capable for diagnosis
TEST_MODEL = "claude-sonnet-4-5-20250929"    # Sonnet 4.5 - Balanced for testing
JUDGE_MODEL = "claude-sonnet-4-5-20250929"   # Sonnet 4.5 - Fast, reliable judging


def call_with_retry(api_call_func, max_retries=3, context="API call"):
    """Call API with exponential backoff on transient failures.

    Args:
        api_call_func: Lambda/function that makes the API call
        max_retries: Maximum retry attempts
        context: Description for logging

    Returns:
        API response

    Raises:
        Last encountered error if all retries fail
    """
    for attempt in range(max_retries):
        try:
            return api_call_func()
        except RateLimitError as e:
            if attempt == max_retries - 1:
                raise
            # Rate limits need longer backoff
            wait = min(60, (2 ** attempt) * 10)  # 10s, 20s, 40s (max 60s)
            jitter = random.uniform(0, 0.1 * wait)
            total_wait = wait + jitter
            print(f"  ⚠ Rate limit hit during {context}")
            print(f"    Waiting {total_wait:.1f}s before retry {attempt + 2}/{max_retries}...")
            time.sleep(total_wait)
        except (APITimeoutError, APIError) as e:
            if attempt == max_retries - 1:
                raise
            # Network errors need shorter backoff
            wait = 2 ** attempt  # 1s, 2s, 4s
            jitter = random.uniform(0, 0.1 * wait)
            total_wait = wait + jitter
            print(f"  ⚠ {type(e).__name__} during {context}: {e}")
            print(f"    Retrying in {total_wait:.1f}s... ({attempt + 2}/{max_retries})")
            time.sleep(total_wait)
        except Exception as e:
            # Unknown errors - don't retry
            print(f"  ✖ Unexpected error during {context}: {e}")
            raise


class TestCase:
    """Represents a single test case with input, expected output, and actual output."""

    def __init__(self, input_text: str, expected_output: str, actual_output: str = None):
        self.input = input_text
        self.expected = expected_output
        self.actual = actual_output

    def to_dict(self) -> Dict:
        return {
            "input": self.input,
            "expected": self.expected,
            "actual": self.actual
        }


class PromptOptimizer:
    """Main optimizer class that orchestrates the I/T/E optimization workflow."""

    def __init__(self, failing_prompt: str, test_cases: List[TestCase],
                 success_criteria: str, num_variations: int = 3,
                 test_combinations: bool = False, skip_baseline: bool = False):
        self.original_prompt = failing_prompt
        self.test_cases = test_cases
        self.success_criteria = success_criteria
        self.num_variations = num_variations
        self.test_combinations = test_combinations
        self.skip_baseline = skip_baseline
        self.diagnosis_result = None
        self.variations = []
        self.results = []
        self.baseline_score = None

    def validate_test_cases(self) -> Tuple[bool, List[str]]:
        """Validate test case quality and coverage.

        Returns:
            (is_valid, list_of_warnings)
        """
        warnings = []

        # Rule 1: Minimum quantity
        if len(self.test_cases) < 5:
            warnings.append(
                f"Only {len(self.test_cases)} test cases. Recommend 10+ for reliable optimization."
            )

        # Rule 2: Input diversity (simple heuristic)
        inputs = [tc.input for tc in self.test_cases]
        unique_words = set()
        for inp in inputs:
            unique_words.update(inp.lower().split())
        if len(unique_words) < len(inputs) * 3:  # Expect ~3 unique words per test
            warnings.append(
                "Test inputs may lack diversity. Consider adding more varied scenarios."
            )

        # Rule 3: Expected output specificity
        for i, tc in enumerate(self.test_cases):
            if len(tc.expected.split()) < 5:
                warnings.append(
                    f"Test {i+1}: Expected output is very short ('{tc.expected}'). "
                    "Vague expectations make judging difficult."
                )

        # Rule 4: Check for contradictions (LLM-based, optional)
        if len(self.test_cases) >= 3:
            contradiction_check = self._check_contradictions()
            if contradiction_check:
                warnings.append(f"Potential contradiction: {contradiction_check}")

        # Rule 5: Edge case coverage (heuristic)
        edge_case_keywords = ['empty', 'null', 'invalid', 'missing', 'error',
                              'edge', 'boundary', 'max', 'min']
        has_edge_cases = any(
            any(keyword in tc.input.lower() for keyword in edge_case_keywords)
            for tc in self.test_cases
        )
        if not has_edge_cases:
            warnings.append(
                "No obvious edge cases detected. Consider adding tests for "
                "empty inputs, errors, or boundary conditions."
            )

        is_valid = len(warnings) == 0 or len(self.test_cases) >= 5
        return is_valid, warnings

    def _check_contradictions(self) -> Optional[str]:
        """Use LLM to detect contradictory test cases (optional, costs 1 API call)."""
        test_summary = "\n".join([
            f"{i+1}. Input: {tc.input} → Expected: {tc.expected}"
            for i, tc in enumerate(self.test_cases[:10])  # Check first 10
        ])

        prompt = f"""Review these test cases for contradictions:

{test_summary}

Do any test cases contradict each other? For example:
- Same input expecting different outputs
- Requirements that are mutually exclusive
- Inconsistent expectations

If you find contradictions, return JSON:
{{"has_contradiction": true, "description": "Test 2 expects X but Test 5 expects Y for similar input"}}

If no contradictions, return:
{{"has_contradiction": false}}

Output ONLY valid JSON."""

        try:
            response = call_with_retry(
                lambda: client.messages.create(
                    model=JUDGE_MODEL,
                    max_tokens=500,
                    messages=[{"role": "user", "content": prompt}]
                ),
                context="contradiction check"
            )
            result = json.loads(response.content[0].text)
            if result.get("has_contradiction"):
                return result["description"]
        except:
            pass  # Contradiction check is optional, fail silently
        return None

    def run_optimization(self) -> Dict:
        """Main optimization pipeline."""
        print("=" * 80)
        print("AUTOMATED I/T/E PROMPT OPTIMIZATION")
        print("=" * 80)

        # Validation: Check test case quality
        print("\n[Validation] Checking test case quality...")
        is_valid, warnings = self.validate_test_cases()
        if warnings:
            print("  ⚠ Test Case Warnings:")
            for w in warnings:
                print(f"    - {w}")
            if not is_valid:
                response = input("\nContinue anyway? (y/n): ")
                if response.lower() != 'y':
                    print("Aborted. Please improve test cases and re-run.")
                    return None
        else:
            print("✓ Test cases look good")

        # Step 0: Test baseline (unless skipped)
        if not self.skip_baseline:
            print("\n[Step 0/6] Testing original prompt for baseline...")
            baseline_result = self._test_single_variation({
                "variation_id": 0,
                "modified_prompt": self.original_prompt,
                "change_description": "Original (baseline)",
                "test_hypothesis": "Baseline performance"
            })
            baseline_score = self._score_single_result(baseline_result)
            print(f"✓ Baseline score: {baseline_score['overall_score']:.1f}/100")
            self.baseline_score = baseline_score['overall_score']

            # Early exit if baseline is already good
            if baseline_score['overall_score'] >= 90:
                print("\n 🎉 Original prompt already performs well (≥90%). No optimization needed.")
                return self._format_final_report({
                    "variation_id": 0,
                    "optimized_prompt": self.original_prompt,
                    "overall_score": baseline_score['overall_score'],
                    "improvement": 0,
                    "change_description": "No changes needed",
                    "pass_rate": baseline_score.get('pass_rate', 'N/A'),
                    "strengths": baseline_score.get('strengths', []),
                    "weaknesses": baseline_score.get('weaknesses', [])
                })
        else:
            self.baseline_score = 50  # Fallback assumption if baseline skipped

        # Step 1: Diagnose the failure
        print("\n[Step 1/6] Diagnosing failure type...")
        self.diagnosis_result = self._diagnose_failure()
        print(f"✓ Diagnosis complete: {self.diagnosis_result['failure_type']}")
        print(f"  Broken Variable: {self.diagnosis_result['broken_variable']}")
        print(f"  Confidence: {self.diagnosis_result['confidence']}")

        # Step 2: Generate variations
        print(f"\n[Step 2/6] Generating {self.num_variations} prompt variations...")
        self.variations = self._generate_variations()
        print(f"✓ Generated {len(self.variations)} variations")

        # Step 3: Test all variations
        print("\n[Step 3/6] Testing variations against test set...")
        self.results = self._test_variations()
        print(f"✓ Tested all variations ({len(self.test_cases)} test cases each)")

        # Step 4: Score with LLM-as-Judge
        print("\n[Step 4/6] Scoring results with LLM-as-Judge...")
        scored_results = self._score_results()
        print("✓ Scoring complete")

        # Step 5: Select winner
        print("\n[Step 5/6] Selecting best variation...")
        winner = self._select_winner(scored_results)
        print(f"✓ Winner: Variation {winner['variation_id']}")
        print(f"  Score: {winner['score']:.2f}/100")
        print(f"  Improvement: +{winner['improvement']:.1f}%")

        # Step 6: Optional combination testing
        if self.test_combinations:
            print("\n[Step 6/6] Testing variable combinations (Phase 2)...")
            combo_winner = self._test_combinations(winner)
            if combo_winner and combo_winner['overall_score'] > winner['overall_score']:
                print(f"✓ Combination improved score to {combo_winner['overall_score']:.2f}/100")
                winner = combo_winner
            else:
                print("✓ No combination outperformed the single-variable optimization")
        else:
            print("\n[Step 6/6] Skipping combination testing (use --test-combinations to enable)")

        return self._format_final_report(winner)

    def _test_single_variation(self, variation: Dict) -> Dict:
        """Test a single variation against all test cases."""
        variation_results = {
            "variation_id": variation["variation_id"],
            "test_outputs": []
        }

        for test_case in self.test_cases:
            # Run the test with this variation's prompt
            test_prompt = variation["modified_prompt"]
            response = call_with_retry(
                lambda: client.messages.create(
                    model=TEST_MODEL,
                    max_tokens=2000,
                    messages=[{
                        "role": "user",
                        "content": f"{test_prompt}\n\nInput: {test_case.input}"
                    }]
                ),
                context=f"testing variation {variation['variation_id']}"
            )
            output = response.content[0].text
            variation_results["test_outputs"].append({
                "input": test_case.input,
                "expected": test_case.expected,
                "actual": output
            })

        return variation_results

    def _score_single_result(self, result: Dict) -> Dict:
        """Score a single variation's results."""
        judge_prompt = f"""You are an LLM Judge evaluating prompt optimization results.

Success Criteria:
{self.success_criteria}

Evaluate these test results and provide a score:
{json.dumps(result['test_outputs'], indent=2)}

Provide your evaluation as JSON:
{{
    "overall_score": 0-100,
    "pass_rate": "X/Y tests passed",
    "strengths": ["what this variation does well"],
    "weaknesses": ["remaining issues"],
    "meets_criteria": true/false
}}

Output ONLY valid JSON."""

        response = call_with_retry(
            lambda: client.messages.create(
                model=JUDGE_MODEL,
                max_tokens=1500,
                messages=[{"role": "user", "content": judge_prompt}]
            ),
            context="judging results"
        )
        score = json.loads(response.content[0].text)
        score["variation_id"] = result["variation_id"]
        return score

    def _diagnose_failure(self) -> Dict:
        """Use meta-model to diagnose which variable (I/T/E) is broken."""

        # Format test case failures for diagnosis
        failures_text = "\n\n".join([
            f"Test Case {i+1}:\nInput: {tc.input}\nExpected: {tc.expected}\nActual: {tc.actual}"
            for i, tc in enumerate(self.test_cases)
        ])

        diagnostic_prompt = f"""You are an Expert Prompt Optimization Agent specializing in the I/T/E framework.

# Background: The I/T/E Framework
Every agent prompt decomposes into three independent variables:
- I (Instructions): The task directive and behavioral rules
- T (Thoughts/State): The reasoning structure or state file format
- E (Exemplars): Few-shot examples demonstrating correct behavior

# Current Failing Prompt
{self.original_prompt}

# Observed Failures
{failures_text}

# Success Criteria
{self.success_criteria}

# Your Task
Analyze the failures and provide a diagnosis in JSON format:
{{
    "failure_type": "Structure Failure" | "Logic Failure" | "Syntax Failure",
    "broken_variable": "I" | "T" | "E",
    "confidence": "High" | "Medium" | "Low",
    "reasoning": "Explain what in the failure examples led to this diagnosis",
    "diagnostic_evidence": ["specific symptom 1", "specific symptom 2", ...]
}}

Output ONLY valid JSON, no other text."""

        response = call_with_retry(
            lambda: client.messages.create(
                model=META_MODEL,
                max_tokens=2000,
                messages=[{"role": "user", "content": diagnostic_prompt}]
            ),
            context="diagnosis"
        )

        # Parse JSON response
        diagnosis = json.loads(response.content[0].text)
        return diagnosis

    def _generate_variations(self) -> List[Dict]:
        """Generate variations based on the diagnosed broken variable."""

        variation_prompt = f"""Based on this diagnosis:
Failure Type: {self.diagnosis_result['failure_type']}
Broken Variable: {self.diagnosis_result['broken_variable']}

Original Prompt:
{self.original_prompt}

Generate {self.num_variations} variations that ONLY modify Variable {self.diagnosis_result['broken_variable']}.
Lock the other two variables (keep them unchanged).

Return as JSON array:
[
    {{
        "variation_id": 1,
        "modified_prompt": "full revised prompt",
        "change_description": "what specifically changed",
        "test_hypothesis": "what this should fix"
    }},
    ...
]

Output ONLY valid JSON, no other text."""

        response = call_with_retry(
            lambda: client.messages.create(
                model=META_MODEL,
                max_tokens=4000,
                messages=[{"role": "user", "content": variation_prompt}]
            ),
            context="variation generation"
        )

        variations = json.loads(response.content[0].text)
        return variations

    def _test_variations(self) -> List[Dict]:
        """Run each variation against all test cases."""
        results = []
        for var_idx, variation in enumerate(self.variations):
            print(f"  Testing Variation {var_idx + 1}/{len(self.variations)}...")
            variation_results = self._test_single_variation(variation)
            results.append(variation_results)
        return results

    def _score_results(self) -> List[Dict]:
        """Use LLM-as-Judge to score each variation's performance."""
        scored = []
        for result in self.results:
            score = self._score_single_result(result)
            scored.append(score)
        return scored

    def _select_winner(self, scored_results: List[Dict]) -> Dict:
        """Select the best-performing variation."""
        # Sort by overall_score
        sorted_results = sorted(scored_results,
                                key=lambda x: x["overall_score"],
                                reverse=True)
        winner = sorted_results[0]

        # Calculate improvement over baseline
        if self.baseline_score and self.baseline_score > 0:
            improvement = ((winner["overall_score"] - self.baseline_score) / self.baseline_score) * 100
        else:
            improvement = 0

        winner["improvement"] = improvement
        winner["score"] = winner["overall_score"]

        # Attach the winning variation's prompt
        winning_variation = next(v for v in self.variations
                                 if v["variation_id"] == winner["variation_id"])
        winner["optimized_prompt"] = winning_variation["modified_prompt"]
        winner["change_description"] = winning_variation["change_description"]
        return winner

    def _test_combinations(self, current_winner: Dict) -> Optional[Dict]:
        """Phase 2: Test combinations of winning variables (optional).

        Tests:
        - Best I + Best T (keep original E)
        - Best I + Best E (keep original T)
        - Best T + Best E (keep original I)
        """
        print("  Generating combination variations...")

        # Extract the best variation for each variable type
        # For now, we'll use the current winner for the diagnosed variable
        # and keep originals for the others
        broken_var = self.diagnosis_result['broken_variable']
        best_variation = next(v for v in self.variations
                              if v["variation_id"] == current_winner["variation_id"])

        # Create combinations by merging the optimized variable with originals
        # Note: This is a simplified implementation. A full implementation would
        # need to parse and extract I/T/E from prompts, which is complex.
        # For now, we'll generate new combination prompts via LLM
        combo_prompt = f"""You previously optimized variable {broken_var} in this prompt:

Original Prompt:
{self.original_prompt}

Optimized {broken_var}:
{best_variation['modified_prompt']}

Now generate 3 combination variations that test interactions:
1. Optimize both I and T (keep original E)
2. Optimize both I and E (keep original T)
3. Optimize both T and E (keep original I)

Since you previously optimized {broken_var}, incorporate that improvement into the relevant combinations.

Return as JSON array:
[
    {{
        "variation_id": "combo_1",
        "modified_prompt": "full combined prompt",
        "change_description": "I+T combination",
        "test_hypothesis": "Tests I/T interaction"
    }},
    ...
]

Output ONLY valid JSON, no other text."""

        try:
            response = call_with_retry(
                lambda: client.messages.create(
                    model=META_MODEL,
                    max_tokens=4000,
                    messages=[{"role": "user", "content": combo_prompt}]
                ),
                context="combination generation"
            )
            combinations = json.loads(response.content[0].text)

            # Test each combination
            print(f"  Testing {len(combinations)} combinations...")
            combo_results = []
            for combo in combinations:
                result = self._test_single_variation(combo)
                score = self._score_single_result(result)
                combo_results.append(score)

            # Find best combination
            best_combo = max(combo_results, key=lambda x: x["overall_score"])

            # Attach prompt and metadata
            combo_variation = next(c for c in combinations
                                   if c["variation_id"] == best_combo["variation_id"])
            best_combo["optimized_prompt"] = combo_variation["modified_prompt"]
            best_combo["change_description"] = combo_variation["change_description"]
            best_combo["score"] = best_combo["overall_score"]

            # Calculate improvement over baseline
            if self.baseline_score and self.baseline_score > 0:
                best_combo["improvement"] = ((best_combo["overall_score"] - self.baseline_score) /
                                             self.baseline_score) * 100
            else:
                best_combo["improvement"] = 0

            return best_combo
        except Exception as e:
            print(f"  ⚠ Combination testing failed: {e}")
            return None

    def _format_final_report(self, winner: Dict) -> Dict:
        """Format the final optimization report."""

        report = {
            "original_prompt": self.original_prompt,
            "diagnosis": self.diagnosis_result,
            "optimized_prompt": winner["optimized_prompt"],
            "performance": {
                "score": winner["overall_score"],
                "improvement": winner["improvement"],
                "pass_rate": winner["pass_rate"]
            },
            "changes_made": winner["change_description"],
            "recommendations": winner.get("weaknesses", [])
        }

        return report


def load_test_cases_from_json(filepath: str) -> List[TestCase]:
    """Load test cases from JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)

    return [TestCase(tc["input"], tc["expected"], tc.get("actual"))
            for tc in data["test_cases"]]


def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description='Automated I/T/E Prompt Optimizer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Run with built-in example
    python optimize_prompt.py

    # Use custom prompt and test cases
    python optimize_prompt.py --prompt my_prompt.txt --tests test_cases.json

    # Generate more variations and test combinations
    python optimize_prompt.py --num-variations 5 --test-combinations

    # Skip baseline testing to save cost
    python optimize_prompt.py --skip-baseline
        """
    )

    parser.add_argument(
        '--prompt',
        type=str,
        help='Path to file containing the failing prompt (default: use built-in example)'
    )
    parser.add_argument(
        '--tests',
        type=str,
        help='Path to JSON file containing test cases (default: use built-in example)'
    )
    parser.add_argument(
        '--success-criteria',
        type=str,
        help='Success criteria description (default: use built-in example)'
    )
    parser.add_argument(
        '--num-variations',
        type=int,
        default=3,
        help='Number of variations to generate (default: 3)'
    )
    parser.add_argument(
        '--test-combinations',
        action='store_true',
        help='Enable Phase 2 combination testing (tests I+T, I+E, T+E interactions)'
    )
    parser.add_argument(
        '--skip-baseline',
        action='store_true',
        help='Skip baseline testing (saves cost but less accurate improvement metrics)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='optimization_result.json',
        help='Output file for optimization report (default: optimization_result.json)'
    )

    args = parser.parse_args()

    # Load prompt
    if args.prompt:
        with open(args.prompt, 'r') as f:
            failing_prompt = f.read().strip()
    else:
        # Use built-in example
        failing_prompt = """You are a Worker Agent. Read feature_list.md and complete one task."""

    # Load test cases
    if args.tests:
        test_cases = load_test_cases_from_json(args.tests)
    else:
        # Use built-in example
        test_cases = [
            TestCase(
                input="feature_list.md contains '- [ ] Add login button'",
                expected="Agent writes code AND marks task as [x]",
                actual="Agent writes code but doesn't update the file"
            ),
            TestCase(
                input="feature_list.md contains '- [ ] Write tests'",
                expected="Agent writes tests THEN marks [x]",
                actual="Agent marks [x] without writing tests"
            ),
            TestCase(
                input="feature_list.md contains '- [ ] Fix bug in auth.py'",
                expected="Agent fixes bug, writes test, marks [x]",
                actual="Agent fixes bug but skips test and marking"
            )
        ]

    # Load success criteria
    if args.success_criteria:
        success_criteria = args.success_criteria
    else:
        # Use built-in example
        success_criteria = """
        - Agent must update feature_list.md to [x] after completing task
        - Agent must not mark [x] until work is actually done
        - Agent must write tests for any code changes
        """

    # Run optimization
    optimizer = PromptOptimizer(
        failing_prompt,
        test_cases,
        success_criteria,
        num_variations=args.num_variations,
        test_combinations=args.test_combinations,
        skip_baseline=args.skip_baseline
    )
    result = optimizer.run_optimization()

    # Handle early exit (e.g., user aborted or prompt already optimal)
    if result is None:
        return

    # Print final report
    print("\n" + "=" * 80)
    print("OPTIMIZATION REPORT")
    print("=" * 80)
    print(f"\n 📊 Performance Score: {result['performance']['score']}/100")
    print(f" 📈 Improvement: +{result['performance']['improvement']:.1f}%")
    print(f" ✅ Pass Rate: {result['performance']['pass_rate']}")
    print(f"\n 🔧 Changes Made:")
    print(f"    {result['changes_made']}")
    print(f"\n ✨ Optimized Prompt:")
    print("    " + "-" * 76)
    for line in result['optimized_prompt'].split('\n'):
        print(f"    {line}")
    print("    " + "-" * 76)

    if result.get('recommendations'):
        print(f"\n ⚠ Remaining Issues:")
        for rec in result['recommendations']:
            print(f"    - {rec}")

    # Save to file
    with open(args.output, 'w') as f:
        json.dump(result, f, indent=2)
    print(f"\n 💾 Full report saved to: {args.output}")


if __name__ == "__main__":
    main()
```

---

## Usage Guide

### Basic Usage

```bash
# Run with the built-in example
python optimize_prompt.py

# Provide your own prompt and test cases
python optimize_prompt.py --prompt my_prompt.txt --tests my_test_cases.json

# Generate 5 variations instead of 3
python optimize_prompt.py --num-variations 5

# Enable Phase 2 combination testing
python optimize_prompt.py --test-combinations

# Skip baseline testing to save API costs
python optimize_prompt.py --skip-baseline

# Combine multiple options
python optimize_prompt.py --prompt my_prompt.txt --tests my_tests.json --num-variations 5 --test-combinations --output my_result.json
```

---

## Test Cases JSON Format

```json
{
    "test_cases": [
        {
            "input": "Description of what the agent receives",
            "expected": "What the agent should do/output",
            "actual": "What the agent actually did (if known)"
        }
    ]
}
```

---

## Expected Output

```
================================================================================
AUTOMATED I/T/E PROMPT OPTIMIZATION
================================================================================

[Step 1/5] Diagnosing failure type...
✓ Diagnosis complete: Logic Failure
  Broken Variable: I
  Confidence: High

[Step 2/5] Generating prompt variations...
✓ Generated 3 variations

[Step 3/5] Testing variations against test set...
  Testing Variation 1/3...
  Testing Variation 2/3...
  Testing Variation 3/3...
✓ Tested all variations (3 test cases each)

[Step 4/5] Scoring results with LLM-as-Judge...
✓ Scoring complete

[Step 5/5] Selecting best variation...
✓ Winner: Variation 1
  Score: 92.00/100
  Improvement: +84.0%

================================================================================
OPTIMIZATION REPORT
================================================================================

 📊 Performance Score: 92/100
 📈 Improvement: +84.0%
 ✅ Pass Rate: 3/3 tests passed

 🔧 Changes Made:
    Added explicit 3-phase loop with timing constraints

 ✨ Optimized Prompt:
    --------------------------------------------------------------------
    You are a Worker Agent. Follow this protocol:
    PHASE 1 (Read): Read feature_list.md, identify next [ ] task
    PHASE 2 (Execute): Complete that task fully
    PHASE 3 (Update): ONLY after work is complete, mark it [x]

    Constraint: You may NOT mark [x] until Phase 2 is complete.
    ------------------------------------------------------------

 💾 Full report saved to: optimization_result.json
```

---

## Customization Options

### Change Models

Use different models for different stages in the configuration at the top of the file:

```python
META_MODEL = "claude-opus-4-5-20251101"      # Most capable for diagnosis
TEST_MODEL = "claude-sonnet-4-5-20250929"    # Balanced for testing
JUDGE_MODEL = "claude-sonnet-4-5-20250929"   # Fast, reliable judging
```

### Add More Test Cases

The more test cases, the more reliable the optimization:

- **Minimum:** 5 test cases
- **Recommended:** 10–20 test cases
- **Production:** 50+ test cases

### Adjust Scoring Criteria

Modify the `_score_single_result()` method to weight different factors. Example: weight correctness more than format:

```python
judge_prompt = '''...
Scoring weights:
  - Correctness: 70%
  - Format compliance: 20%
  - Efficiency: 10%
...'''
```

---

## Cost Estimation

For a typical optimization run:

| Stage | Call Details | Cost |
|---|---|---|
| Diagnosis | 1 Opus call (~2K tokens) | ~$0.03 |
| Variation Generation | 1 Opus call (~4K tokens) | ~$0.06 |
| Testing | 3 variations × 5 test cases × Sonnet | ~$0.15 |
| Judging | 3 Sonnet calls (~3K tokens each) | ~$0.03 |
| **Total per optimization** | **(with 5 test cases)** | **~$0.27** |

**Recommendation:** Start with 5 test cases during development, scale to 20+ for production validation.

---

## Limitations & Future Enhancements

### Current Limitations

- Requires manual creation of test cases (can't auto-generate them yet)
- Assumes test cases can be run via simple API calls (doesn't handle complex environments)
- LLM-as-Judge may have biases (validate against human judgment initially)

### Possible Enhancements

- Auto-generate test cases from prompt description
- Support for multi-turn agent conversations (not just single prompts)
- Integration with actual agent harnesses (test real Workers, not simulated)
- Iterative optimization (if first round doesn't hit 95%, run again)
