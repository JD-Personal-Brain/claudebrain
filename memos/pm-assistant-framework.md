# The PM Assistant: the full delivery plan

Principal Applied AI Product Manager · Associated Bank · October 2026 (memo v1, 2026-10-19, first cut)

The detail behind the three short portfolio manager (PM) pages (the PM Executive Summary, The PM Assistant
and the PM Assistant Plan), read in PM Detail. What the product is, its capabilities and waves, and the
decisions behind them are in PM Detail, Part 3 (The PM Assistant in full detail); the rules every product
follows are in the [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ) and aren't repeated here.
Appendix A specifies the product's agents (A7 to A10) and Appendix B its workflows (B10 to B15), so the
team can build directly from them. It is a working hypothesis until Discover with the bank's PMs.

**The limiting factor: not known yet.** ⚠️ The real blockers are a first question
for the bank (what usually holds up a new AI tool there, and how long does the
credit policy owner's review take?). Possible ones, our assumptions to confirm:
approval to use borrower financials and credit files (the data contract, signed by
the data owners [names needed]; aimed for week 2), and the higher-risk review. Credit
memo and annual review drafts inform a credit decision, so wave 1 takes the
higher-risk path (control K3): a fairness check, must-refuse tests and the credit
policy owner's sign-off as well as the usual ones.

---

## 1. The outcome

The assistant has two goals that work together:

- **More PM time for judgment ("banker capacity"):** less time gathering financials, re-typing numbers and writing the routine parts of annual reviews and credit memos.
- **Earlier sight of credit trouble:** spotting a weakening borrower sooner, so the PM and RM can act while there are still options.

The return comes from three places. Finding out which is biggest is the first job:

| Lever | What the assistant does | Capabilities |
|---|---|---|
| **Save time on each review** | Gathers the borrower's file and drafts the routine sections of the annual review or credit memo, with a source on every number | Borrower file, review and memo drafts |
| **Faster answers for RMs and clients** | Shorter time from a credit request to a decision, because the first draft is ready sooner | Review and memo drafts, deal screening |
| **Fewer surprises in the portfolio** | Flags borrowers whose signals are weakening (late statements, a covenant near its limit, falling deposits) | Early warning watchlist, covenant and statement tracker |

---

## 2. The value model

The business case is built in Discover from real data. The structure is set now,
and the **[X]** values are filled in with the bank's numbers, not invented here.
Unlike the RM model, the PM model counts **costs saved** and tracks **loan losses
avoided**, because the bank has said its first AI work in this business includes
portfolio management, with goals that include faster loan processing (Bank
Business Briefing, section 4; ⚠️ check the release's exact wording).

| Part | How it's calculated |
|---|---|
| **Time saved** | PMs in scope [X] × reviews and memos per PM per year [X] × hours saved per review [X]. Reported as hours and as PM capacity (more reviews per PM, or time back for judgment); turned into cost only by the method Finance agrees |
| **Faster turnaround** | Days from a complete credit request to a decision, before and after [X]. Reported, not turned into revenue: any revenue it helps win already shows in the RM results |
| **Loan losses avoided** | Tracked, not counted in payback: borrowers flagged early, what was done, and what happened. Losses are rare and slow to show, so proving an effect takes years and a large portfolio ⚠️ (our judgment; Finance and credit risk decide whether it is ever counted) |
| **Costs** | Licenses + build effort + running costs (AI usage, data, document reading) + the higher-risk review + change management |
| **Net value** | Hours saved (valued by Finance's method) minus costs. Target payback: [X] months, judged for wave 1 as a whole |

**How it's proven:** pilot PMs are compared with similar PMs not yet using it, on
hours per review (time study or survey, method agreed with Finance), turnaround
and the share of drafts used with light edits. Every AI-drafted section is tagged
from day one.

---

## 3. Who's involved and who decides

The roles, what each one decides and the gates each joins are set once in the
[Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ). For the PM project they are:

| Role (Product Framework) | For the PM project |
|---|---|
| Sponsor | A credit or commercial banking leader [name needed] ⚠️ (whether credit or the business sponsors it is a first question) |
| User leaders | PM team leaders and credit managers: they choose the pilot group, decide with the sponsor whether to scale (gate 5), and use the watchlist in a portfolio review they already run (⚠️ to confirm) |
| Pilot users | Pilot PMs and credit analysts: they co-design and test, and grade the test set |
| Credit policy owner | What a draft may contain (for example, whether it may carry a recommendation), the must-refuse cases, and a sign-off at step 4 (higher-risk path, control K3) [name needed] |
| Credit officer | Makes every credit decision a draft or flag informs; named on every draft (K3) ⚠️ (may be the PM or a credit approver; to map) |
| Data owners | The owners of borrower financials, loan and covenant data and credit files (⚠️ which systems hold them is to confirm) [names needed] |
| Platform teams | Microsoft, AWS, data engineering and the loan system's team (⚠️ which loan system the bank uses is not public) |
| Long-term owner | To be decided by a date set in Define (sub-step 2.8); confirmed before scaling (5.7); for example, someone in credit administration |
| Also for PMs: credit risk review | Whether early warning flags change how loans are watched, and how a flag relates to the bank's own watchlist process (⚠️ to confirm) |

The risk partner, compliance, privacy and security (who sign off at step 4), vendor
risk, IT, Finance, Analytics and Operations join as the Product Framework sets out;
the risk partner's step 4 approval can't be overruled by the sponsor. **Every wave 1
capability takes the higher-risk path**, so the credit policy owner joins at 2.4 and
signs at 4.7, and compliance always runs the fairness check (4.4).

**Keeping partners aligned.** Decisions go in the decision log, and dependencies,
risks and issues in the risk and issue list (Product Framework). Its top item is the
limiting factor, named with its owner once the bank confirms what is actually
holding the work up (⚠️ not known yet).

---

## 4. How the work flows

Six steps, each ending in a go/no-go gate, run as the [Product Workflow](https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv)
sets out: its questions, gates and sub-steps aren't repeated here. The first pass overlaps:
a working prototype in week 1, the borrower file live in about weeks 3–5 and the drafts
in about weeks 6–9 (later than for RMs, because of the higher-risk path); then steps 3–6
repeat in cycles of a week or two, and each new feature wave takes the quick pass through
Discover and Define. What's different for PMs:

| Step | Gate for PMs | What's specific to PMs | General agents used (M20 to M33; M1 to M19 run every step as the Product Machine sets out) |
|---|---|---|---|
| **1. Discover** | The sponsor, with the risk partner, agrees the target lever, the main measure (hours per review is our first guess) and today's baseline (provisional; confirmed at gate 2), and confirms wave 1 | Count reviews and memos per PM per year and time each part (gathering, spreading, writing, approvals); interview and shadow PMs and credit analysts through one real annual review, starting from the PM user workflow; collect the bank's review and memo templates; learn how PMs are measured; test the prototype on sample borrowers every few days | M20 interview synthesizer, M21 opportunity sizer, M22 time-use analyst |
| **2. Define** | The brief, data contract and risk rating agreed (higher-risk path set); the credit policy owner agrees what drafts may contain; the value model shows payback within [X] months | The data contract covers documents (financial statements, tax returns, appraisals, prior reviews: their source, owner and who may see them); the risk intake marks wave 1 for the higher-risk path (K3) and lists the must-refuse cases (a risk rating, approve or decline, a price, a recommendation if the policy owner says no); Finance agrees how hours are valued | M23 requirements drafter, M24 data contract checker, M25 risk intake assistant |
| **3. Build** | Meets the quality bar in testing; every control is built and passes its control test | Every number in a draft traces to a source document or system (K7) and is checked in code; the "judgment" sections (risk rating, recommendation) are left for the PM, clearly marked; each PM sees only borrowers they may already see (K4); the test set uses real past reviews graded by experienced PMs, with must-refuse cases | M26 test grader |
| **4. Govern and test** | All sign-offs recorded, including the credit policy owner's, and the monitoring plan agreed | Register the product in the model inventory (⚠️ to confirm) and confirm its rating (SR 11-7; ⚠️ SR 26-2 may replace it, item W17); red-team for a credit decision, a rating, a price and other PMs' borrowers; fairness check agreed with compliance (are drafts equally complete and accurate across borrower types and sizes?); every draft names the credit officer who decides | M27 red-team agent, M28 fairness monitor, M29 evidence pack assembler |
| **5. Release and adopt** | Weekly use and leading results hit targets (at least [X]% of pilot PMs using drafts weekly; hours per review down [X]%); no serious incidents; long-term owner confirmed before scaling | A pilot group of PMs, with a comparison group; build it into the annual review cycle and the portfolio review managers already run (⚠️ to confirm); train on PMs' own borrowers; champions answer "how do I…?" | M30 feedback triage |
| **6. Measure and iterate** | Each month, keep, change or stop each AI product; each quarter, the sponsor with Finance decides to invest more, adjust or stop | Leading measures first (drafts used, hours per review, turnaround), visible within weeks; early warning judged on flags acted on and how early they came, not on losses avoided until Finance and credit risk agree a method | M31 impact analyst, M32 quality watchdog, M33 improvement scout |

---

## 5. How we deploy AI

The AI principles are the Product Framework's; the assistant's own limits are on The
PM Assistant page. What's specific to PMs:

**Choosing the platform.** The pilot picks one delivery platform, using the same five
criteria as every product (where PMs spend their day, where the data lives, fit with
approvals, cost model, speed to a pilot).

**Starting point, our assumption to confirm in Discover:** PMs write reviews and memos
in Word from a bank template and work in a loan system and a spreading tool (⚠️ which
ones is not public). If so: gather the borrower file from Snowflake (or Fabric) and the
document store, read documents with AWS Bedrock (with a Knowledge Base for the credit
file, citing pages), and deliver the draft as a Word document in the PM's own workspace
through a Copilot Studio agent in Teams. If the bank's loan system has its own drafting
features, compare it first: building where the work already happens comes before a new
path.

**What ships when:** in feature waves of capabilities (the capabilities and their waves
are in PM Detail, Part 3), with a release every week or two in between.

**The quality bar for PMs.** For PMs, accuracy means every number in a draft matches its
source exactly (zero tolerance on financial figures, ⚠️ our proposal to the risk partner),
sources shown means every figure and statement links to its document and page, and
permissions mean no PM sees a borrower they aren't allowed to see (zero tolerance).

---

## 6. The project plan (estimate)

Building starts on day one. The plan is organized around what most often holds banks up
(our assumption for Associated, to confirm): access to borrower data and the higher-risk
review. The risk partner and the credit policy owner see each version as it is built.

**What lets us move this fast.** The same six conditions as every product (build from day
one, standard features, low risk by design, review as we go, data access on day one, fast
decisions), with one change: wave 1 is **not** low risk by design, because drafts inform
credit decisions. What keeps it moving is that the AI never writes the judgment: the
rating and the recommendation stay with the PM.

**Backup plan if the higher-risk review runs long.** The borrower file goes first: it
gathers and cites, but writes no judgment and drafts no memo, so we assume it needs less
review (⚠️ the risk partner decides). The drafts keep improving in the test environment on
past reviews, ready the day sign-off lands. The call is made at gate 2.

**Wave 1: the first nine weeks**

| Week | What gets done | Owner | Proof it's done |
|---|---|---|---|
| Days 1–5 | Sponsor kickoff; risk partner and credit policy owner briefed; data access and test environments requested; working prototype on sample borrowers; the review templates collected; a first count of reviews per PM | Product manager, platform team | Prototype shown to the sponsor |
| 1 | **Gate 1:** target lever, main measure and provisional baseline agreed; wave 1 confirmed | Sponsor, with the risk partner | Decision log entry |
| 1–3 | Shadow 4–6 PMs and analysts through a real review (our estimate); time each part; improve the prototype every few days | Product manager, pilot PMs, analyst | Time map; feedback log |
| 2 | **Gate 2:** data contract, early risk rating (higher-risk path), what drafts may contain (credit policy owner), measures and value model | Sponsor, data owners, risk partner, credit policy owner | Signed data contract; decision log |
| 2–4 | Borrower file built and tested on real data; controls tested; sign-offs | Platform team, risk partner | Gate 3 and 4 entries |
| About 3–5 | **Borrower file live with pilot PMs** | Product manager | First weekly usage report |
| 2–7 | Review and memo drafts built on past reviews; test set graded by PMs, with must-refuse cases; fairness check agreed with compliance; evidence pack | Platform teams, product manager, compliance | Test results against the quality bar |
| 6–8 | Sign-offs for the drafts, including the credit policy owner's; readiness (training, incident process, comparison group) | Risk, compliance, privacy, security, credit policy owner | Sign-offs recorded |
| About 6–9 | **Annual review and credit memo drafts live with pilot PMs** | Product manager | Hours per review; drafts used |

**By day 90 (about week 13):** the borrower file has been live for about two months and the
drafts for about one; leading measures are coming in. Waves 2 and 3 get dates at gate 2.

---

## 7. Top risks and how I'd handle them

| Risk | How I'd handle it |
|---|---|
| **A wrong number in a credit draft** | Every number traced to its source and checked in code before the PM sees the draft; zero tolerance in the test set; drafts marked as drafts |
| **The AI drifts into the credit decision** | It never writes the rating or the recommendation; must-refuse tests; guardrails; the credit officer named on every draft (K3) |
| **The higher-risk review takes longer** | Brief the credit policy owner in week one; the borrower file goes first (backup plan) |
| **Documents are scanned, messy or spread across systems** (⚠️ to confirm) | Start with the documents already in a standard form; the borrower file shows what's missing instead of guessing (K25) |
| **PMs don't trust the drafts** | A source on every figure; build it with pilot PMs on their own past reviews; PMs edit freely |
| **Uneven quality across borrower types** | The fairness check compares draft accuracy and completeness across borrower types and sizes |
| **Early warning floods PMs with flags** | Few, explainable rules agreed with credit risk; every flag shows its numbers; measure flags acted on and tune |

---

## 8. What I'd confirm in the first weeks

This is the one full list; the Executive Summary asks the top few.

- What usually holds up a new AI tool at the bank, and how does the credit policy owner review AI that informs credit?
- How many PMs and credit analysts are there, how many borrowers each, and how many annual reviews and memos a year?
- How long does an annual review take today, and which part takes longest?
- Which loan system and spreading tool does the bank use, and do they have drafting features already?
- Where do borrower financials, covenants and credit files live, and who owns them?
- Is there a standard template for annual reviews and credit memos?
- May a draft carry a recommendation, or must it stop at the facts?
- Who is the credit officer for each kind of decision?
- How does the bank watch credit quality today (a watchlist, a portfolio review), and who runs it?
- Which PM teams would make a good pilot group?
- How are PMs measured, and what team and budget does the pilot have?

---

## Appendix A: Agent specs

The product's own agents. PM agents are numbered on from the RM ones (A7 onward) so no
number means two things. **[X]** values are set in Define.

**Rules for every agent:**
- **One job.** If a request falls outside it, the agent says so and stops.
- **Read-only by default.** Any change to a record needs a named person's click.
- **Approved models and data only.** Uses only AI models and data sources approved for this product.
- **Never guesses.** If its inputs are missing, stale or fail a check, it stops and says what's missing (K25).
- **Never decides credit.** It never sets or suggests a risk rating, never approves or declines, never sets a price, and writes a recommendation only if the credit policy owner allows it (K3).
- **Everything logged.** Each run records who, what, when, which sources and what it produced.

### Agents PMs use (the product)

**A7. Borrower file builder** · wave 1 · runs on Snowflake and AWS Bedrock (Knowledge Bases)
- **Job:** pull everything about one borrower into one file: the financials and their trend, loans and their terms, covenants and their latest tests, deposits and payment history, the last review, the RM's recent notes, and dated public news; list what's missing or late.
- **Inputs:** certified views of loans, covenants, deposits and payments; the spread of the financial statements; the credit file documents; the RM's approved call notes (⚠️ which systems hold each is to confirm).
- **Allowed actions:** read the inputs; write the file to the assistant's own workspace.
- **Not allowed:** changing any record; filling a gap with an estimate; reading borrowers outside the PM's permissions.
- **Outputs:** one borrower file, every figure with its source (document and page, or system and date), and a "missing or late" list.
- **Stops when:** the file is built, or a required input is missing or older than [X] days (it says which and stops).
- **Proof it worked:** a sample of files matches the source systems exactly; missing items are listed, never filled.
- **Person in charge:** the PM; the data owners for the inputs.

**A8. Review and memo drafter** · wave 1 · runs on AWS Bedrock or a Copilot Studio agent · higher-risk path (K3)
- **Job:** draft the routine sections of an annual review or a credit memo in the bank's template, from A7's file: the borrower, the relationship, financial performance, covenant compliance, collateral facts and the risks the numbers show.
- **Inputs:** the borrower file from A7; the bank's template; for a credit memo, the request as the RM or PM wrote it.
- **Allowed actions:** read the inputs; create a draft for the PM.
- **Not allowed:** writing a risk rating, an approve or decline, or a price; writing a recommendation unless the credit policy owner allows it; stating any number not in the borrower file.
- **Outputs:** a draft marked "AI draft" with the judgment sections left blank for the PM, every figure linked to its source, and the credit officer who decides named at the top.
- **Stops when:** the draft is delivered, or the file has a gap a section needs (it marks the section "needs input" and stops there).
- **Proof it worked:** test-set score meets the quality bar (accuracy zero tolerance, sources, usefulness graded by PMs); every must-refuse case refused.
- **Person in charge:** the PM writes the judgment and owns the final document; the credit officer decides.

**A9. Early warning watcher** · wave 2 · runs on Snowflake (Cortex) · higher-risk path (K3)
- **Job:** each night, check each PM's borrowers against the agreed early warning rules (for example: financial statements late, a covenant within [X]% of its limit, deposits down [X]%, overdrafts, a payment past due) and explain each flag in plain English.
- **Inputs:** certified views of covenants, deposits, payments and statement due dates; the rule set owned by credit risk.
- **Allowed actions:** read; write flags to the assistant's watchlist.
- **Not allowed:** changing a risk rating or a watchlist status; inventing flags outside the rule set; telling the borrower.
- **Outputs:** a watchlist per PM, each flag with the rule that fired and the numbers behind it.
- **Stops when:** every borrower is checked, or the data is older than [X] hours (it alerts the data owner and produces nothing).
- **Proof it worked:** a sample of flags matches the source numbers; flags acted on ≥ [X]%.
- **Person in charge:** the PM decides what to do; credit risk owns the rules.

**A10. Credit policy Q&A** · wave 3 · runs on a Copilot Studio agent or AWS Bedrock (Knowledge Bases)
- **Job:** answer PMs' and analysts' questions from the bank's credit policy, citing the section.
- **Inputs:** the current credit policy and procedures, read-only.
- **Allowed actions:** read; answer with the section cited.
- **Not allowed:** deciding whether a specific loan meets policy; answering from anything but the policy.
- **Outputs:** an answer with its section, or "the policy doesn't say; ask [owner]."
- **Stops when:** answered, or out of scope.
- **Proof it worked:** test-set score meets the quality bar; answers checked by the credit policy owner's team.
- **Person in charge:** the credit policy owner for content; the product manager for quality.

### Agents the team uses

The team uses the product machine's general agents, specified in full in the
[Agent Library](https://claude.ai/artifact/Cn9nANQoqp2BP7yrmy61zn); which ones each step uses is in section 4.

## Appendix B: Workflows

Each PM-facing capability as a step-by-step flow. Every PM-facing flow (B10–B14) has one
**decision point** where the PM decides, and everything is logged. B15 is the release routine.

**B10. Borrower file** (wave 1; first in the backup plan)
- **Trigger:** a review comes due in [X] days, a credit request arrives, or the PM asks.
- **Steps:** 1. A7 checks the PM may see the borrower. 2. It gathers the file, with a source on every figure. 3. It lists what's missing or late. 4. **Decision point:** the PM uses the file, asks for what's missing, or flags an error.
- **Logged:** files built, opened, errors flagged.
- **Measures:** hours spent gathering (before and after); errors found.

**B11. Annual review draft** (wave 1)
- **Trigger:** a borrower file is ready for a review coming due.
- **Steps:** 1. A8 drafts the routine sections in the bank's template. 2. Every number is checked against the file in code. 3. **Decision point:** the PM edits, writes the judgment sections and submits the review through the bank's normal process. Nothing is submitted by the assistant.
- **Logged:** drafts, edits, sections kept or rewritten.
- **Measures:** hours per review; share of sections used with light edits.

**B12. Credit memo draft** (wave 1)
- **Trigger:** a new request, renewal or line change with a borrower file ready.
- **Steps:** 1. A8 drafts the memo's routine sections, restating the requested terms as written. 2. The number check runs. 3. **Decision point:** the PM writes the analysis and recommendation (if any) and sends it to the credit officer through the bank's normal approval route.
- **Logged:** drafts, edits, time from request to submission.
- **Measures:** turnaround; hours per memo.

**B13. Early warning watchlist** (wave 2)
- **Trigger:** A9's nightly check finds a flag.
- **Steps:** 1. A9 explains it with the numbers. 2. The flag appears on the PM's watchlist and in a weekly summary. 3. **Decision point:** the PM dismisses it (with a reason), watches it, or raises it through the bank's own process, telling the RM.
- **Logged:** flags, decisions, reasons, outcomes.
- **Measures:** flags acted on; how many weeks earlier than today's process (⚠️ to measure against the bank's watchlist).

**B14. Covenant and statement tracker** (wave 2)
- **Trigger:** a statement or compliance certificate due date, or a new spread.
- **Steps:** 1. Rules in code calculate each covenant test from the spread and list what's due or late. 2. **Decision point:** the PM confirms the result and decides any follow-up; reminders to the RM or borrower are drafted for the PM to send.
- **Logged:** tests, confirmations, reminders.
- **Measures:** late items; analyst hours saved.

**B15. Every release (every week or two)**
- **Trigger:** any change to prompts, rules, templates, data or models.
- **Steps:** 1. M32 re-runs the test set, including every must-refuse case. 2. If the score is below the quality bar, the release stops. 3. If the change is material (Product Framework), it goes back through step 4, with the credit policy owner. 4. Release; M32 watches live quality for [X] days.
- **Logged:** test scores, approvals, release notes.
- **Measures:** quality trend; releases rolled back.

_Last updated: 2026-10-19_
