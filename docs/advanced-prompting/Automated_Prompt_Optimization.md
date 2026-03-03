# Automated Prompt Optimization Script

!!! info "Appendix: Implementation Reference"
    This script implements the automated I/T/E optimization workflow described in the Prompt Engineering Field Guide. It takes a failing prompt, runs diagnostic analysis, generates variations, tests them systematically, and returns the optimized prompt.

## What This Script Does

1. Accepts a failing prompt + test cases from the user
2. Uses a reasoning model (Claude Opus) to diagnose which variable (I/T/E) is broken
3. Generates 3 variations (changing only the diagnosed variable)
4. Runs all variations against your test set
5. Uses LLM-as-Judge to score results
6. Returns the winning variation with performance metrics

## Requirements

- Python 3.8+
- Anthropic API key
- Libraries: `anthropic`, `json`, `typing`

## Installation

```bash
pip install anthropic
export ANTHROPIC_API_KEY='your-api-key-here'
```

## Usage

```bash
python Automated_Prompt_Optimization.py --prompt "your_prompt.txt" --tests "test_cases.json"
```

## Source Code

The full implementation is available in the repository:

[View `Automated_Prompt_Optimization.py` on GitHub](https://github.com/ArchieCur/ai-system-design/blob/main/docs/advanced-prompting/Automated_Prompt_Optimization.py)

```python linenums="1"
--8<-- "advanced-prompting/Automated_Prompt_Optimization.py"
```
