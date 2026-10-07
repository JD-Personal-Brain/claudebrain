# Lessons

The full story of each mistake. Newest at the top.
Each lesson produces one rule (in rules.md) and one test (in tests.md).

If a mistake happens again, its fix moves up a level:
1 = a rule · 2 = a sharper rule, moved to the top · 3 = a required step in a skill

---

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
