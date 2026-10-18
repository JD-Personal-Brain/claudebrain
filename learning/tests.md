# Tests

> **Merged rules (2026-10-18).** Tests written for R1, R3, R5, R8, R10, R11, R13, R19, R20, R25 and R34 now test the rule each merged into (see the note at the end of `learning/rules.md`): R1, R11, R20 → R21; R3, R5, R34 → R31; R8, R13 → R2; R10 → R9; R19 → R26; R25 → R23.

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
- **Also try (L33):** ask for a multi-step GitHub task. **Pass if:** the report opens with the outcome and what it means for me, gives at most one step for me, and is about 5 lines.
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
- **And:** "Add a paragraph to section 7 of the RM plan." **Pass if:** Claude edits the plan's working file, rebuilds the page, runs the render check on every page, it reports 0 problems, and Claude looks at the bottom of the changed page (from L19).
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
- **Say this:** "Refresh the Bank Business Briefing" (Prompt 3 in `prompt-library.md`).
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
- **Second part (from L24):** "Merge the side branch," where the branch was written before the Open Items log was renumbered. **Pass if:** Claude searches every file the branch adds or changes for item numbers and shows each one checked against the current log before merging.
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

### T33 → user-workflow skill (idea 41)
- **Say this:** "Map the RM workflow."
- **Pass if:** Claude reads the RM plan, the core use cases and Map 2 before asking anything; lists the RM's stages today with sources or ⚠️; marks which AI product touches each stage and which stages no product touches; shows the work afterwards with [X] for unmeasured time; shows a sample layout and waits for a yes before building the page; and replaces the "RM user workflow" placeholder in the Document Library.
- **Results:** not run yet (first use is W2, next session)

### T34 → jump-link check in the page check (idea 40)
- **Say this:** "Run the page check."
- **Pass if:** the render check clicks every link that jumps within each page, at desktop and phone width, and fails on a link with no target, one that lands on something hidden, one that cuts off the top of its section, or one that lands far below the top.
- **Results:** 2026-10-14 pass: 328 jump-link clicks across 19 pages, 0 problems; a test page with a missing target and a hidden target failed as it should (4 failures).

### T35 → scout run check at session start (rule R28, idea 45)
- **Say this:** start a new session the day after the scout's Monday run.
- **Pass if:** Claude lists the scheduled tasks before its start lines, and mentions the scout only if its last run failed, stalled or is overdue, with the reason.
- **Results:** 2026-10-14 tried once: both scout tasks found, enabled, no runs yet (first run Monday October 19), so nothing to report. Full test after October 19.

### T36 → R29
- **Say this:** "Move the quality bar from the Product Framework into the Product Workflow."
- **Pass if:** before calling it done, Claude shows that every line removed from the framework appears on the workflow page (or names any line it cut on purpose, with the reason), and the audit's `lost-lines.py` output shows each removed sentence found, reworded or cut on purpose.
- **Results:** not run yet.

### T37 → R23 (names I set)
- **Say this:** "Call the Product Machine page 'The Machine' everywhere."
- **Pass if:** Claude changes every form (with and without "the", in files and on the built pages), adds the name to the audit checker's page-name check, and shows the check passing.
- **Results:** not run yet.


### T38 → R30
- **Say this:** "How could the Product Framework and the Product Machine work better together?"
- **Pass if:** Claude's first suggestion is links between the two (each summary item linking to its exact detail, and page-to-page links), keeps each piece of content in one home, and doesn't propose moving or copying content between the pages unless asked.
- **Results:** not run yet.

### T39 → check 12 in the audit checker (idea 48)
- **Say this:** change one sub-step link on the Product Workflow page to a sub-step that doesn't exist, then run the audit checker.
- **Pass if:** the checker names the page and the missing section and counts it as a problem; restoring the link brings it back to 0.
- **Results:** 2026-10-15 pass: a link changed to `#s2-9` was caught ("links to steps.html#s2-9 but that page has no section with that id"); 298 links between pages checked, 0 problems after restoring.

### T40 → wrap-up step 4, two backlog ideas (idea 50)
- **Say this:** "wrap up" in a session that didn't touch any open idea.
- **Pass if:** besides any new ideas, Claude puts forward the two oldest open ideas from `ideas.md` (not done, not "no"), each as one line ending "(yes / no / not yet)", records each answer as the idea's status with the date, and builds every yes in the same session.
- **Results:** not run yet (first run at the next wrap-up).

### T41 → R31
- **Say this:** "Agree with [the top open decision] in Open Items" (one that implies follow-up work, such as changing a plan).
- **Pass if:** Claude records the decision as closed and does nothing else: no new open item, no "next step" in NOW.md or the log, no start on the follow-up work. It may mention the follow-up once, labeled Optional.
- **Also try (L34):** during work on the How we deliver pages, have a reviewer flag a contradiction in a PM page (such as the Use Case Library's portfolio manager section; RM pages are in scope since 2026-10-17). **Pass if:** Claude reports it once as **Optional** and leaves the PM page unchanged.
- **Results:** not run yet.

### T42 → elon-mode skill, and wrap-up step 4 (idea 51)
- **Say this:** "run Elon mode on the Product Machine"; separately, wrap up when NOW.md says 2 wrap-ups since the last Elon mode review (every third wrap-up since 2026-10-18).
- **Pass if:** Claude gives at most five findings, each naming a real sub-step, agent, control or page section, labeled Needed or Optional, none cutting anything tagged law, regulator or bank policy, and ends with one question. At the wrap-up, the count reaches 3, the review runs on the product machine and on this system (rules, skills, checks, pages, open items), only its top finding is shown (one line, with "say 'Elon mode' to see the rest"), and the count resets to 0 with the date. A run on a single plan leaves the count alone.
- **Results:** 2026-10-15 sample run on the Product Machine: pass. Five findings, none touching law or bank policy: the two sponsor meetings in 1.0 and 1.1 could be one (our choice); agent M3 (interview scheduler) may not need to exist if Outlook's scheduling is enough (our choice); the limiting factor for automation is bank question B22 (may automations message people?), which decides every Auto ⚠️ task; the machine's measures can't be recorded until the dry run (W8) sets a baseline; the wait index needs W5's start and finish fields. Not yet run at a real fifth wrap-up. 2026-10-15 first real fifth-wrap-up run (a reviewer helper, on the whole machine): pass. Five findings, none touching law or bank policy: (1) Needed: start the dry run (W8) now instead of waiting on W4, W5 and V1, and shape the templates from it; (2) merge overlapping agents before any is built (M4 into M20, M2 into M23, M29 into M6); (3) cut the first-time log to the light log plus "did this change a decision or catch a problem?"; (4) park "Many projects at once" and the one view of all projects until a second project exists; (5) the sponsor alone decides the Discover gate, with risk still briefed at 1.0. All proposals; none applied (rule R31). 2026-10-17 run on the RM plan (W3, step 3, asked by name): pass. Five findings, none touching law or bank policy (K3, K24, consent and sign-offs kept): (1) Needed: drop the week dates for waves 2 and 3 until gate 2 knows data access and review times; (2) cut wave 1 from five AI products to three (merge meeting follow-up and call notes, both from A3; drop the A6 how-to helper while champions cover it); (3) remove what the plan repeats from the Product Framework and link to it; (4) count freed-up time as hours, not revenue, in the value model; (5) name the limiting factor and its owner up front (the data contract signature). The count was left alone (a single plan). All proposals; none applied (rule R31). Then I said yes to all five, and they were applied the same day (memo v10, closed item C47). 2026-10-17 fifth-wrap-up run on the whole machine: pass. Top finding: gates 3 and 4 are passed per AI product (Product Framework, "Projects, AI products and feature waves"), so an assistant with three wave 1 capabilities on one shared foundation faces three step 4 reviews; let one step 4 review cover a feature wave's capabilities when they share the foundation and add no new data (our choice; the bank's model risk policy has the final word ⚠️). Others: the 2026-10-15 findings (start the dry run W8 now, merge overlapping agents, a lighter first-time log, park "many projects at once") are still open. Count reset to 0. All proposals; none applied (rule R31). 2026-10-18 wrap-up run (the first at the new every-third cadence) on the three RM pages and on this system: pass. Six findings each, none touching law, bank policy or a control; put to me as one list.

### T43 → audit checker check 14, requirement sources (idea 52)
- **Say this:** remove one row (for example 1.3) from "Where the requirements come from" in `playbook/README.md`, then run the checker.
- **Pass if:** the checker names the sub-step and the control it sets, builds, proves or watches, counts it as a problem, and is back to 0 when the row returns.
- **Results:** 2026-10-15 pass: removing the 1.3 row gave "sub-step 1.3 sets, builds, proves or watches K24 (Law or regulator) but isn't in 'Where the requirements come from'"; 0 problems after restoring it.

### T44 → rule R22, no page-read prompts (L30)
- **Say this:** after editing three designed pages, say "republish them".
- **Pass if:** Claude publishes each page straight away (no separate read of each live page first); only if a publish is refused because the live page is newer does it compare that version with the repo and publish again.
- **Results:** not run yet.

### T45 → rule R32, facts only the bank has (L36)
- **Say this:** "give me the to-do list for the portfolio manager work."
- **Pass if:** any item that needs facts only the bank has (such as how PMs work today) is labeled as a draft of assumptions with questions to confirm, not offered as something we can finish now.
- **Results:** not run yet.

### T46 → rule R33, one spine (L37)
- **Say this:** "organize the PM plan on these five themes" (once a PM plan exists).
- **Pass if:** Claude rebuilds the plan around one spine that opens with what the product is, rather than adding the themes as another layer next to the existing ones.
- **Results:** not run yet.

### T47 → audit checker check 17, the RM Assistant page and the RM plan in step (idea 60)
- **Say this:** rename one capability in the RM plan's capability table (for example "Prospect lookalikes" to "Prospect matches"), then run the checker.
- **Pass if:** the checker names the capability on each side as a problem, and is back to 0 when the name is restored.
- **Results:** 2026-10-17 pass: renaming gave two problems (one per page); 0 after restoring it.

### T48 → rule R2, the length warning hook (idea 57)
- **Say this:** ask a question whose full answer would run past 8 lines.
- **Pass if:** after a reply longer than 8 lines, the hook stops Claude once and Claude sends a short follow-up (outcome, what it means, at most one step); it never fires twice in a row.
- **Results:** 2026-10-17 script test: pass (a 12-line reply is stopped, a 3-line reply isn't, a repeat isn't). Not yet seen in a live session; the hook loads from the next session on.

### T49 → rule R34, one user group per page (L38)
- **Say this:** "Cut the PM plan down to a short page for portfolio manager leaders."
- **Pass if:** the short page mentions only portfolio managers (no "RMs next" or RM plan sections); anything about RMs stays in the detail document or the shared pages.
