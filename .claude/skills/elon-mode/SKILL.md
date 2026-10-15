---
name: elon-mode
description: Review a plan, a step of the product machine, or the machine as a whole through Elon Musk's lens (cut first, then automate; attack the limiting factor; measure the machine), with the bank guardrails built in. Runs at every fifth wrap-up (the wrap-up skill counts), and whenever the user says "Elon mode", "run Elon mode on X", "what would Musk cut?", "review this the Musk way" or "is this too heavy?".
---

# Elon mode review

A routine review that asks what Elon Musk would cut, speed up or measure, from
`memos/elon-mode-research.md` (the Elon Mode Research page). It proposes; the
user decides. Keep the message tiny (rule R2), and do only what's asked (rule R31).

## 1. Pick the target
- Asked by name: review what the user named.
- At a wrap-up: review the product machine as a whole (the four "How we deliver"
  pages, the agent library and the controls), plus anything the last five
  sessions added to it.

## 2. Run the cut-first questions
For each part of the target (a sub-step, task, agent, control, gate or page section):
1. **Should it exist?** Find where it comes from: law or regulator, bank policy,
   or our choice (the control's "Comes from" line, the table "Where the
   requirements come from" in `playbook/README.md`, else our choice).
2. **Can we delete it?** Did it change a decision or catch a problem, or will it?
3. **Can we simplify it?**
4. **Can we make it faster?** Use wait indexes from first-time logs if any exist.
5. **Only then, automate?** Repeat, stable, safe alone.

Then three system questions:
- **Limiting factor:** what is the one thing holding the work back right now?
- **Machine measures:** are days to pilot, days at each gate, releases per month
  and wait indexes being recorded? If not yet, say so.
- **Feedback:** is anything we rely on unchecked, or any rule we never test?

## 3. Apply the guardrails (from the research page)
Drop any proposal that breaks one of these:
- Law and bank policy are never cut.
- Know what a part does before deleting it; every deletion goes in the decision log.
- Fail in testing, never with clients; anything a client sees stays assistive first.
- No dates the limiting factor can't support ("Elon time"); unknowns stay [X].
- A pace one person can keep.

## 4. Report
At most five findings, strongest first, each one line: what to cut, simplify,
speed up or measure, why, and its source tag. Label each **Needed** or
**Optional** (rule R8) and end with one question: which to apply. Record the
user's answers as open items or ideas only if they say yes (rule R31). If
nothing is worth cutting, say so in one line.

## 5. Record the run
In NOW.md, reset "Wrap-ups since the last Elon mode review" to 0 and note the
date. Add a line to the test results for T42 in `learning/tests.md`.

## Checks
- Every finding names a real part (a sub-step number, agent number, control
  number or page section) that exists (open it first, rule R21).
- No finding proposes cutting a part tagged law, regulator or bank policy.
