# Lessons

The full story of each mistake. Newest at the top.
Each lesson produces one rule (in rules.md) and one test (in tests.md).

If a mistake happens again, its fix moves up a level:
1 = a rule · 2 = a sharper rule, moved to the top · 3 = a required step in a skill

---

### L6 · 2026-10-07 · Made me paste the job description again
- **What happened:** I had to paste the Associated Bank job description a third time. Claude said it couldn't find it, even though `job-description.md` was already on main.
- **Root cause:** The session was started from an old draft branch (`claude/focused-noether-hvnz1x`) instead of main, so its copy was missing everything merged since. Claude didn't check whether its copy was up to date. Also, the job description was only mentioned in NOW.md, not loaded automatically. It happened 3 times, so it starts at Level 2.
- **Fix:** `job-description.md` is now loaded automatically by CLAUDE.md in every session. At the start of each session, Claude checks that its copy matches the latest main version. If it doesn't, Claude says so first, before anything else.
- **Rule:** R6 · **Test:** T6 · **Level:** 2 · **Times it happened:** 3

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
- **Rule:** R2 · **Test:** T2 · **Level:** 2 · **Times it happened:** 2

### L1 · 2026-10-07 · Explained saving without checking
- **What happened:** Claude said nothing would reach GitHub until the end. In fact, the cloud workspace backs up each saved file right away.
- **Root cause:** Claude described a process from an assumption.
- **Fix:** Check first, or say "I'm not certain."
- **Rule:** R1 · **Test:** T1 · **Level:** 1 · **Times it happened:** 1
