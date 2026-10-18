# Audit Log

How we audit our work: what we believe about audit, every check and when it
runs, the record of every audit so far, and what to improve. Approved 2026-10-15, with all six improvements; every audit adds a row to
the record below.

## How we think about audit

Seven principles, drawn from what we already do and the lessons behind it.

1. **Nothing reaches main unaudited.** Main is what every new session starts from, so it must always be clean (rule R18).
2. **Check everything, not just what changed.** A stale line in a file nobody touched is still drift, so the scripts check every file and page every time, and standard and deep audits sweep every core document (lesson L18).
3. **Machines check the mechanical, people-style reviewers check the meaning.** Counts, names, links, wording and rendering are checked by scripts; logic, gaps and plain English by independent reviewers.
4. **Fresh eyes, twice.** In standard and deep audits, a reviewer who didn't do the work finds the problems; a second fresh reviewer confirms the fixes and looks for problems the fixes caused. Quick audits (small fixes) use the scripts only.
5. **Evidence, not claims.** "Clean" means the checker's output, the render check's output, screenshots and the reviewers' pass list (rule R7).
6. **Every miss becomes a check.** A mistake is logged as a lesson, becomes a rule with a test, and, if it happens again, a required step or an automatic check (the log-lesson levels 1 to 3).
7. **The work stays with Claude, the decisions with me.** Claude runs every check without asking; only decisions (a new rule, a merge into main) come to me, and I'm never asked to proofread reference pages (rule R22, and the co-collaborator rule in CLAUDE.md).

## Every check, and when it runs

| When | Check | What it catches | How it runs |
|---|---|---|---|
| Start of every session | Startup check | Working from an old copy of main; work stranded on a branch that never reached main | Automatic (session-start hook) |
| Start of every session | Bank news scout check (R28) | A scheduled scout run that failed, stalled or is overdue | Claude, every session |
| While building | Look at it as I will (R7) | Edits that landed in the wrong place; pages that render badly | Claude, after every change |
| While building | Live page newer than its file (idea 38) | Overwriting another session's published edits | Inside every publish |
| While building | Glossary check before naming (R23) and "check before you claim" (R21) | New names that clash with a defined term; claims a file doesn't support | Claude |
| Every audit | The audit checker (every check listed in `check.py`) | Machine tables against the playbook; missing fields; empty tables; stale built pages; library and README out of step; Open Items numbers and counts; shorthand in What's next; counts of agents, sub-steps and controls; gate, question and governance wording; banned and retired words; RM and PM spelling; old page names; broken section links; stray marks; requirement sources; agent names | Automatic script |
| Every audit | Render check | Empty tables, cut-off canvas parts, sideways scrolling, stray Markdown, jump links that land in the wrong place (about 330 clicks) | Automatic script |
| Every audit | Nothing-lost check (R29) | Sentences that disappeared from the working files | Automatic script; each line explained |
| Standard and deep audits | Alignment sweep | Any core document that disagrees with the reference pages (agents, workflows, steps, controls, glossary) | Independent reviewers |
| Standard and deep audits | First review | Consistency, cross-references, coverage, facts, logic, drift, plain English, open items | A fresh reviewer |
| Standard and deep audits | Second review | Fixes that didn't land, and new problems the fixes caused | A second fresh reviewer |
| Every wrap-up | Audit first (wrap-up step 0) | Everything above, plus a scrub of every open item | Claude |
| Every pull request | GitHub audit check | Any checker problem; the pull request shows a red mark and can't be merged (a required check since 2026-10-15, closed item C38) | Automatic, on GitHub |
| Merging into main | Pre-merge check (idea 36) | Any checker or render problem; it blocks the merge | Automatic, when Claude merges |
| Every third wrap-up (every fifth until 2026-10-18) | Elon mode review | Work that should be cut or simplified before it's automated, in the product machine and in this system itself (rules, skills, checks, pages, open items) | Claude (elon-mode skill) |
| About weekly | Rule tests (run-tests) and the weekly review | Rules that no longer work; what's annoying | Claude and me |
| After any mistake | Lesson, rule and test (log-lesson) | The same mistake happening twice; a repeat raises the fix a level | Claude |

**Severity:** **Must fix** (wrong, contradicts another page, or would stall real work), **Should fix** (unclear, incomplete or inconsistent), **Minor** (wording, dates, polish). All three are fixed before merging, unless a fix would change a decision I made; that goes to me.

## The record

Every audit so far, newest first. Earlier entries are rebuilt from NOW.md and the
saved history, so their counts are approximate.

| Date | What was audited | Size and how | Findings (and lost lines by reason) | Result |
|---|---|---|---|---|
| 2026-10-18 | Elon mode changes (all six findings applied at my request): the RM plan and Executive Summary tightened (limiting factor first, timing and the backup plan said once, asks and questions merged); NOW.md's "Where things stand" cut from about 6,400 words of history to the current state; rules merged from 32 to 21; Elon mode every third wrap-up, also reviewing this system | Quick: checker, render check, nothing-lost; the Elon mode reviews counted as the review | 0 findings; lost lines: NOW.md's dated history (cut on purpose: it lives in git, the Open Items log's closed items and the lessons), the old rule wordings (merged, with the mapping noted in the rules and tests), and the plan's repeated timing table, backup lines and confirm list (cut on purpose; RM Detail keeps them in full) | Waiting for my yes to merge |
| 2026-10-18 | Wrap-up (later): NOW.md; the Open Items log rechecked | Quick: checker, render check, nothing-lost | 0 findings; lost lines: 0 | Waiting for my yes to merge |
| 2026-10-18 | Detail links from the RM Assistant Plan into RM Detail: a link on every Gantt row and at the end of each plan section; RM Detail's headings now have link targets | Quick: checker (with a test that a broken detail link fails it), render check, nothing-lost; sample screenshot approved | 0 findings; lost lines: 0 | Merged into main |
| 2026-10-18 | Wrap-up: lesson L38 and rule R34, test T49, profile, NOW.md, idea 61 (added to the Open Items log as D2); the Open Items log scrubbed | Quick: checker, render check, nothing-lost | 1 checker problem fixed before saving (idea 61 missing from the log); lost lines: 2, both reworded (the profile's library rows line, NOW.md's library rows item) | Waiting for my yes to merge |
| 2026-10-18 | The Gantt chart at the top of the RM Assistant Plan (a new chart block in the page kit, its styles only on pages that use it) and the portfolio manager section removed from the RM Assistant page | Quick: checker, render check, nothing-lost; screenshot checked before publishing | 0 findings; lost lines: the RM Assistant page's "Portfolio managers next" lines, cut on purpose at my request (the full text stays in RM Detail) | Merged into main |
| 2026-10-18 | The RM reorganization (C50, C51): three short pages for people (RM Executive Summary, RM Assistant, RM Assistant Plan), RM Detail for AI to read (built by `rm-ai-build.py`), the Use Case Library in Reference, page 2 renamed RM Assistant; with the knock-on edits to the library, checker, skills, playbook, Product Framework, glossary, Prompt Library, NOW.md and Open Items log | Deep: checker, render check, nothing-lost, a consistency and facts reviewer and an alignment-sweep reviewer, fixes, then a second reviewer | About 37 findings (5 Must fix, 20 Should fix, 12 Minor), all fixed except two left on purpose: the retired page names RM Core Use Cases and Portfolio Manager Core Use Cases aren't added to the retired-wording table (they would flag dated history lines), and the credit scan's own page is untouched (PM scope, R31). Main ones: a PM time claim backed by an RM statistic, an overstated "no US bank" line, and stale references to the old plan page and its appendices. Lost lines: 85, all reworded for the reorganization (old page names and descriptions) or cut on purpose (the RM user workflow and mock-up placeholder rows, C50) | Fixed; merged into main |
| 2026-10-17 | Wrap-up: ideas 57 and 60 built (the length-warning hook, checker check 17), idea 59 parked; Open Items, ideas, rules, tests and NOW.md | Quick: checker (with a test that a renamed capability fails check 17), render check, nothing-lost, hook tested on long, short and repeat replies | 0 findings; lost lines: the three idea rows' old statuses and the two decision items and the old P5 (moved to C48, C49 and the new P5) | Waiting for my yes to merge |
| 2026-10-17 | The RM Assistant page and the RM plan rebuilt around it (memo v10, all five Elon mode findings applied), with the knock-on edits to the playbook, Product Machine, glossary, Agent Library, Workflow Maps, Bank Business Briefing, RM Core Use Cases page and Open Items log; plus the wrap-up (lessons L36 and L37, ideas 59 and 60) | Deep: checker, render check, nothing-lost, three reviewers in parallel (fresh review, alignment sweep across every core document, a walk-through of wave 1 from kickoff to gate 5), fixes, a second reviewer, fixes, scripts again | About 4 Must fix, 25 Should fix and 20 Minor (overlapping between reviewers). Main ones: the meeting follow-up went live before its own gate 3, step 4 evidence and readiness, and needed a second step 4 pass for saving call notes (now written in); gate 2 didn't produce the wave 2 and 3 dates it was meant to set (now proposed at gate 2, confirmed at each wave's quick pass); a playbook row still pointed to the removed help agent; the Open Items log and NOW.md still listed the Elon mode review as to do. Lost lines: about 190, all moved (to The RM Assistant page, the RM Core Use Cases page or by link to the Product Framework), reworded, or cut on purpose (agent A6, week dates for waves 2 and 3, freed-up time counted as revenue) | All fixed; scripts 0 problems; merged into main after my yes |
| 2026-10-17 | Wrap-up after the kit check: NOW.md and this row; the Open Items log rechecked | Quick: checker, nothing-lost | 0 findings; lost lines: 0 | Waiting for my yes to merge |
| 2026-10-17 | The use case kit check (idea 58, closed item C45): checker check 4b and two "to build" rows in the RM section of the library | Quick: checker (with a test that removing a kit piece fails it), render check, nothing-lost | 0 findings; lost lines: the open question about the check (now C45) | Merged; pull request #108 |
| 2026-10-17 | Deep audit of the Open Items log (asked for at wrap-up): every open item checked against the repo, NOW.md and closed decisions | Deep for the log: checker, one reviewer for the whole log, fixes, a second reviewer | 3 Must fix, 7 Should fix, 6 Minor: the agreed use case kit order (C44) had no item, so the old Andy edition item merged into a new W3 in Now; the library rows item had no entry (now W21); W2 reworded to RMs only; counts fixed (12 control gaps, 21 bank terms); two pointers to closed items fixed; stage 2 to 4 items renumbered and every reference updated. Second review: pass | Fixed; merged after my yes |
| 2026-10-17 | Wrap-up: the retired design page deleted, NOW.md, profile, idea 58; the Open Items log scrubbed | Quick: checker, render check, nothing-lost | 0 findings; lost lines: the earlier rows' rewordings only | Merged after my yes |
| 2026-10-17 | Use case kit stage 2, step 1: the RM plan made the one source (the RM Analytics Plan page, now the RM Assistant Plan, built from its working file), brought up to date (decisions C30 to C32 and C41, the How we deliver rules), plan sections 8 and 10 cut (C40), the design canvas retired (C42), A6 renamed How-to helper; the Open Items log scrubbed | Standard: checker, render check (21 pages, 344 link clicks), nothing-lost, one fresh reviewer, fixes, a second reviewer | 0 Must fix, 7 Should fix, 11 Minor; second review: all fixes pass, 4 Minor leftovers, fixed. Main ones: the reader page called itself a working file; eight open items pointed to the plan's old section 11; gate 1 contradicted the quick pass; the plan's who-decides table left out the user leaders' scale decision. Lost lines: rewordings from the updates, plus sections 8 and 10 cut on purpose (C40; the role map lives in the Product Framework) | Fixed; draft saved, waiting for my yes to merge |
| 2026-10-17 | The new Prompt Library (Prompt 1, the use case kit; Examples 4 and 5 moved in as Prompts 2 and 3, every pointer repointed), the move into RM work (agreement, R31, profile, test T41), the Open Items log scrubbed | Standard: checker, render check (21 pages, 1 canvas, 350 link clicks), nothing-lost, one fresh reviewer, fixes, a second reviewer | 0 Must fix, 8 Should fix, 9 Minor, 1 Optional (taken); second review: all fixes pass, 3 Minor wording points, fixed. Main ones: Prompt 1's stage 1 said "change nothing" yet makes a review page; its source rule let unsourced facts in; the checker didn't cover the new page. Lost lines: 15, all reworded on purpose (pointers to the moved prompts, the RM scope change); the 88 moved prompt lines all found in `prompt-library.md` | Fixed; merged after my yes |
| 2026-10-15 | Wrap-up: idea 57 set to not yet (parked as P5), NOW.md, the Open Items log scrubbed | Quick: checker, nothing-lost | 0 findings; lost lines: the old open-item text for idea 57 (moved to P5) | Merged after my yes |
| 2026-10-15 | Wrap-up: lesson L34, rule R31 at Level 2, profile and NOW.md; the Open Items log scrubbed | Quick: checker, nothing-lost (no designed page changed apart from this log) | 0 findings; lost lines: 0 | Merged after my yes |
| 2026-10-15 | The six gaps from the 2026-10-15 audit of How we deliver, written in (closed item C39): unit of work, quick pass, material change, control K3's credit boundary, products built on documents, workflow maps into Discover | Deep by step 0's rule (new rules and a restated control): checker, render check, nothing-lost, a reviewer with a walk-through (credit memo drafts from financial statements as a feature wave), fixes, a second reviewer | First review: 3 Must fix, 9 Should fix, 4 Minor; second review: 1 Must fix, 6 Should fix, 4 Minor (the rollout group step 4 approves, credit-memo terms, the credit policy owner at 2.4, K13 in the sources table and others); lost lines: 15, all reworded by these rules or the closed decision | All fixed; the RM plan's old change rule updated in its memo and pages; merged after my yes |
| 2026-10-15 | Wrap-up: lesson L33 (task reports too long), rule R2 widened, idea 57, NOW.md; the fifth-wrap-up Elon mode review of the machine (five proposals, none applied) | Quick: checker, nothing-lost | 2 checker problems fixed before saving (a stale item number, an idea missing from the Open Items log); lost lines: 0 | Merged; pull request #103 |
| 2026-10-15 | Required check switched on: closed item C38, idea 56 done | Quick: checker, render check, nothing-lost | 0 findings; the test pull request #100 now reads blocked; lost lines: 6, all from the closed required-check item (moved to C38) | Merged |
| 2026-10-15 | After the move to JD-Personal-Brain: pull request #98 (the steps for the required check), the required-check test, old account name | Quick: checker, render check, nothing-lost | 0 findings; no file still names the old account; the required-check test showed GitHub does not yet block a red pull request (it was switched on later the same day: C38); lost lines: 3, all reworded (the required-check item went from "suggested" to "yes") | Merged |
| 2026-10-15 | Wrap-up: the settings-file repair and lesson L32 | Quick: checker, render check, nothing-lost | 1 Must fix (the settings file couldn't be read, found by reading it back); lost lines: a few, all reworded | Fixed in pull request #96; check 16 added so it can't recur |
| 2026-10-15 | The Audit Log itself and its six improvements | Deep by step 0's rule (a rename across pages and new audit rules), run as scripts plus one reviewer, because a deep audit of the same pages had run hours before | 1 Must fix, 6 Should fix, 7 Minor; lost lines: 10, all reworded or renamed | All fixed; merged |
| 2026-10-15 | How we deliver and the reference pages, top to bottom (details below) | 7 reviewers, a made-up product walked through all 44 sub-steps, 4 editors, a second reviewer | About 110 (8 Must fix), plus about 25 from the second review | All fixed; 12 pages republished; 6 gaps to decide (all approved and written in the same day: closed item C39); pull request #94 |
| 2026-10-15 | Requirement sources check (idea 52) and the Elon mode changes | Checker, reviewer, second reviewer | A handful (approximately) | Fixed; merged |
| 2026-10-15 | Product Workflow links to the Steps Catalog and Workflow Maps | 5 reviewers | Not counted | Passed; pull request #87 |
| 2026-10-14 | The How we deliver reorganization and the Document Library | Two full audits | Not counted | Fixed; merged |
| 2026-10-10 | Deep audit before merging: every core document | 5 reviewers, second reviewer | About 60 | Fixed; rule R23 and the retired-wording check added |
| 2026-10-10 | Alignment audit against the four reference pages | Reviewers per reference page | About 44 | Fixed; the alignment sweep became a standard audit step |
| 2026-10-09 | The Product Playbook, all six steps | Reviewer, second reviewer | 20, then 8 follow-ups | Fixed; the audit became step 0 of every wrap-up |

## Gaps found (2026-10-15)

What this review of our own audit found, and what closed each one:

1. **A merge done on GitHub skips the pre-merge check.** The check runs only when Claude merges; a merge clicked on GitHub (as on 2026-10-15) isn't checked. → Improvement 1, built; since 2026-10-15 the check is required, so a pull request with a red mark can't be merged on GitHub at all (tested blocked, closed item C38).
2. **Audits leave no record.** Results live in chat and commit messages, so there's no trend of findings over time. This log starts that record. → Improvement 2, built.
3. **Every audit is the same size.** A one-line fix and a full reorganization both get the full treatment, which costs time on small changes. → Improvement 3, built.
4. **Rule tests rarely run.** Item W16 lists more than 25 tests not yet run in a live session. → Improvement 4, built.
5. **Audits wait on approval pop-ups.** Page checks and publishes stopped the 2026-10-15 audit for about 30 minutes (lesson L30). → Improvement 5, done.
6. **The nothing-lost list is long and read by eye.** About 130 lines on 2026-10-15, explained in one sentence rather than line by line. → Improvement 6, built.

## Improvements (all six approved 2026-10-15)

| # | Improvement | Where it runs | Status |
|---|---|---|---|
| 1 | **A GitHub check on every pull request** runs the audit checker and shows a red mark if anything fails; since 2026-10-15 it is a required check, so GitHub won't merge a pull request with a red mark (closed item C38) | `.github/workflows/audit-check.yml` (the render check still runs only when Claude merges, because it needs a browser) | Built; required since 2026-10-15 |
| 2 | **This Audit Log is the record**: every audit adds a row (date, scope, size, findings by severity, lost lines by reason, result) | A required step (6) of the audit skill | Built |
| 3 | **Three audit sizes**: quick (the three scripts) for small fixes, standard (scripts plus a reviewer and a second) for normal sessions, deep (plus one reviewer per reference page and a walk-through) for reorganizations and milestones | Step 0 of the audit skill: Claude picks the size and says why | Built |
| 4 | **Rule tests at every weekly review**, with results recorded here | The wrap-up skill (weekly review) and the run-tests skill | Built |
| 5 | **The page pop-up fix**: one permission rule, so page checks and publishes never wait on me | The page rule in `.claude/settings.json`, added by me (closed C37) | Done |
| 6 | **Lost lines grouped by reason** in each audit row | The nothing-lost script now ends with a count per file; the audit row groups them as reworded, moved or cut on purpose | Built |

## Entry: 2026-10-15, How we deliver and the reference pages


**Scope:** the four "How we deliver" pages (Product Workflow, Product Framework, Product Machine, Product Playbook), the Reference pages built from them (Agent Library, Controls Catalog, Steps Catalog, Workflow Maps, Glossary, Tech Stack Guide) and how they line up with the Elon Mode page. Relationship manager (RM) and portfolio manager (PM) work was left out on purpose: it's what we build next.

**How:** seven independent reviewers, each attacking one part (the Workflow and Framework, the Product Machine, playbook steps 1 to 3, steps 4 to 6, agents and controls, language and the reference pages), plus one that ran a made-up product ("a Teams assistant that answers bankers' questions about the bank's products") through all 44 sub-steps to find where the machine would stall. Four editors fixed what they found, and a fresh reviewer checked every fix.

**The verdict**

- **The structure is sound.** All 44 sub-steps have every field, every agent name and kind matches across files, every gate's wording matches the Product Workflow, and the built pages were all up to date.
- **The pages disagreed on details that matter in real use:** who decides at each gate, what "proof" means at the Build gate, and whether a sponsor could waive the zero-tolerance permissions test. These are fixed.
- **Several things the pages promised had no task behind them**, such as the incident dry run (proof of a legally required control) and the guardrail test in step 4. These are fixed.
- **Six gaps needed my decision** (all approved and written in on 2026-10-15, closed item C39) before the RM and PM work. They are rules we never wrote, not mistakes, so Claude didn't invent them. They're listed below with Claude's recommendation.

### What was found and fixed

About 110 findings: 8 Must fix, about 55 Should fix, the rest Minor. All are fixed except those that need your decision (next section).

| Page | What mattered most | Fixed |
|---|---|---|
| Product Workflow | Gate 3 said "every control has proof", but most controls are proved in step 4, so the gate could never pass. Now: "every control is built and passes its control test". Gate 5 said "results hit targets", but revenue takes months. Now: "leading results". | Yes |
| Product Framework | The "who decides" table didn't match the gates. It now names who joins the sponsor at each gate, adds Finance, IT, vendor risk and analytics, and says risk's step 4 approval can't be overruled. It now carries the Elon mode rules (cut first, gates in writing, limiting factor, machine measures) and says what can never be waived. | Yes |
| Product Machine | Missing tasks: incident dry run, compliance agreeing the fairness test, showing the controls to risk, acting on an alert, the incident log, the quarterly summary, recording the machine's measures. Two "Auto" rows hid a person's decision. Claims about where my time goes didn't match the tables. The page now reads every section from the working file, so it can't drift. | Yes |
| Product Playbook, steps 1 to 3 | The sponsor could accept a gap on permissions; the data contract never marked fields as sensitive, but Build masks "sensitive" fields; the baseline could be recorded before the measure was final; vendor reviews started only in step 4 (now in 2.2, because they're slow). | Yes |
| Product Playbook, steps 4 to 6 | Guardrails were never shown working; the monitoring plan came after the sign-offs that depend on it (now drafted alongside 4.5 and in the evidence pack); the step 4 no-go skipped re-testing; the monthly decision required a meeting (now in writing); "stop" had no steps (now it does). | Yes |
| Agent Library | Monitors didn't say what happens when data is missing, so a missing input could read as "all clear". Every agent now stops and alerts, and a monitor never reports a pass on missing data. An Auto agent ticked readiness items itself (now it marks them for me to confirm). | Yes |
| Controls Catalog | The customer privacy law (GLBA) was described as covering business owners and guarantors, which is uncertain; now marked ⚠️ for privacy to confirm. Several controls gained the sub-steps that now build or prove them. 13 of 25 controls still have a stage not covered in the playbook (item W7, unchanged). | Yes |
| Glossary and language | "Risk contact" and "risk partner" named one role; "risk and issue list" had three names; "automation check" meant two things. Each now has one name. New terms: risk and issue list, project file, automation review. | Yes |
| Tech Stack Guide | Heading named the wrong page; the model risk note now cites the OCC's matching guidance and the possible SR 26-2 replacement (item W17). | Yes |
| The checker | It now also catches plural forms of retired words, and fails if an agent's number and name differ between the Product Machine, the playbook and the Agent Library. | Yes |

**Left on purpose:** the RM plan still quotes the old wording of gates 3 and 5. It's out of scope today and gets aligned when we do the RM work.

### Decisions for me: gaps to close before the RM and PM work

Each is a rule the machine needs and doesn't have. My recommendation is in the last column. **Decided 2026-10-15:** I approved the recommendations for gaps 1 to 6 and they are written into the How we deliver pages (closed item C39 in the Open Items log); gaps 7 to 9 stay optional.

| # | Gap | Why it matters for the RM and PM work | Label | My recommendation |
|---|---|---|---|---|
| 1 | **The unit of work.** Nothing says whether a gate is passed per project, per AI product or per feature wave. | The RM plan already runs gates per AI product and per feature wave in parallel; the PM plan will copy whatever we set. | **Needed** | One hierarchy: project (one per user group) → core use case → AI product → feature wave. Gates 1 and 2 per project the first time, then per feature wave (the quick pass); gates 3 and 4 per AI product, gate 5 per feature wave, gate 6 monthly per AI product and quarterly per project. |
| 2 | **Change after launch.** No rule says which changes go back through step 4. | RM pilots release every week or two; without a rule, each fix either breaks the approval or stalls. | **Needed** | A "material change" (new data, a new action, new users, a new or vendor-changed model) goes back through step 4; anything else is re-tested, logged and the risk partner told. ⚠️ The bank's model risk policy has the final word. |
| 3 | **The quick pass.** "A quick pass through Discover and Define" for the next feature wave is never defined. | RM waves 2 and 3 and every credit wave after the first come in this way. | **Needed** | A short checklist: which sub-steps are required (2.3 data contract update, 2.4 intake update, 2.5 stories, 2.7 measures), which reuse earlier work, and that gates 1 and 2 are decided in writing. |
| 4 | **The credit boundary.** Control K3 ("no credit decisions") would block the first PM product, credit memo drafts, which inform credit decisions. | Blocks the PM work as written. | **Needed before PM** | Restate K3 as "AI drafts or flags; a named credit officer decides", and add a higher-risk path in step 4 for products near credit decisions, set at 2.4. |
| 5 | **Products built on documents.** The data contract, data preparation and "simple rules first" assume data fields and rules. | Credit memos, financial statements and RM call notes are documents. | **Needed before PM** | A document variant in 2.3, 3.2 and 3.3: sources, content owner, re-indexing schedule, permissions per document and a check that every answer cites its source. |
| 6 | **From user workflow to AI products.** Discover doesn't start from the user workflow map, and nothing says how a map turns into candidate AI products. | Mapping the RM workflow (item W2) is the next job; its output has no defined way in. | **Needed** | Sub-steps 1.3 and 1.4 start from the user group's workflow map; the map's "where AI fits" list feeds 1.7's choice of target. |
| 7 | **Review depth by risk rating.** A low-risk internal tool goes through the same step 4 as a client-facing one. | Many RM admin products are low-risk; credit products are high-risk. | Optional | A lighter step 4 for low-risk products (fewer sign-offs, same tests), set by the rating in 2.4. Fits Elon mode. |
| 8 | **Four new controls:** hidden instructions in emails and documents (prompt injection), vendor model changes, how long logs are kept, and a periodic access review. | Any product that reads emails or call notes is exposed to the first. | Optional now, needed before the first build | Add them as K26 to K29 with "Comes from" lines. |
| 9 | **A fallback for each ⚠️ Auto task** if the bank says automations can't message people. | Otherwise the machine stalls waiting for that answer at the first project. | Optional | One line per ⚠️ row: what it becomes (usually Draft) if the answer is no. |

**Already planned, with what the audit adds:**
- **W4 templates:** add the outcome note, sizing table, measures sheet, value model, controls checklist, scale recommendation, monthly and quarterly packs, incident log, the sub-step log and a gate approval record.
- **W5 tracker design:** include the limiting factor, the date each gate pack was ready and the decision date (two machine measures depend on them).
- **W6 approvals map:** add credit officers and the credit policy owner when PM work starts.
- **W7 control gaps:** 13 of 25 controls (12 as of 2026-10-17) still have a stage not covered.
- **W10 support model:** incident severity, who may pause, rollback and the handover to the long-term owner.

### Proof

- The audit checker: 0 problems after the fixes. It now also checks agent names across files, the gate wording on the Product Workflow page's step cards, and plural forms of retired words.
- The render check: every designed page renders fully, and all 330 jump links land on their sections.
- The nothing-lost check: about 130 sentences changed; all are rewordings from these fixes, except the Framework's "Starting a new project" list, cut on purpose because it repeated sub-step 1.0 (it now points there).
- A fresh second reviewer checked every fix and found about 25 follow-ons, all fixed, including one rule an editor had changed by mistake (which steps are capped when many projects run at once), now put back as I set it.
- 12 pages were republished after checking that none had newer live edits: Product Workflow, Product Framework, Product Machine, Product Playbook, Steps Catalog, Workflow Maps, Agent Library, Controls Catalog, Glossary, Tech Stack Guide, Elon Mode and the Document Library.

_Last updated: 2026-10-18_
