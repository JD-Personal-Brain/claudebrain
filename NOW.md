# NOW: start here

_Last updated: 2026-10-07 · Last review: none yet (first one due around 2026-10-14)_

## Where things stand
- The Claude brain is set up: rule book, profile, learning files, ideas list and two skills.
- The first pull request (the setup) is waiting for me to review and merge.
- An official "main" copy now exists on GitHub. Future work is proposed as pull requests against it.
- First prototype made: a calculator (v1, then v2 with green buttons). The prototyping process is under agreements below.

## What's next
1. Review and merge the setup pull request.
2. Review and merge the prototypes pull request.
3. Use Claude for real work, including prototypes for the new job, and say "wrap up" at the end of each session.
4. Do the first weekly review around 2026-10-14.

## Current agreements (and why)
- **Claude explains, I decide.** Why: I'm not a developer and want to stay in control.
- **Tiny pieces to review.** Why: long messages are hard to review.
- **Keep moving and let the system grow naturally.** Why: getting everything perfect up front isn't worth the time.
- **Claude asks only before saving to GitHub or doing something big.** Why: asking about every small action slows us down.
- **A weekly review.** Why: it's often enough to catch problems early.
- **Work is saved to a draft branch on GitHub, and the main version changes only when I merge.** Why: the cloud workspace is temporary, but I keep the final say.
- **How we prototype screens (UI).** Why: I'm learning to prototype and expect to need it in my new job, and I want every version kept so any new session can carry on.
  1. Claude builds one HTML file that I can download and open in my browser. Nothing needs installing.
  2. It's saved as `prototypes/<name>/prototype-v1.html`. Each change I ask for becomes a new file (v2, v3, and so on), and old versions are never changed.
  3. Claude tests it, sends me the file, and saves it to GitHub after I say yes.
  4. Any new session can continue from the latest version. Current: calculator, v2 (green buttons).
