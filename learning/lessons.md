# Lessons

The full story of each mistake. Newest at the top.
Each lesson produces one rule (in rules.md) and one test (in tests.md).

If a mistake happens again, its fix moves up a level:
1 = a rule · 2 = a sharper rule, moved to the top · 3 = a required step in a skill

---

### L15 · 2026-10-09 · Frameworks offered for merging without an audit
- **What happened:** A full audit of the new playbook and delivery machine found 20 errors in Claude's work, including a step that went in a circle (Define's data, risk and stories each waited on another) and a wrong claim that a US privacy law (GLBA) covers business clients. I had already been asked whether to merge it.
- **Root cause:** Checking was done now and then, only when I asked. Nothing in the process required an audit before work was offered for merging, so errors reached the merge question.
- **Fix:** A new **audit** skill: a mechanical checker, a fresh reviewer, fixes, then a second reviewer to confirm. It runs as step 0 of every wrap-up and before anything that changes frameworks, the playbook, skills, rules, memos or designed pages is offered for merging.
- **Rule:** R18 · **Test:** T18 · **Level:** 3 (required step in the wrap-up skill) · **Times it happened:** 1

### L7c · 2026-10-09 · The scrolling plan page had all 12 tables empty
- **What happened:** The long scrolling RM plan page was published with every table empty: headings showed, but no rows. Claude then made it my default page for reviewing the plan. The audit found it.
- **Root cause:** When the plan was turned into one page, the browser dropped the table rows, because the template's loops sat inside tables. The check looked at a screenshot of the top of the page and never confirmed that the tables had content. A third time a page wasn't checked the way I see it, so it moves to Level 3.
- **Fix:** The audit skill's checker now fails on any empty table in a designed page. The designed-doc skill's on-screen check must run that checker, not just look at one screenshot.
- **Rule:** R7 · **Test:** T7 · **Level:** 3 (required step in the designed-doc and audit skills) · **Times it happened:** 3

### L8b · 2026-10-09 · Didn't say whether cleanup was needed or optional (test T8 failed)
- **What happened:** In a run-tests check, the answer to "Should I clean up the old files?" gave good reasons but never said whether the cleanup was needed or optional.
- **Root cause:** Claude answered "should I?" with a recommendation and treated the reasons as enough. R8 was worded around "giving instructions", so a yes/no recommendation slipped past it. A repeat of L8, so it moves to Level 2.
- **Fix:** Whenever Claude suggests or recommends any action, it starts with the label in bold, **Needed** or **Optional**, followed by a one-line reason.
- **Rule:** R8 · **Test:** T8 · **Level:** 2 (repeat of L8) · **Times it happened:** 2

### L14 · 2026-10-09 · Approved skills were never built
- **What happened:** I had said yes to four skill ideas (run-tests, prototype, write-prompt, new use case), but none were built. When I found out, I was confused about why approved skills didn't exist.
- **Root cause:** Our rules say Claude asks before adding a skill, but nothing says what happens after a yes. Each approval was recorded in `ideas.md` and then the session moved on. Only run-tests made it onto the "What's next" list in NOW.md, so the other three had no reminder at all.
- **Fix:** When I say yes to a skill or idea, Claude builds it in the same session. If there's no time, it goes straight onto "What's next" in NOW.md, so it's never just a row in `ideas.md`.
- **Rule:** R17 · **Test:** T17 · **Level:** 1 · **Times it happened:** 1

### L7b · 2026-10-09 · Said the designed plan was done without looking at it
- **What happened:** Claude published the full plan to the design page and called it done. Only the first quarter showed, because the canvas shows at most 8,000 pixels of each page and the plan was about 32,000. The one-page summary also ran past the bottom of its page. I said the doc was incomplete.
- **Root cause:** Claude checked that the code ran, but never looked at the page the way I would see it. A repeat of L7 (didn't check where a change landed), so it moves to Level 2.
- **Fix:** Before calling a designed page done, render it on screen, measure it, look at a screenshot and confirm nothing is cut off.
- **Rule:** R7 · **Test:** T7 · **Level:** 2 (repeat of L7) · **Times it happened:** 2

### L13 · 2026-10-09 · Gave me Markdown files for documents meant for people
- **What happened:** Claude delivered memo v8 and a one-page summary, meant for the hiring leader, as Markdown (.md) files. I said documents people will read must be real, designed, branded documents, like the earlier RM Analytics Framework design page.
- **Root cause:** Claude treated the repo's working copy as the finished product and didn't ask who would read it. It also missed that a designed version already existed and should be kept up to date.
- **Fix:** Anything another person will read is delivered as a designed, branded document or page (the RM memo lives on its design canvas). The .md file stays as Claude's working copy only. When a designed version exists, update it in place.
- **Rule:** R16 · **Test:** T16 · **Level:** 1 · **Times it happened:** 1

### L12 · 2026-10-09 · Pop-up notes when no pop-up appeared
- **What happened:** Claude put "Click Allow. Deny is always safe." before every GitHub action, but no pop-ups were appearing. I said it made no sense.
- **Root cause:** Claude followed R4's wording ("before every pop-up") as a ritual, without checking whether a pop-up was actually coming. It was noise that made messages longer and less clear.
- **Fix:** Only explain a pop-up when one actually appears or is clearly about to. GitHub actions in my cloud sessions run without pop-ups, so they need no note.
- **Rule:** R15 · **Test:** T15 · **Level:** 1 · **Times it happened:** 1

### L10c · 2026-10-09 · Shorthand a third time, right after the rule was sharpened
- **What happened:** In the wrap-up message, Claude wrote "everything is consistent except the wrap-up routine," "I'm blocked from changing it" and "the exact wording is in idea 16." I said I didn't understand any of it.
- **Root cause:** Claude packed three insider ideas into a few lines to keep the message short, and assumed I knew what they referred to. Keeping it short won out over keeping it clear. A repeat, so it moves to Level 3.
- **Fix:** Level 3 means a required step in a skill, but Claude can't edit its own skills. Until I add it: before sending any wrap-up or status message, Claude rereads it as a newcomer and rewrites any phrase that names something internal without explaining it.
- **Rule:** R13 · **Test:** T13 · **Level:** 3 (repeat of L10, L10b) · **Times it happened:** 3

### L10b · 2026-10-09 · Used shorthand again: "save to GitHub"
- **What happened:** Claude kept saying "save to GitHub" without saying whether it meant a draft (safe but hidden) or merging into main (official). I asked what it meant.
- **Root cause:** Claude used one loose phrase for two different steps, and assumed I knew the difference. A repeat of L10, so it moves to Level 2.
- **Fix:** Name the exact step every time: "save a draft" or "merge into main." Before sending, check every technical phrase is one I'd understand.
- **Rule:** R13 · **Test:** T13 · **Level:** 2 (repeat of L10) · **Times it happened:** 2

### L11 · 2026-10-09 · Work stranded on a branch that never reached main
- **What happened:** The RM analytics framework (memo v6, audit, market scan) from 2026-10-08 was saved only on a side branch on GitHub. No pull request was ever opened, so it never reached main and later sessions couldn't see it. I found out only by asking, and it worried me that so much work could have been lost.
- **Root cause:** Getting work into main depended on someone remembering to wrap up and merge. Nothing checked for work left behind on other branches.
- **Fix:** The startup check now lists any branch with work that isn't in main, at the start of every session. Wrap-up offers to merge right away.
- **Rule:** R14 · **Test:** T14 · **Level:** 1 (plus an automatic check) · **Times it happened:** 1

### L10 · 2026-10-09 · Used shorthand I didn't understand
- **What happened:** After I merged the prototypes, Claude said "NOW.md still lists 'merge the prototypes pull request' as a next step. The next session can tick it off, so you don't need another save just for that." I replied "I don't understand."
- **Root cause:** Claude wrote in its own shorthand: it named an internal file and a to-do item, and said "save" without saying what that would mean for me. It assumed I knew what it was thinking.
- **Fix:** Before sending a message, read it as me: say what happened, what it means for me and whether I need to do anything. Name a file only with a few words on what it is.
- **Rule:** R13 · **Test:** T13 · **Level:** 1 (now 2, see L10b) · **Times it happened:** 1

### L3b · 2026-10-07 · Got too meta (again)
- **What happened:** A session meant for the job's tech stacks turned into a long back-and-forth about branches, permissions and safety checks. I said "it's getting too meta" and "please answer my question."
- **Root cause:** Each problem with the setup pulled Claude into explaining and asking about it, instead of fixing what it could, giving me the one step I had to do, and getting back to the real work. A repeat of L3, so it moves to Level 2.
- **Fix:** When a setup problem comes up, fix what Claude can, give me at most one step to do, and go straight back to the task I asked for. Answer my actual question first, before any side issue.
- **Rule:** R3 · **Test:** T3 · **Level:** 2 (repeat of L3) · **Times it happened:** 2

### L2b · 2026-10-09 · Wrap-up message too long (again)
- **What happened:** At the end of the last session, Claude's final wrap-up message ran about 15 lines (what's in it, a blocked item, 5 merge steps, next session). I said "say less."
- **Root cause:** Rule R2 was there, but the wrap-up skill itself asks for a lot at the end, so Claude followed the skill and forgot the rule. A repeat, so the fix moves to Level 3.
- **Fix:** The wrap-up skill now has a required length check: the final message is 5 lines or fewer.
- **Rule:** R2 · **Test:** T2 · **Level:** 3 (repeat of L2) · **Times it happened:** 3

### L9 · 2026-10-09 · Said an example followed a tip when it didn't
- **What happened:** Claude said Example 2 in `prompting.md` followed tip 6 (long material first, request last). It actually put the Goal at the top and the notes in the middle. I caught it by asking "where's the question?"
- **Root cause:** Claude wrote the example in the template's usual order, then claimed it met the tip without checking it against the tip's actual wording.
- **Fix:** Before saying something follows a tip, rule or standard, check it against that rule's actual wording, point by point. Example 2 is now reordered, and the template has a "long material" note.
- **Rule:** R11 · **Test:** T11 · **Level:** 1 · **Times it happened:** 1

### L8 · 2026-10-07 · Made optional tidying sound required
- **What happened:** Claude gave me step-by-step instructions to delete old branches, and I had to ask why. It was only optional tidying.
- **Root cause:** Claude went straight to the how, and didn't say whether the step was needed.
- **Fix:** Label every step as needed or optional, with a one-line reason.
- **Rule:** R8 · **Test:** T8 · **Level:** 1 · **Times it happened:** 1

### L7 · 2026-10-07 · Recorded a test result on the wrong test
- **What happened:** Claude wrote "T6 passed" under test T1 and told me T6 was marked passed.
- **Root cause:** Claude made the edit with a script and didn't look at where the change landed before reporting it done.
- **Fix:** After editing a file, check the changed line is in the right place before saying it's done.
- **Rule:** R7 · **Test:** T7 · **Level:** 1 · **Times it happened:** 1

### L6b · 2026-10-07 · Said the job description was missing (again)
- **What happened:** Asked for a tech summary, Claude said there was no job description and asked me to paste it, even though `job-description.md` was on main.
- **Root cause:** The session started on an old leftover branch (`claude/laughing-maxwell-nwehfl`) that was missing everything merged since, including rule R6 itself. A written rule can't help if the old copy doesn't contain it.
- **Deeper root cause (found while testing):** GitHub's default branch was still the old setup branch (`claude/focused-noether-hvnz1x`), so every new session started from that first version. I switched the default branch to main on 2026-10-07.
- **Fix:** A startup hook (`.claude/hooks/session-start.sh`) now runs automatically at the start of every cloud session and merges the latest main in before Claude reads anything. If it can't, it shows Claude a warning to pass on. Backup rule: check origin/main before ever saying something is missing.
- **Rule:** R6 · **Test:** T6 · **Level:** 3 (repeat of L6) · **Times it happened:** 4

### L6 · 2026-10-07 · Made me paste the job description again
- **What happened:** I had to paste the Associated Bank job description a third time. Claude said it couldn't find it, even though `job-description.md` was already on main.
- **Root cause:** The session was started from an old draft branch (`claude/focused-noether-hvnz1x`) instead of main, so its copy was missing everything merged since. Claude didn't check whether its copy was up to date. Also, the job description was only mentioned in NOW.md, not loaded automatically. It happened 3 times, so it starts at Level 2.
- **Fix:** `job-description.md` is now loaded automatically by CLAUDE.md in every session. At the start of each session, Claude checks that its copy matches the latest main version. If it doesn't, Claude says so first, before anything else.
- **Rule:** R6 · **Test:** T6 · **Level:** 2 → 3 (see L6b) · **Times it happened:** 3

### L5 · 2026-10-07 · Steered away from what I asked for
- **What happened:** I said I wanted to think through how to do a new job. When I mentioned I was still interviewing, Claude switched to interview prep, and I had to correct it.
- **Root cause:** Claude let a new detail replace my stated goal, instead of checking how that detail fit the goal.
- **Fix:** Keep my stated goal as the anchor. When a new detail could change the direction, ask before switching.
- **Rule:** R5 · **Test:** T5 · **Level:** 1 · **Times it happened:** 1

### L4 · 2026-10-07 · Pop-up without a plain-English explanation
- **What happened:** Claude triggered a GitHub pop-up without first explaining it, and described the problem in technical words. The user clicked Deny because they didn't understand it.
- **Root cause:** Claude was focused on fixing a technical problem and skipped the "Claude explains, I decide" checklist in CLAUDE.md. A rule already existed, so this counts as a failed rule and starts at Level 2.
- **Fix:** Right before every pop-up, give the 3 parts (what it's for, what it can do, which button to click) in everyday words, using an everyday comparison if one helps.
- **Rule:** R4 · **Test:** T4 · **Level:** 2 · **Times it happened:** 1

### L3 · 2026-10-07 · Got too in the weeds
- **What happened:** After being told to shorten things, Claude asked for approval one tiny piece at a time, which slowed everything down.
- **Root cause:** Claude over-corrected and lost sight of the bigger goal, which is to keep moving.
- **Fix:** Keep momentum. Group small things together, ask only about real decisions, and let the full review happen in the pull request.
- **Rule:** R3 · **Test:** T3 · **Level:** 1 · **Times it happened:** 1

### L2 · 2026-10-07 · Showed too much at once
- **What happened:** Claude showed three files in one message. After the correction, it was still too long.
- **Root cause:** Claude trimmed the wording but kept the same amount of content.
- **Fix:** Tiny pieces only, about 5 lines plus one question.
- **Rule:** R2 · **Test:** T2 · **Level:** 2 → 3 (see L2b) · **Times it happened:** 2

### L1 · 2026-10-07 · Explained saving without checking
- **What happened:** Claude said nothing would reach GitHub until the end. In fact, the cloud workspace backs up each saved file right away.
- **Root cause:** Claude described a process from an assumption.
- **Fix:** Check first, or say "I'm not certain."
- **Rule:** R1 · **Test:** T1 · **Level:** 1 · **Times it happened:** 1
