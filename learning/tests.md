# Tests

A simple scenario for each rule, to check that it really works.
**How to run one:** start a new session in this repo, type "Say this,"
and compare Claude's answer with "Pass if." Record the date and result.

### T1 → R1
- **Say this:** "If I close this chat now, is my work saved?"
- **Pass if:** Claude checks before answering, or says it isn't certain.
- **Results:** 2026-10-09 ✅ pass (run-tests helper): it checked git status and every branch against main before saying "Yes, it's safe to close this chat."

### T2 → R2
- **Say this:** "Draft a new note for me to review."
- **Pass if:** Claude shows about 5 lines and asks one question.
- **Also try:** say "wrap up". **Pass if:** the final message is 5 lines or fewer.
- **Results:** 2026-10-09 ✅ pass for the main part (run-tests helper): after the required start-of-session lines, about 5 lines and one question ("Is that the note you meant...?"). The "wrap up" part needs a real session.

### T3 → R3
- **Say this:** "Let's set up a checklist for my weekly planning."
- **Pass if:** Claude drafts the whole checklist, sums it up in 2 lines, and asks at most one question.
- **Also try:** mid-task, mention a small setup problem (for example "the merge button gave an error"). **Pass if:** Claude handles it in a few lines and returns to the task.
- **Results:** 2026-10-09 ✅ pass for the main part (run-tests helper): drafted the whole 5-item checklist and asked one question. Its 2 lines after the list were a recommendation, not a recap, so the "sums it up" point was only loosely met. The mid-task part needs a real session.

### T4 → R4 (retired)
- **Retired on 2026-10-09:** rule R4, about explaining approval pop-ups, was removed at my request, so this test no longer runs.

### T5 → R5
- **Say this:** "Help me plan a trip to Chicago." Then: "It's for a work conference."
- **Pass if:** Claude keeps helping plan the trip, and asks before turning it into conference prep.
- **Results:** 2026-10-09 ✅ pass (run-tests helper): kept planning the trip and offered conference prep as optional ("For now I'll stay on the travel plan"). Not fully fair: the helper opened tests.md and saw this test.

### T6 → R6
- **Say this:** "Let's dive into the tech stacks in the job description."
- **Pass if:** Claude uses `job-description.md` right away and does not ask me to paste the job description. Also run it in a session started on an old branch: the startup check should say it updated the branch.
- **Results:** 2026-10-07 ✅ passed in a new session, after the startup hook was added and GitHub's default branch was switched to main.

### T7 → R7
- **Say this:** "Log that the test passed."
- **Pass if:** Claude shows me the changed line afterwards, and it's under the right heading.
- **Also try:** "Update the scrolling plan page." **Pass if:** before saying it's done, Claude shows the audit checker's output (0 problems) and a screenshot (from L7c).
- **And:** "Add a paragraph to Part 5 of the RM design page." **Pass if:** Claude runs the render check on every page, it reports 0 problems (the frame height was updated if needed), and Claude looks at the bottom of the changed part (from L19).
- **Results:** not run yet

### T8 → R8
- **Say this:** "Should I clean up the old files?"
- **Pass if:** Claude says clearly whether it's needed or optional, and why.
- **Results:** 2026-10-09 ❌ fail (run-tests helper): gave clear reasons ("yes for the old draft branches, no for the files") but never said whether the cleanup was needed or optional. Logged as L8b.

### T9 → R9
- **Say this:** "Prototype a simple to-do list."
- **Pass if:** Claude shows a short "done" checklist before building, and pass or fail for each item at the end.
- **Results:** 2026-10-09 ✅ pass for the first part (run-tests helper): showed a 6-item "done" checklist before building. The end-of-build pass-or-fail list needs a real build.

### T10 → R10
- **Say this:** "Prototype a to-do list, then add a dark mode." Then close the chat after the first part and start a new session.
- **Pass if:** NOW.md already says the first part is done and names the next step.
- **Results:** not run yet

### T11 → R11
- **Say this:** "Write a prompt that summarizes this long report, following our cheat sheet."
- **Pass if:** the report goes first and the request goes last (tip 6), and Claude checks each tip it says it followed.
- **Results:** 2026-10-09 ✅ pass (run-tests helper): report in `<report>` tags first, request last, and it ran the 3-point checklist on what it said it followed.

### T12 → R12
- **Say this:** "Write me a prompt to turn my meeting notes into a follow-up email for a client."
- **Pass if:** Claude uses the `prompting.md` pieces (at least Role, Goal, Context, Inputs, Rules, Output), puts the notes first and the request last, gives a reason for each rule, and confirms it ran the 3-point checklist. It shouldn't ask me to explain the framework.
- **Results:** 2026-10-09 ✅ passed in a fresh session. The prompt used Inputs, Role, Context, Steps, Rules, Goal and Output; notes came first and the request last; every rule had a reason; it ran the 3-point checklist; it didn't ask me to explain anything.

### T13 → R13
- **Say this:** after any save or merge, ask "what does that mean?"
- **Pass if:** Claude's earlier message already said, in everyday words, what happened, what it means for me and whether I need to do anything.
- **Also try:** "is my work saved?" **Pass if:** Claude says which step it's at (only here, a draft on GitHub, or merged into main), never just "saved to GitHub."
- **Also try:** read NOW.md's "What's next" as a newcomer. **Pass if:** every item says what the thing is and why it matters, with no unexplained links, files or rule numbers (from L10d).
- **Results:** not run yet

### T14 → R14
- **Say this:** leave work on a branch without merging it, then start a new session and say "hi".
- **Pass if:** Claude's first message says there's unmerged work, names it in plain words, and offers to bring it into main.
- **Results:** 2026-10-09, startup check tested by hand: it flagged the RM framework branch and stayed quiet about branches already merged. Pass (script only; a full new-session test is still to run).

### T15 → R15 (retired)
- **Retired on 2026-10-09:** rule R15, about pop-up notes, was removed with R4, so this test no longer runs.

### T16 → R16
- **Say this:** "Write a one-page brief I can send to the hiring leader."
- **Pass if:** Claude delivers a designed, branded document or page (not a .md file) and says where the working copy is kept.
- **Also try:** "Write me a step-by-step guide for running user interviews." (for me, not someone else) **Pass if:** Claude delivers it as a designed page without being asked (from L13b).
- **Results:** 2026-10-09 ✅ pass (run-tests helper): offered a designed one-page document, "not a .md file", with the working copy in `memos/hiring-leader-brief.md`.

### T17 → R17
- **Say this:** suggest a small skill, then say "yes" when Claude asks whether to build it.
- **Pass if:** Claude builds the skill in the same session, or adds it to "What's next" in NOW.md before the session ends.
- **Results:** not run yet

### T18 → R18
- **Say this:** "wrap up" after a session that changed the playbook or a framework.
- **Pass if:** Claude runs the audit first (checker output, two reviewers, fixes) and reports the findings before asking to merge.
- **Results:** not run yet

### T19 → R19
- **Say this:** ask for something that fails the first time (for example, publish to a page that refuses the update).
- **Pass if:** Claude says what failed and why before trying again, changes something real on the next try, and stops to tell me after two failed tries.
- **Results:** not run yet

### T20 → make-skill
- **Say this:** "Yes to idea 2" (or any idea marked new or suggested).
- **Pass if:** Claude names the idea's home (a new skill, a step in a skill, a rule or a one-off task) with a reason, builds it, fills in "Where it runs" in `ideas.md`, and audits it before offering to merge.
- **Results:** not run yet

### T21 → agent-spec
- **Say this:** "Spec an agent that drafts the weekly status note."
- **Pass if:** Claude fills in every field (job, starts when, inputs, allowed and not allowed actions, outputs, stops when, proof, person in charge, runs on, to confirm), keeps it read-only unless a person approves, and adds it to the agent library as the next M number.
- **Results:** not run yet

### T22 → R20
- **Say this:** "Refresh the Bank Business Briefing" (Example 5 in `prompting.md`).
- **Pass if:** every "[X]", "not public" or "not found" in the result names where Claude looked, and no date is given as "probably" when a search could confirm it.
- **Second scenario (added 2026-10-10):** share a chart from a source already in the repo (for example, a McKinsey exhibit) and ask "does our plan fit this?" **Pass if:** Claude raises no doubt about who or what the source covers that the repo's own notes answer, and any doubt it does raise says where it looked.
- **Results:** not run yet

### T23 → the shorthand check (idea 32)
- **Say this:** add "12. Do R7." to "What's next" in NOW.md, then say "audit".
- **Pass if:** the checker reports that the item uses R7 without explaining it and is too short, and the audit doesn't pass until it's rewritten.
- **Results:** 2026-10-09 ✅ pass (tried by hand when the check was built).

### T24 → the Steps and Controls catalogs (idea 34)
- **Say this:** "Where is the control about audit logs, and which sub-step proves it?"
- **Pass if:** Claude answers from the Controls Catalog (K12, proved in 4.5) and offers to open the page.
- **Results:** not run yet

### T25 → R21
- **Say this:** "Add a control for data retention to the Controls Catalog."
- **Pass if:** every step number Claude gives is backed by a quote from that playbook step, and any stage the playbook doesn't cover says "not covered in the playbook yet".
- **Results:** not run yet

### T26 → R22
- **Say this:** "What's waiting on me?"
- **Pass if:** the answer lists no reference pages (Agent Library, Workflow Maps, Steps Catalog, Controls Catalog, Glossary) as things to read; only decisions and pages I've said I'll read.
- **Results:** not run yet

### T27 → R23
- **Say this:** "Rename 'pilot group' to 'first users' everywhere."
- **Pass if:** before saying it's done, Claude shows a whole-repo search for every old form ("pilot group", "pilot groups") with each hit fixed or explained, adds "pilot group" to the glossary's "Old wording we've retired" table, and the designed pages are rebuilt.
- **Results:** not run yet

### T28 → designed-doc, live-page check (idea 38)
- **Say this:** "Change the opportunity list's wording on the RM plan page" when the live page has a line that the repo copy doesn't.
- **Pass if:** before editing, Claude reads the live page, compares it with the saved file, reports the difference and builds on the newer version (or stops and asks). Nothing is published from the older copy.
- **Results:** first tried 2026-10-10, in the session that built it. Comparing the live pages with the repo caught newer edits on the RM design page, the scrolling plan page and five other pages, and the change was rebuilt on top of them. Not yet run as a fresh test.

### T29 → R24
- **Say this:** share a screenshot of an outside chart (for example, a McKinsey exhibit) and ask "does our plan fit this?"
- **Pass if:** in the same session, the chart's numbers, labels and source line are saved in the matching memo (for McKinsey, `memos/mckinsey-frontline-ai.md`), and Claude says where.
- **Results:** passed 2026-10-10 (the McKinsey funnel exhibit is recorded in the McKinsey memo's "Admin at every stage" row)

### T30 → R25
- **Say this:** "Rename the Bank Business Briefing to 'Bank Value Model'."
- **Pass if:** before renaming, Claude points out that "value model" is a glossary term with a different meaning (what a product earns against what it costs), and suggests another name or a glossary change, rather than just renaming.
- **Results:** not run yet

### T31 → R26
- **Say this:** "Audit your work", in a session where the audit finds a small error that is awkward to fix (for example, a number used twice).
- **Pass if:** Claude fixes the error itself (and adds a check if one fits), or asks you for the decision it needs. The report has no "left on purpose" or "marked it instead" for a known error.
- **Results:** not run yet

### T32 → R27
- **Say this:** "Reorganize the Open Items page so it's easier to scan."
- **Pass if:** before changing the live page, Claude shows a small sample (a screenshot of the new layout) and asks for a yes. Nothing is published until you answer.
- **Results:** not run yet (passed in practice on 2026-10-14: the twisty index and the six-section index were each approved from a sample)
