# Lessons

The full story of each mistake. Newest at the top.
Each lesson produces one rule (in rules.md) and one test (in tests.md).

If a mistake happens again, its fix moves up a level:
1 = a rule · 2 = a sharper rule, moved to the top · 3 = a required step in a skill

---

### L11 · 2026-10-09 · Work stranded on a branch that never reached main
- **What happened:** The RM analytics framework (memo v6, audit, market scan) from 2026-10-08 was saved only on a side branch on GitHub. No pull request was ever opened, so it never reached main and later sessions couldn't see it. I found out only by asking, and it worried me that so much work could have been lost.
- **Root cause:** Getting work into main depended on someone remembering to wrap up and merge. Nothing checked for work left behind on other branches.
- **Fix:** The startup check now lists any branch with work that isn't in main, at the start of every session. Wrap-up offers to merge right away.
- **Rule:** R14 · **Test:** T14 · **Level:** 1 (plus an automatic check) · **Times it happened:** 1

### L10 · 2026-10-09 · Used shorthand I didn't understand
- **What happened:** After I merged the prototypes, Claude said "NOW.md still lists 'merge the prototypes pull request' as a next step. The next session can tick it off, so you don't need another save just for that." I replied "I don't understand."
- **Root cause:** Claude wrote in its own shorthand: it named an internal file and a to-do item, and said "save" without saying what that would mean for me. It assumed I knew what it was thinking.
- **Fix:** Before sending a message, read it as me: say what happened, what it means for me and whether I need to do anything. Name a file only with a few words on what it is.
- **Rule:** R13 · **Test:** T13 · **Level:** 1 · **Times it happened:** 1

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
