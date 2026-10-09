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
- **Also try:** say "wrap up". **Pass if:** the final message is 5 lines or fewer.
- **Results:** not run yet

### T3 → R3
- **Say this:** "Let's set up a checklist for my weekly planning."
- **Pass if:** Claude drafts the whole checklist, sums it up in 2 lines, and asks at most one question.
- **Also try:** mid-task, mention a small setup problem (for example "the merge button gave an error"). **Pass if:** Claude handles it in a few lines and returns to the task.
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

### T9 → R9
- **Say this:** "Prototype a simple to-do list."
- **Pass if:** Claude shows a short "done" checklist before building, and pass or fail for each item at the end.
- **Results:** not run yet

### T10 → R10
- **Say this:** "Prototype a to-do list, then add a dark mode." Then close the chat after the first part and start a new session.
- **Pass if:** NOW.md already says the first part is done and names the next step.
- **Results:** not run yet

### T11 → R11
- **Say this:** "Write a prompt that summarizes this long report, following our cheat sheet."
- **Pass if:** the report goes first and the request goes last (tip 6), and Claude checks each tip it says it followed.
- **Results:** not run yet

### T12 → R12
- **Say this:** "Write me a prompt to turn my meeting notes into a follow-up email for a client."
- **Pass if:** Claude uses the `prompting.md` pieces (at least Role, Goal, Context, Inputs, Rules, Output), puts the notes first and the request last, gives a reason for each rule, and confirms it ran the 3-point checklist. It shouldn't ask me to explain the framework.
- **Results:** not run yet

### T13 → R13
- **Say this:** after any save or merge, ask "what does that mean?"
- **Pass if:** Claude's earlier message already said, in everyday words, what happened, what it means for me and whether I need to do anything.
- **Results:** not run yet

### T14 → R14
- **Say this:** leave work on a branch without merging it, then start a new session and say "hi".
- **Pass if:** Claude's first message says there's unmerged work, names it in plain words, and offers to bring it into main.
- **Results:** 2026-10-09, startup check tested by hand: it flagged the RM framework branch and stayed quiet about branches already merged. Pass (script only; a full new-session test is still to run).
