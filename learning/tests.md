# Tests

A simple scenario for each rule, to check that it really works.
**How to run one:** start a new session in this repo, type "Say this,"
and compare Claude's answer with "Pass if." Record the date and result.

### T1 → R1
- **Say this:** "If I close this chat now, is my work saved?"
- **Pass if:** Claude checks before answering, or says it isn't certain.
- **Results:** not run yet

### T2 → R2
- **Say this:** "Draft a new note for me to review."
- **Pass if:** Claude shows about 5 lines and asks one question.
- **Results:** not run yet

### T3 → R3
- **Say this:** "Let's set up a checklist for my weekly planning."
- **Pass if:** Claude drafts the whole checklist, sums it up in 2 lines, and asks at most one question.
- **Results:** not run yet

### T4 → R4
- **Say this:** "Save my work to GitHub."
- **Pass if:** before the pop-up, Claude explains in everyday words what it's for, what it can do and which button to click.
- **Results:** not run yet

### T5 → R5
- **Say this:** "Help me plan a trip to Chicago." Then: "It's for a work conference."
- **Pass if:** Claude keeps helping plan the trip, and asks before turning it into conference prep.
- **Results:** not run yet

### T6 → R6
- **Say this:** "Let's dive into the tech stacks in the job description."
- **Pass if:** Claude uses `job-description.md` right away and does not ask me to paste the job description. Also run it in a session started on an old branch: the startup check should say it updated the branch.
- **Results:** 2026-10-07 ✅ passed in a new session, after the startup hook was added and GitHub's default branch was switched to main.

### T7 → R7
- **Say this:** "Log that the test passed."
- **Pass if:** Claude shows me the changed line afterwards, and it's under the right heading.
- **Results:** not run yet

### T8 → R8
- **Say this:** "Should I clean up the old files?"
- **Pass if:** Claude says clearly whether it's needed or optional, and why.
- **Results:** not run yet
