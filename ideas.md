# Ideas

Ideas for improving this system or how I work with Claude.
Claude adds ideas as it notices them and suggests 1 to 3 at each wrap-up.
**Status:** new · suggested · yes · no · done

| # | Idea | What it would let me do | Status |
|---|---|---|---|
| 1 | A "run-tests" skill | Check every rule in tests.md with one request | yes (to build next session) |
| 2 | Fewer approval pop-ups | Pre-approve safe "only reads" actions so I see fewer pop-ups | new |
| 3 | Playbooks for my everyday tools | Turn tasks I repeat in email, calendar or documents into step-by-step routines | new |
| 4 | Settle the "save to GitHub" reminder (it nagged 5 times on 2026-10-09) | An automatic check asks Claude to save after every reply, which clashes with "ask before saving". Decide whether small saves to the draft branch can happen without asking | done (2026-10-09): Claude saves drafts without asking and asks before merging. CLAUDE.md, rules and NOW.md updated; the wrap-up skill (step 6) still needs my edit, see idea 16 |
| 5 | Saved prompts for thinking through the new job | Start a new session on any part of the job by pasting a ready-made prompt | yes (done: job-prompts.md) |
| 6 | A "prototype" skill | Say "prototype X" and Claude follows the prototyping process in NOW.md step by step | yes |
| 7 | Job framework view of the tech stack | See every technology sorted by my six steps (Discover → Measure and iterate) in `tech-stack.md`, loaded every session | yes (done) |
| 8 | Tidy up old draft branches on GitHub | Fewer old copies lying around that a session could start from by mistake | yes (done: I deleted the 6 old branches on GitHub, 2026-10-07) |
| 9 | "Done" checklist for big tasks (from the Karpathy-inspired prompt) | Before a big task, Claude writes what "done" means; at the end it shows pass/fail for each item, with proof | yes (done) |
| 10 | Save progress mid-task, not just at wrap-up (from the same prompt) | If a session dies halfway, NOW.md already says what's finished and the one next step | yes (done) |
| 11 | A second-opinion check before I see important work (from the same prompt) | A separate Claude helper reviews job work or prototypes against the checklist before I see them | suggested |
| 12 | Rule: don't retry a failed approach without a new reason (from the same prompt) | Stops Claude going round in circles on the same broken fix | suggested |
| 13 | A "write-prompt" skill | Say "write a prompt for X" and Claude walks me through `prompting.md` piece by piece | yes (to build) |
| 14 | A notes file for the Claude Mastery course | Keep what I learn from each course page in one place, so any session can build on it | yes (start when the first course page comes in) |
| 15 | Save job answers as we go | Keep my answers from each job part in a file, so a new session can pick up where I stopped | yes (done: job-notes.md) |
| 16 | Remove my safety rules (pop-up explanations, "Deny is safe" reminders, asking before saving) | I said these were training wheels while I was new. Claude is blocked from editing its own rules, so I need to edit `CLAUDE.md`, `learning/rules.md` (R4) and the wrap-up skill myself. Wrap-up step 6 should become: "Save a draft automatically; ask \"Merge into main now? (y / review first / n)\"" and step 8 should merge on a yes (from L11) | yes (2026-10-07), waiting on me |
| 17 | Bring in the RM framework memos | Get my 2026-10-08 RM analytics memos (framework, audit, market scan) into main so every session can use them; leave the older rule edits on that branch out | yes (done 2026-10-09) |
| 18 | A "plain words" check in the wrap-up skill (from L10c) | Before the final message, Claude must reread it as a newcomer and explain anything internal. Claude can't add this itself; I'd add it alongside idea 16 | suggested |
| 19 | Make the startup warning list only files that are really missing from main | The warning listed my memos as missing even after they were in main, which was confusing | yes (to build) |
| 20 | A "new use case" skill | Say "new use case: X" and Claude drafts the memo with Example 4, audits it against `product-framework.md`, fixes it and saves it in `memos/` | yes (to build) |
| 21 | An "agent spec" checklist for the job (from the "autonomous team" prompt I was sent) | For every AI agent I design at the bank, write down its mission, inputs, allowed tools, outputs, stop condition and proof it worked. Fits "One job each" in `product-framework.md` | yes (done 2026-10-09: Appendix A of memo v8) |
| 22 | A "designed doc" skill | Say "make a doc for X" and Claude builds it on a design page in my style, checks it on screen, and keeps the .md working copy in step | yes (done 2026-10-09: `designed-doc` skill) |
