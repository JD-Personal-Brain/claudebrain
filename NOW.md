# NOW: start here

_Last updated: 2026-10-09 · Last review: none yet (first one due around 2026-10-14)_

## Where things stand
- The Claude brain is set up: rule book, profile, learning files, ideas list and two skills.
- An official "main" copy now exists on GitHub, and it is now GitHub's default branch, so every new session starts from it. Future work is proposed as pull requests against it.
- A startup check runs at the start of every session and pulls in the latest main automatically, so Claude never works from an old copy. Tested and working.
- New focus: I'm interviewing for a Principal Applied AI Product Manager job at Associated Bank. The focus is thinking through how I'd do the job itself, not interview prep.
- The full job description is saved in `job-description.md`, and a full guide to every technology in it is in `tech-stack.md`. Both load automatically every session. Never ask me to paste it again.
- First prototype made: a calculator (v1, then v2 with green buttons). It was practice and has nothing to do with the job. The prototyping process is under agreements below.

## What's next
1. Think through how I'd do the Associated Bank job: start a new session with the Part 1 prompt in `job-prompts.md`.
2. Use Claude for real work, including prototypes for the new job, and say "wrap up" at the end of each session.
3. Build the "run-tests" skill (idea 1, approved).
4. Do the first weekly review around 2026-10-14.

## Current agreements (and why)
- **Claude explains, I decide.** Why: I'm not a developer and want to stay in control.
- **Tiny pieces to review.** Why: long messages are hard to review.
- **Keep moving and let the system grow naturally.** Why: getting everything perfect up front isn't worth the time.
- **Claude asks only before saving to GitHub or doing something big.** Why: asking about every small action slows us down.
- **A weekly review.** Why: it's often enough to catch problems early.
- **Work is saved to a draft branch on GitHub, and the main version changes only when I merge.** Why: the cloud workspace is temporary, but I keep the final say.
- **main stays GitHub's default branch, and the startup check stays on.** Why: otherwise new sessions start from an old copy and can't find saved files like the job description.
- **Big tasks get a "done" checklist and progress saved partway.** Why: I can see proof each part works, and a session that dies halfway doesn't lose its place. (Ideas taken from a Karpathy-inspired prompt, 2026-10-09.)
- **How we prototype screens (UI).** Why: I'm learning to prototype and expect to need it in my new job, and I want every version kept so any new session can carry on.
  1. Claude builds one HTML file that I can download and open in my browser. Nothing needs installing.
  2. It's saved as `prototypes/<name>/prototype-v1.html`. Each change I ask for becomes a new file (v2, v3, and so on), and old versions are never changed.
  3. Claude tests it against a "done" checklist (pass or fail for each item), sends me the file, and saves it to GitHub after I say yes.
  4. Any new session can continue from the latest version. Current: calculator, v2 (green buttons).
