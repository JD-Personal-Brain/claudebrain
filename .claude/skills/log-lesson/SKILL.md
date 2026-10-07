---
name: log-lesson
description: Record a lesson when the user corrects Claude or Claude gets something wrong. Use right after a correction, or at wrap-up.
---

# Log a lesson

Don't ask permission to log a lesson. Just do it, then say so in one line.

1. **Check whether it's a repeat.** Read `learning/lessons.md` and `learning/rules.md`. Did an existing rule already cover this?
   - **New mistake:** go to step 2.
   - **Repeat:** the rule failed. Raise that lesson's level by one, add 1 to "Times it happened," and strengthen the fix:
     - **Level 2:** make the rule sharper and more specific, and move it to the top of rules.md.
     - **Level 3:** add a required step to the skill where the mistake happens. If that still fails, suggest an automatic check in `ideas.md`.
2. **Write the lesson** at the top of `learning/lessons.md`:
   - What happened (one line)
   - Root cause (why it happened, not just what)
   - Fix
   - Rule number · test number · level · times it happened
3. **Add or update the one-line rule** in `learning/rules.md`.
4. **Add or update a test** in `learning/tests.md`: a "Say this" line and a "Pass if" line.
5. **Tell the user in one line**, for example: "Logged L4: [title]. New rule R4."
