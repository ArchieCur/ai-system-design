# Tool Templates

## There are 3 tool templates included. A Fill-in-the-Blank template for intermediate to advanced users. A Minimal template for simple tools. And a template for Non-Coders.

**Scope:** These templates cover tool definition- how to structure a tool so a model can understand when and how to use it. 
They do not cover programmatic tool orchestration, which is how your code controls when tools fire, 
in what sequence, and how errors are handled outside the model's reasoning process. 
For production agents and multi-agent systems where reliability and context hygiene matter, see Programmatic_Tool_Calling.md.
---

## Tool Definition Template: Fill-in-the-Blank Edition

**Instructions:** Replace all [BLANK] sections with your specific information. Delete optional sections if not needed. Copy this entire template for each tool you create.

---

### BASIC INFORMATION

```json
{
  "name": "[TOOL_NAME]",
  // Example: "send_email", "get_user_profile", "calculate_mortgage"

  "description": "[ONE SENTENCE: What does this tool do?]",
  // Example: "Sends an email to a specified recipient with subject and body"
  // Example: "Retrieves a single user's complete profile from the database"
  // Example: "Calculates monthly mortgage payment including principal and interest"

  "class": "[A, B, or C]",
  // A = Read-Only (no side effects, safe to use freely)
  // B = State-Change (modifies data, requires confirmation)
  // C = Computational (task exceeds Claude's reasoning capability)
```

---

### TRIGGER LOGIC (When a Model Should Use This)

```json
  "trigger_logic": {
    "use_when": [
      "[Scenario 1: When should Claude use this tool?]",
      "[Scenario 2: Another situation where this tool is appropriate]",
      "[Scenario 3: Add more as needed]"
    ],
    // Examples:
    // - "User asks to send an email or message"
    // - "User requests information about a specific person"
    // - "User needs complex financial calculation"

    "dont_use_when": [
      "[Scenario 1: When should Claude NOT use this? Use reasoning instead?]",
      "[Scenario 2: When should a different tool be used instead?]",
      "[Scenario 3: What edge cases fail?]"
    ]
    // Examples:
    // - "User is asking ABOUT email (explain, don't send)"
    // - "General questions about users (use search_users for multiple)"
    // - "Simple calculations Claude can do (e.g., 15% of 200)"
  },
```

---

### PARAMETERS (What Inputs Does This Tool Accept?)

```json
  "parameters": {
    "[parameter_name]": {
      "type": "[string/number/boolean/array/object]",
      "description": "[What is this parameter for?]",
      "required": [true/false],
      "example": "[Example value]",
      "constraints": "[Any validation rules? e.g., 'must be valid email format']"
    },
    // Repeat for each parameter

    // Example:
    // "email_address": {
    //   "type": "string",
    //   "description": "Recipient's email address",
    //   "required": true,
    //   "example": "user@example.com",
    //   "constraints": "Must be valid email format (name@domain.com)"
    // }
  },
```

---

### NEGATIVE CONSTRAINTS (What a Model Should NEVER Do)

```json
  "negative_constraints": {
    "do_not": [
      "[Common mistake 1: What should Claude avoid?]",
      "[Common mistake 2: What input patterns cause failure?]",
      "[Common mistake 3: What behaviors cause loops?]"
    ],
    // Examples:
    // - "Do not execute with empty or null input (validate first)"
    // - "Do not assume field names that aren't in the schema"
    // - "Do not retry the same failed input without modification"

    "safety": [
      "[Safety rule 1: What data should never be exposed?]",
      "[Safety rule 2: What are the rate limits?]",
      "[Safety rule 3: What are the timeout thresholds?]"
    ]
    // Examples:
    // - "Never return password or API key fields in responses"
    // - "Limit to 100 results maximum"
    // - "Timeout after 5 seconds"
  },
```

---

### RETURN CONTRACT (What to Expect When the Tool Runs)

**Success Case:**

```json
  "return_contract": {
    "success": {
      "type": "[object/array/string/number/boolean]",
      "description": "[What does successful output look like?]",
      "schema": {
        "[field_name]": "[field_type and description]"
        // Example: "message_id": "string - unique identifier for sent message"
      },
      "example": {
        // Paste a real example of successful output here
        // Example: {"sent": true, "message_id": "msg_abc123"}
      }
    },
```

**Failure Cases:**

```json
    "failure_modes": {
      "[error_type_1]": {
        // Example: "invalid_email", "rate_limit", "timeout"

        "error": "[Human-readable error message]",
        // Example: "Recipient email format is invalid"

        "recovery_action": "[What should Claude DO when this happens?]",
        // Example: "Ask user to verify email address format"

        "retry": [true/false],
        // true = Claude should retry automatically
        // false = Claude should NOT retry (ask user for help)

        "user_action": "[What should Claude tell the user?]"
        // Example: "Please provide email in format: name@domain.com"
      },

      // Copy this block for each error type

      "[error_type_2]": {
        "error": "[What went wrong?]",
        "recovery_action": "[What should Claude do?]",
        "retry": [true/false],
        "user_action": "[What to tell user?]"
      }
    }
  }
```

---

### COMPOSITION (Optional: How This Tool Relates to Others)

```json
  "composition": {
    "typically_followed_by": [
      "[tool_name_1]",
      "[tool_name_2]"
    ],
    // Examples of tools that usually run AFTER this one
    // Example: After "create_user", you typically run "send_welcome_email"

    "prerequisites": [
      "[tool_name_that_must_run_first]"
    ],
    // Tools that MUST run successfully before this one
    // Example: "build_app" must run before "deploy_app"

    "conflicts_with": [
      "[tool_name_that_cant_run_simultaneously]"
    ]
    // Tools that should NOT run at the same time as this one
    // Example: "delete_user" conflicts with "create_user"
  }
}
```

---

### CLASS-SPECIFIC ADDITIONS

**If Class B (State-Change), Add This:**

```json
  "confirmation_required": true,
  "confirmation_template": "[This will [ACTION]. Proceed? (yes/no)]",
  // Example: "This will permanently delete user_profile.json. Proceed? (yes/no)"

  "reversible": [true/false],
  // Can this action be undone?

  "backup_strategy": "[How is data backed up before this operation?]"
  // Example: "File is copied to .backup/ directory before deletion"
```

**If Class C (Computational), Add This:**

```json
  "complexity_justification": "[Why can't Claude do this with reasoning alone?]",
  // Example: "Requires 360 separate calculations (30 years × 12 months)"
  // Example: "Statistical analysis on dataset with 10,000+ rows"

  "estimated_duration": "[How long does this typically take?]",
  // Example: "2-5 seconds for typical inputs"

  "timeout_threshold": "[When should this operation time out?]"
  // Example: "30 seconds maximum"
```

---

## QUICK REFERENCE CHECKLIST

Before finalizing your tool definition, verify:

- [ ] **Name** is clear and descriptive (not generic like "do_thing")
- [ ] **Description** is ONE sentence explaining what it does
- [ ] **Class** is assigned (A, B, or C)
- [ ] **Trigger Logic** has at least 2 "use_when" scenarios
- [ ] **Trigger Logic** has at least 2 "dont_use_when" scenarios
- [ ] **Parameters** all have types, descriptions, and examples
- [ ] **Negative Constraints** list common mistakes to avoid
- [ ] **Return Contract** includes success schema AND example
- [ ] **Failure Modes** include at least 2 error types with recovery actions
- [ ] **Class B tools** have confirmation templates
- [ ] **Class C tools** have complexity justification

---

## COMPLETE EXAMPLE (Filled Template)

Here's what a fully-completed template looks like:

```json
{
  "name": "send_email",
  "description": "Sends an email to a specified recipient with subject and body content",
  "class": "B",

  "trigger_logic": {
    "use_when": [
      "User explicitly asks to send an email or message",
      "Workflow requires notification via email",
      "User provides recipient, subject, and message content"
    ],
    "dont_use_when": [
      "User is asking ABOUT email (explain, don't send)",
      "Recipient email is missing or unclear (ask for clarification first)",
      "User wants to draft email (write content, don't send)"
    ]
  },

  "parameters": {
    "to": {
      "type": "string",
      "description": "Recipient's email address",
      "required": true,
      "example": "user@example.com",
      "constraints": "Must be valid email format (name@domain.com)"
    },
    "subject": {
      "type": "string",
      "description": "Email subject line",
      "required": true,
      "example": "Meeting Reminder",
      "constraints": "Maximum 200 characters"
    },
    "body": {
      "type": "string",
      "description": "Email message content",
      "required": true,
      "example": "Hi, this is a reminder about our 3pm meeting.",
      "constraints": "Maximum 10,000 characters"
    }
  },

  "negative_constraints": {
    "do_not": [
      "Send email with empty subject or body",
      "Send to invalid email addresses (validate format first)",
      "Retry sending the same email multiple times on rate limit errors"
    ],
    "safety": [
      "Never include API keys or passwords in email content",
      "Rate limit: maximum 10 emails per minute",
      "Never send to more than 50 recipients in a single call"
    ]
  },

  "return_contract": {
    "success": {
      "type": "object",
      "description": "Confirmation that email was sent successfully",
      "schema": {
        "sent": "boolean - true if email sent successfully",
        "message_id": "string - unique identifier for tracking"
      },
      "example": {
        "sent": true,
        "message_id": "msg_abc123xyz"
      }
    },
    "failure_modes": {
      "invalid_email": {
        "error": "Recipient email format is invalid",
        "recovery_action": "Ask user to verify email address format",
        "retry": false,
        "user_action": "Please provide email in format: name@domain.com"
      },
      "rate_limit": {
        "error": "Rate limit exceeded (max 10 emails/minute)",
        "recovery_action": "Wait 60 seconds, then retry automatically",
        "retry": true,
        "user_action": "Email will be sent in 60 seconds due to rate limiting"
      },
      "smtp_failure": {
        "error": "Email server temporarily unavailable",
        "recovery_action": "Inform user, do not retry",
        "retry": false,
        "user_action": "Email system is temporarily unavailable. Please try again in a few minutes."
      }
    }
  },

  "composition": {
    "typically_followed_by": ["log_email_sent", "update_notification_status"],
    "prerequisites": ["validate_email_address"],
    "conflicts_with": []
  },

  "confirmation_required": true,
  "confirmation_template": "This will send an email to {to} with subject '{subject}'. Proceed? (yes/no)",
  "reversible": false,
  "backup_strategy": "Email is logged in sent_emails table before sending"
}
```

---

## MINIMAL TEMPLATE (For Simple Tools)

If your tool is simple (like a Class A read-only tool), here's a shorter version:

```json
{
  "name": "[TOOL_NAME]",
  "description": "[ONE SENTENCE: What does this do?]",
  "class": "A",

  "trigger_logic": {
    "use_when": [
      "[When to use this]"
    ],
    "dont_use_when": [
      "[When NOT to use this]"
    ]
  },

  "parameters": {
    "[param_name]": {
      "type": "[type]",
      "description": "[what is this?]",
      "required": [true/false],
      "example": "[example]"
    }
  },

  "return_contract": {
    "success": {
      "type": "[type]",
      "example": {}
    },
    "failure_modes": {
      "not_found": {
        "error": "[What went wrong]",
        "recovery_action": "[What to do]",
        "retry": false
      }
    }
  }
}
```

---

## WORKSHEET FORMAT (For Non-Coders)

Prefer a questionnaire style? Answer these questions:

BASIC INFORMATION

1. Tool name: ____________________
2. What does it do (one sentence)? ____________________
3. Risk level?
   - [ ] Class A - Just reads data (safe)
   - [ ] Class B - Changes data (needs confirmation)
   - [ ] Class C - Complex calculation
WHEN TO USE
4. Claude should use this when:

   - [                            ]
   - [                            ]
5. Claude should NOT use this when:

   - [                            ]
   - [                            ]

INPUTS
6. What information does this tool need?

- Parameter 1:
- Parameter 2:

SAFETY
7. What should Claude never do with this tool?

- [                            ]
- [                            ]

OUTPUTS
8. What does success look like? (Give an example)

[                            ]
9. What errors can happen?

- Error 1: ____________________
- What to do: ____________________
- Error 2: ____________________
- What to do: ____________________

CONFIRMATION (If Class B)
10. What should Claude ask before using this tool?

- "This will ____________________. Proceed?"

## What's Next:

- Programmatic_Tool_Calling
 
END OF TOOL TEMPLATES

version 1.0.0  2026-02-28 


