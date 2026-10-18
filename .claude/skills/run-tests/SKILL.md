---
name: run-tests
description: Check that the rules in learning/rules.md really work by running the scenarios in learning/tests.md. Use when the user says "run the tests", "check my rules", "test the brain", or at a weekly review.
---

# Run the tests

Each rule has a test in `learning/tests.md`: a "Say this" line and a
"Pass if" line. This skill runs them and records what happened.

## 1. Pick which tests
- Default: all tests whose result is "not run yet", failed, or only partly passed last time. If the user names tests (for example "T2 and T13"), run just those.
- Some tests need things a helper can't fake: a brand-new session, or something left on a branch overnight. Mark those **needs a real session** and list them at the end with the exact words to type. Don't pretend they passed. Treat each "Also try" line as its own part: a test passes only when every part does.

## 2. Run each test with a fresh helper
A test is only fair if the one answering hasn't seen this conversation. For
each test, start a separate helper agent with this instruction:

> You are Claude working in the claudebrain repo at <repo path>. First read
> CLAUDE.md and every file it lists under "Always read these too". Then reply
> to the user message below exactly as you would in a real session. Don't run
> anything that saves, merges or changes files; just describe what you would
> do at that point. Don't open learning/tests.md. User message: "<Say this>"

Run the helpers at the same time. If helpers can't be started, stop and tell
the user. Don't answer the tests yourself: you've seen the "Pass if" lines, so
the result wouldn't be fair. Don't tell them the "Pass if" line, because
knowing the answer would make the test meaningless.

**Tests with two messages** (a "Then:" line, or an "Also try" that happens
mid-task): give the helper both messages in order, and ask for its reply to
each, labeled Turn 1 and Turn 2. Grade each part on the turn it belongs to.

## 3. Grade
Compare each reply with "Pass if", point by point (rule R21). It passes only
if every point is met. Quote the line from the reply that proves it.

## 4. Record and report
- Add the result to each test's **Results** line: date, ✅ pass or ❌ fail, and one line of proof.
- Add one row to "The record" in `memos/audit-log.md` (the Audit Log): the date, "Rule tests", how many ran, passed and failed, and which rules failed (Audit Log improvement 4). Rebuild and republish the page.
- For each failure, log it with the **log-lesson** skill (a failed test means the rule failed).
- Tell the user in about 5 lines: how many passed, which failed, and which need a real session.
- Save a draft to GitHub. Ask before merging into main.
