# NOW: start here

_Last updated: 2026-10-18 · Last review: none yet (first one due around 2026-10-21; I said not yet on 2026-10-14) · Wrap-ups since the last Elon mode review: 1 (last run 2026-10-18, evening, on everything; it runs at 3)_

_Kept short on purpose (Elon mode, 2026-10-18): this note says where things stand and points to the one home of everything else. Open work lives in the Open Items log; how Claude works lives in `CLAUDE.md` and `learning/rules.md`; history lives in git, the log's closed items and `learning/lessons.md`._

## Where things stand
- **The job:** Principal Applied AI Product Manager at Associated Bank (`job-description.md`, `tech-stack.md`; every tool in it is assumed live). The focus is how I'd do the job, not interview prep. I talk with the RM lead and the credit lead on Tuesday October 20, 2026.
- **The front door:** the Document Library (https://claude.ai/artifact/LTpbCT4kN4LcyEoYnh7vgj, pinned; say /documents), seven sections (regrouped 2026-10-18, C54). My workspace is shown to others too: I'm happy for them to see how I work (C58). Every page is built from a working file by script (`designs/README.md`).
- **How we deliver (read and in use):** Product Workflow, Product Framework, Product Machine and Product Playbook, with the Agent Library (38 agents), Steps Catalog, Controls Catalog (25 controls), Workflow Maps and Glossary. Never yet run, even on a made-up product (the dry run, W8).
- **RM work (in main):** three short pages for people (the RM Executive Summary https://claude.ai/artifact/LPPq2gt5PSoiB8GzX8ZBE2, RM Assistant https://claude.ai/artifact/RBaZS636CtycDwZyDrgum2 and the RM Assistant Plan https://claude.ai/artifact/KxPNQLCj6HASThmQpYtfhk) and RM Detail for AI to read (https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n). Reviewed and good (2026-10-19, C59). The RM Assistant is a working hypothesis until Discover.
- **RM prototype (in main):** the RM Assistant Prototype, version 4 (https://claude.ai/artifact/RFM2o7cdren3TxesQBsjky; code in `prototypes/rm-assistant/`): Today, the wave 1 screens with agents A1 to A3 live on Claude, a wave 2 preview (early warning, refer to treasury), the controls working, a spoken tour and the tour as a video (`rm-assistant-tour-v4.mp4`). Reviewed and good (2026-10-19, C60).
- **Use cases:** the Use Case Library (https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X, in use). **Portfolio managers (credit):** untouched until I say we're moving into PM; the credit order is agreed (credit memo and annual review drafts first, early warning second).
- **The bank:** the Bank Business Briefing (https://claude.ai/artifact/7ZVT7LtdqxwAma4UrBgTPX), updated by the bank news scout every Monday (first run October 19) and after the Q3 results (October 23), by email notice to my personal address.
- **Quality:** every change is audited before main (the audit skill, the GitHub audit check, the Audit Log https://claude.ai/artifact/QnPL82PBx6AfGKB5VgqUPf). The mechanical part of each wrap-up runs by script (`.claude/skills/wrap-up/run.py`).
- **Working with Claude:** the Prompting Guide and the Prompt Library (four core prompts); the Claude Mastery course comes in by paste (next up: Module 3, Projects, Connectors and Skills).

## What's next
_Everything open, in priority order, is in the Open Items log (https://claude.ai/artifact/NsW5AH5XFNHmDNYJvmVDMb). Before Tuesday October 20 I'm going down it from the top, one item at a time. The top three:_
1. **Monday October 19 (me):** check that the bank news scout's first weekly notice arrived at my personal email (item W1 in the Open Items log); it comes from the scheduled task itself, so nothing needs setting up first.
2. **Before Tuesday (me):** open the RM Assistant Prototype inside claude.ai, press "Run live on Claude" on the Monday list once to confirm the live AI works, the one check that real Claude hasn't been through yet (the prototype itself is reviewed, C60).
3. **For Tuesday (me):** ask first how long the bank's AI review takes and whether client meetings may be recorded; the RM timeline rests on both (the RM plan's open questions).

## Current agreements (and why)
_Agreements already written as rules or in `CLAUDE.md` are listed there, not repeated here: Claude explains and I decide (`CLAUDE.md` §1); drafts saved without asking, merges only on my yes and only after every check passes (rules R14 and R18); every change audited (R18); short messages (R2); designed pages, never Markdown, for anything a person reads (R16); one source for every page (C42); never state bank facts as fact (R32); my personal email only, never sent to outside services (R35)._
- **Cut first, then automate** (Elon mode, 2026-10-15): at every gate, ask whether each task should exist, can be deleted, simplified or made faster before automating it; law and bank policy are never cut. Why: automating work that shouldn't exist locks in the waste.
- **The overlapping first pass** (C55, 2026-10-18): gate 1 can pass early on a first sizing and a provisional baseline; the rest of Discover and the final baseline finish by gate 2. Why: the pace is set by what really blocks us.
- **Base first, then RM, then PM** (2026-10-15; RM open since 2026-10-17): PM pages stay untouched until I say we're moving into PM. Why: the RM and PM plans copy the base, so it must be solid first.
- **Short pages for people, one full document for AI** (C50): each user group gets three short pages, and every detail goes into one detail document (RM Detail is the fifth row of the RM section, after the prototype). Why: people need simple, actionable pages; an AI can take everything at once.
- **Projects run on the product machine**, every task marked Auto, Draft, Me or Partner. Why: I'm one person running many projects, so routine work must run itself.
- **The product manager owns each product until a long-term owner is named.** Why: who holds a product long term is a decision the process must make.
- **Keep moving, tiny pieces to review, and let the system grow naturally.** Why: long messages are hard to review, and perfect up front isn't worth the time.
- **A weekly review**, about 5 minutes. Why: often enough to catch problems early.
- **main stays GitHub's default branch, and the startup check stays on.** Why: otherwise new sessions start from an old copy.
- **One log for open items, scrubbed in full once a day** (2026-10-09; once a day since 2026-10-18). Why: open items go out of date quickly, and a full scrub at every quick wrap-up found nothing.
- **The Document Library is the front door,** and the checker fails if a page is missing from it. Why: I want to find any document at any moment.
- **The credit user group is called portfolio managers.** Why: it's the bank's own title, used in its job postings.
- **Course pages come in by copy-paste or screenshots.** Why: Cloud sessions can't reach my browser or the course site.
- **Every wrap-up puts forward two open ideas from the backlog** (idea 50). Why: so the ideas list gets decided instead of piling up.
- **Sharing with Associated:** not yet (2026-10-09). Every page can be shared as it is, with no separate edition (2026-10-15); when I'm ready, Claude lists which pages to share one by one, since sharing the library doesn't share the pages it links to.
- **How we prototype screens (UI).** Why: I'm learning to prototype and want every version kept.
  1. Claude builds one HTML file I can open in my browser, saved as `prototypes/<name>/prototype-v<N>.html`; each change is a new version, and old versions are never changed.
  2. Claude tests it against a "done" checklist, sends me the file, saves a draft and merges it after my yes.
  3. Current: calculator, v2 (practice only); RM Assistant Prototype, v4 (`prototypes/rm-assistant/`, built from source by its `build.py`).
