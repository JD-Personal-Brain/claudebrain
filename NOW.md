# NOW: start here

_Last updated: 2026-10-09 · Last review: none yet (first one due around 2026-10-14)_

## Where things stand
- The Claude brain is set up: rule book, profile, learning files, ideas list and three skills (log-lesson, wrap-up, designed-doc).
- An official "main" copy now exists on GitHub, and it is now GitHub's default branch, so every new session starts from it. Future work is proposed as pull requests against it.
- A startup check runs at the start of every session and pulls in the latest main automatically, so Claude never works from an old copy. Tested and working.
- The startup check now also warns about work saved on a side branch that never reached main (added 2026-10-09, after my RM framework was found stranded).
- My RM analytics framework is now in main (brought in 2026-10-09): `memos/rm-analytics-framework.md` (now memo v8, 2026-10-09: a working project plan that builds from day one, with first features live in about weeks 2–6, a backup date, outside sources checked, and every agent and workflow specified in two appendices), plus a 1-page summary (`memos/rm-analytics-summary.md`), the audit and the market scan. The designed versions people will read are on the RM Analytics Framework design page (https://claude.ai/artifact/3c7ZxKjJcjWRyV7BbzKfhY): the one-page summary and the full plan in six parts, side by side. The full plan is also one continuous scrolling page: https://claude.ai/artifact/KxPNQLCj6HASThmQpYtfhk (made from the design page; update the design page first, then rebuild this). The .md files are only working copies. Both are waiting for my review before I share them with Associated. The sources were checked through web search only, because the pages themselves were blocked in this session, so open the McKinsey link in a browser before sharing. The old branch it was stranded on is deleted, so nothing is left outside main.
- Working assumption: every tool in the job description is live at the bank (I was told so). It's noted in `tech-stack.md`.
- My product framework (six steps, each with a go/no-go gate) is saved in `product-framework.md` and loads every session. It was taken from the RM memo.
- Test T12 passed: a fresh session built a prompt from `prompting.md` without reminders.
- New focus: I'm interviewing for a Principal Applied AI Product Manager job at Associated Bank. The focus is thinking through how I'd do the job itself, not interview prep.
- The full job description is saved in `job-description.md`, and a full guide to every technology in it is in `tech-stack.md`. Both load automatically every session. Never ask me to paste it again.
- Job Part 1 (finding problems) has started. My answers so far are in `job-notes.md`; pick up at step 1's open question.
- A prompting cheat sheet is saved in `prompting.md`, built from Anthropic's official guide, and loads every session. Claude follows it whenever it writes a prompt. Example 4 is a reusable prompt that drafts a full product memo for a new use case.
- I can now work in the Claude desktop app: choose **Cloud** and the claudebrain repo each time. Cloud sessions can't see my Chrome, and the course site (notion.site) is blocked here, so course pages come in by copy-paste or screenshots.
- **Memo v8 merged into main on 2026-10-09** (pull request #35). Reviewed so far: the summary's opening and plan table.
- **Six-step workflow visual** for the role (2026-10-09): https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv. Working copy: `memos/role-workflow.md`.
- First prototype made: a calculator (v1, then v2 with green buttons). It was practice and has nothing to do with the job. The prototyping process is under agreements below.

## What's next
1. Read the rest of the design page (summary from "What lets us move this fast" on, then Parts 1–6), and open the McKinsey link in a browser before sharing.
2. Work through the Claude Mastery course: paste in the first page and pick what to add to the brain.
3. Continue the Associated Bank job, Part 1, with the prompt in `job-prompts.md`. Pick up where `job-notes.md` stops.
4. Use Claude for real work, including prototypes for the new job, and say "wrap up" at the end of each session.
5. Build the "run-tests" skill (idea 1, approved).
6. Remove my safety rules and update the wrap-up skill myself in GitHub (idea 16): Claude is blocked from changing those.
7. Do the first weekly review around 2026-10-14.

## Current agreements (and why)
- **Claude explains, I decide.** Why: I'm not a developer and want to stay in control.
- **Tiny pieces to review.** Why: long messages are hard to review.
- **Keep moving and let the system grow naturally.** Why: getting everything perfect up front isn't worth the time.
- **Claude saves drafts to GitHub without asking, and asks before merging into main or doing something big.** Why: drafts protect my work, and I want to understand exactly what's merged (decided 2026-10-09).
- **A weekly review.** Why: it's often enough to catch problems early.
- **Work is saved to a draft branch on GitHub, and main changes only when I say yes to a merge.** Why: the cloud workspace is temporary, but I keep the final say. Work isn't safe for future sessions until it's in main (rule R14).
- **main stays GitHub's default branch, and the startup check stays on.** Why: otherwise new sessions start from an old copy and can't find saved files like the job description.
- **Big tasks get a "done" checklist and progress saved partway.** Why: I can see proof each part works, and a session that dies halfway doesn't lose its place. (Ideas taken from a Karpathy-inspired prompt, 2026-10-09.)
- **Product work follows `product-framework.md`.** Why: every project gets organized the same way, from Discover to Measure and iterate.
- **Prompts follow `prompting.md`.** Why: so every prompt we write uses a framework that works, based on Anthropic's own advice.
- **Documents for other people are designed pages, not .md files** (rule R16). Why: they must look like something a person wants to read; the .md is only the working copy.
- **Course pages come in by copy-paste or screenshots.** Why: Cloud sessions can't reach my browser or the course site.
- **How we prototype screens (UI).** Why: I'm learning to prototype and expect to need it in my new job, and I want every version kept so any new session can carry on.
  1. Claude builds one HTML file that I can download and open in my browser. Nothing needs installing.
  2. It's saved as `prototypes/<name>/prototype-v1.html`. Each change I ask for becomes a new file (v2, v3, and so on), and old versions are never changed.
  3. Claude tests it against a "done" checklist (pass or fail for each item), sends me the file and saves a draft to GitHub, then merges it into main after I say yes.
  4. Any new session can continue from the latest version. Current: calculator, v2 (green buttons).
