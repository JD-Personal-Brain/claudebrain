# The PM Assistant: the full delivery plan

Associated Bank · Corporate and Commercial Banking · October 2026

The detail behind the three short portfolio manager (PM) pages (the PM Executive Summary, The PM Assistant
and the PM Assistant Plan), read in PM Detail. What the product is, its capabilities and waves, and the
decisions behind them are in PM Detail, Part 3 (The PM Assistant in full detail); the rules every product
follows are in the [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ) and aren't repeated here.
Appendix A specifies the product's agents (A7 to A11) and Appendix B its workflows (B10 to B16), so the
team can build directly from them. It is a working hypothesis until Discover with the bank's PMs.

**The limiting factor: not known yet.** ⚠️ The real blockers are a first question
for the bank (what usually holds up a new AI tool there, and how long does the
credit policy owner's review take?). Possible ones, our assumptions to confirm:
approval to use borrower financials and credit files (the data contract, signed by
the data owners [names needed]; aimed for weeks 2 to 4), and the higher-risk review. Credit
memo and annual review drafts inform a credit decision, so the feature wave 1 drafts take the
higher-risk path (control K3): a fairness check, must-refuse tests and the credit
policy owner's sign-off as well as the usual ones. The industry background draft, the first capability, uses
no borrower data, so it doesn't wait for the data contract's borrower fields.

---

## 1. The outcome

The assistant has two goals that work together:

- **More PM time for judgment ("banker capacity"):** less time gathering financials, re-typing numbers and writing the routine parts of annual reviews and credit memos.
- **Earlier sight of credit trouble:** spotting a weakening borrower sooner, so the PM and the relationship manager (RM) can act while there are still options.

The return comes from four places. Finding out which is biggest is the first job:

| Lever | What the assistant does | Capabilities |
|---|---|---|
| **Replace an outside cost** | Drafts the industry background section of the credit memo, which an outside firm the bank pays writes today, according to the bank's credit lead (2026-10-19; ⚠️ details to confirm), from approved sources with every statement cited | Industry background draft |
| **Save time on each review** | Gathers the borrower's file and drafts the routine sections of the annual review or credit memo, with a source on every number | Borrower file, review and memo drafts |
| **Faster reviews, and faster answers on new requests** | Shorter time from a credit request to a decision, because the first draft is ready sooner | Review and memo drafts, deal screening |
| **Fewer surprises in the portfolio** | Flags borrowers whose signals are weakening (late statements, a covenant near its limit, falling deposits) | Early warning flags, covenant and statement tracker |

---

## 2. The value model

The business case is built in Discover from real data. The structure is set now,
and the **[X]** values are filled in with the bank's numbers, not invented here.
Unlike the RM model, the PM model counts **costs saved** and tracks **loan losses
avoided**, because the bank has said its first AI work in this business includes
portfolio management (we read this as loan portfolio management, PMs' work; to confirm), with goals that include faster loan processing (Bank
Business Briefing, section 4; ⚠️ check the release's exact wording). The bank's credit lead (2026-10-19; ⚠️ details to confirm: which firm, cost per section, how many a year, turnaround, the contract's terms, and which sources the firm uses) told us the bank pays an outside firm to write the industry background section of its credit memos, and wants AI to draft that section as one of the first use cases.

| Part | How it's calculated |
|---|---|
| **Outside cost saved** | Industry sections written outside per year [X] × fee per section [$X]; plus days of turnaround saved [X]. Counted only once the outside firm's contract actually changes ⚠️ (its notice period is to confirm) |
| **Time saved** | PMs in scope [X] × reviews and memos per PM per year [X] × hours saved per review [X]. Reported as hours and as PM capacity (more reviews per PM, or time back for judgment); turned into cost only by the method Finance agrees |
| **Faster turnaround** | Days from a complete credit request to a decision, before and after [X]. Reported, not turned into revenue: any revenue it helps win already shows in the RM results |
| **Loan losses avoided** | Tracked, not counted in payback: borrowers flagged early, what was done, and what happened. Losses are rare and slow to show, so proving an effect takes years and a large portfolio ⚠️ (our judgment; Finance and credit risk decide whether it is ever counted) |
| **Costs** | Licenses + build effort + running costs (AI usage, data, document reading) + the higher-risk review + change management |
| **Net value** | Outside fees saved (once the contract changes) plus hours saved (valued by Finance's method) minus costs. Target payback: [X] months, judged for wave 1 as a whole |

**How it's proven:** pilot PMs are compared with similar PMs not yet using it, on
hours per review (time study or survey, method agreed with Finance), turnaround
and the share of drafts used with light edits. For the industry background draft: outside
fees saved once the contract changes, the section's turnaround (days from request to an approved section) and the
share of each section kept with light edits. Every AI-drafted section is tagged
from day one.

---

## 3. Who's involved and who decides

The roles, what each one decides and the gates each joins are set once in the
[Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ). For the PM project they are:

| Role (Product Framework) | For the PM project |
|---|---|
| Sponsor | A credit or commercial banking leader [name needed] ⚠️ (whether credit or the business sponsors it is a first question) |
| User leaders | PM team leaders and credit managers: they choose the pilot group, decide with the sponsor whether to scale (gate 5), and use the early warning flags in a portfolio review they already run (⚠️ to confirm) |
| Pilot users | Pilot PMs and credit analysts: they co-design and test, and grade the test set |
| Credit policy owner | What a draft may contain (for example, whether a later feature wave's drafts may carry a recommendation, asked in that wave's quick pass), the must-refuse cases, and a sign-off at step 4 (higher-risk path, control K3) [name needed] |
| Credit officer | Whoever holds approval authority for that credit under the bank's authority list (it may be the PM; ⚠️ to confirm): makes every credit decision a draft or flag informs; named on every draft (K3) |
| Data owners | The owners of borrower financials, loan and covenant data and credit files (⚠️ which systems hold them is to confirm) [names needed], including the credit file's content owner, who signs the list of documents the assistant may read (statements, tax returns, appraisals, prior reviews; sub-step 2.3), for example credit administration (⚠️ to confirm) |
| Platform teams | Microsoft, AWS, data engineering and the loan system's team (⚠️ which loan system the bank uses is not yet known) |
| Long-term owner | To be decided by a date set in Define (sub-step 2.8); confirmed before scaling (5.7); for example, someone in credit administration |
| Owner of the outside firm's contract | Vendor management or procurement (⚠️ which team, to confirm): whether and when the contract for industry sections changes, once the industry background draft is proven; vendor risk approves any licensed industry data source the draft reads (K14) |
| From feature wave 2: credit risk | Owns the early warning rules and signs the rule set at 4.7; with credit risk review, decides how a flag relates to the bank's own watchlist process (⚠️ which teams, to confirm) |

The risk partner, compliance, privacy and security (who sign off at step 4), vendor
risk, IT, Finance, Analytics and Operations join as the Product Framework sets out;
the risk partner's step 4 approval can't be overruled by the sponsor. **The review and memo drafts take
the higher-risk path**, so the credit policy owner joins at 2.4 and signs at 4.7, and
compliance runs the fairness check (4.4). We assume the borrower file does not, because
it gathers and cites but writes no judgment (⚠️ the risk partner decides at 2.4). K3's wording (output that informs a credit decision) could cover it, which is why it is the first question for the risk partner at 2.4, and why the backup plan covers it. We also assume the industry background draft does not, because it uses no borrower data and writes no judgment about the borrower; but it sits inside a credit memo, so the risk partner decides that at 2.4 too ⚠️.

**Keeping partners aligned.** Decisions go in the decision log, and dependencies,
risks and issues in the risk and issue list (Product Framework). Its top item is the
limiting factor, named with its owner once the bank confirms what is actually
holding the work up (⚠️ not known yet).

---

## 4. How the work flows

Six steps, each ending in a go/no-go gate, run as the [Product Workflow](https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv)
sets out: its questions, gates and sub-steps aren't repeated here. The first pass overlaps:
a working prototype in week 1, the industry background draft live in about week 6, the borrower
file in about week 7 and the drafts in about week 12 (later than for RMs, because of the higher-risk path); then steps 3–6
repeat in cycles of a week or two, and each new feature wave takes the quick pass through
Discover and Define. What's different for PMs:

| Step | Gate for PMs | What's specific to PMs | General agents used (M20 to M33; M1 to M19 run every step as the Product Machine sets out) |
|---|---|---|---|
| **1. Discover** | The sponsor, with the risk partner, agrees the target lever, the main measure (hours per review is our first guess) and today's baseline (provisional, from the first sizing in 1.2; final baseline checked at gate 2), and confirms wave 1 | Count reviews and memos per PM per year and time each part, and count the industry sections the outside firm writes, their fee and turnaround (⚠️ to confirm) (gathering, spreading, writing, approvals); interview and shadow PMs and credit analysts through one real annual review (with consent before recording any shadowing session, K24), starting from Map 3 on the Workflow Maps (the PM user workflow, how PMs work today, is not written yet); collect the bank's review and memo templates; learn how PMs are measured; test the prototype on sample borrowers every few days | M20 interview synthesizer, M21 opportunity sizer, M22 time-use analyst |
| **2. Define** | The brief, data contract (K5) and the product's risk rating agreed (higher-risk path set); the final baseline; the credit policy owner agrees what drafts may contain; the order of feature waves 2 and 3 agreed; their dates set once the wave 1 drafts' higher-risk review is signed (about week 11), when its real length is known; the value model shows payback within [X] months | The data contract includes the approved industry source list for the industry background draft, with each source's license terms (K5; vendor risk reviews any licensed source, K14), and covers documents (financial statements, tax returns, appraisals, prior reviews: their source, owner and who may see them), which fields are sensitive and hidden or labeled (K6: guarantors' personal financial statements, tax-return identifiers; privacy confirms which laws apply ⚠️), and the bank's approval-authority list ⚠️ (to confirm); M24 checks the data fields; the content owner of the credit file checks the documents' re-indexing and permissions by hand until M24 gains a documents mode; the risk intake marks the drafts for the higher-risk path (K3) and lists the must-refuse cases (a borrower risk rating, approve or decline, a price, and a recommendation: always in wave 1, later if the policy owner says no); Finance agrees how hours are valued | M23 requirements drafter, M24 data contract checker (then on every data refresh), M25 risk intake assistant |
| **3. Build** | Meets the quality bar in testing; every control is built and passes its control test | The industry background draft is built and tested on public sources from week 1, every statement cited and dated (K7); every number in a draft traces to a source document or system (K7) and is checked in code; the "judgment" sections (borrower risk rating, recommendation) are left for the PM, clearly marked; each PM sees only borrowers they may already see (K4); the test set uses real past reviews graded by experienced PMs, with must-refuse cases | M26 test grader |
| **4. Govern and test** | All sign-offs recorded, including the credit policy owner's, and the monitoring plan agreed | Register the product in the model inventory (⚠️ to confirm) and confirm its rating (SR 11-7; ⚠️ SR 26-2 may replace it; to check); privacy compares the documents retrieved with the contract's sources by hand (M13 doesn't cover documents yet); red-team for a credit decision, a borrower risk rating, a price, other PMs' borrowers, instructions hidden inside a borrower-supplied document, one borrower's figures leaking into another's draft, a number with no source, and borrower data, a judgment about the borrower or an uncited statement in the industry background section (M27, K10); fairness check (4.4; compliance sets the fair-lending groups and what data exists for them ⚠️; we'd also compare draft accuracy and completeness across borrower types and sizes as a quality check); every draft names the credit officer who decides, from the bank's approval-authority list | M26 test grader (on the frozen version), M27 red-team agent, M28 fairness monitor (then monthly), M29 evidence pack assembler |
| **5. Release and adopt** | Weekly use and leading results hit targets (at least [X]% of pilot PMs using the assistant weekly; at least [X]% of draft sections kept with light edits); no serious incidents; long-term owner confirmed before scaling. Hours per review and turnaround are judged in step 6, once enough reviews are done | A pilot group of PMs, with a comparison group; build it into the annual review cycle and the portfolio review managers already run (⚠️ to confirm); train on PMs' own borrowers; champions show peers how they use it (5.5) | M30 feedback triage |
| **6. Measure and iterate** | Each month (and at the end of each feature wave), keep, change or stop each AI product, on results against the comparison group; each quarter, the sponsor with Finance decides to invest more, adjust or stop | Leading measures first (drafts used, hours per review, turnaround), visible within weeks; early warning judged on flags acted on and how early they came, not on losses avoided until Finance and credit risk agree a method | M31 impact analyst, M32 quality watchdog, M33 improvement scout |

---

## 5. How we deploy AI

The AI principles are the Product Framework's; the assistant's own limits are on The
PM Assistant page. What's specific to PMs:

**Choosing the platform.** The pilot picks one delivery platform, using the same five
criteria as every product (where PMs spend their day, where the data lives, fit with
approvals, cost model, speed to a pilot).

**Starting point, our assumption to confirm in Discover:** PMs write reviews and memos
in Word from a bank template and work in a loan system and a spreading tool (⚠️ which
ones is not yet known). If so: gather the borrower file from Snowflake (or Fabric) and the
document store, read documents with AWS Bedrock (with a Knowledge Base for the credit
file, citing pages), and deliver the draft as a Word document in the PM's own workspace
through a Copilot Studio agent in Teams. Each search is limited to the one borrower and to borrowers the PM may see (K4; how the index enforces this is a question for the platform team ⚠️). If the bank's loan system has its own drafting
features, compare it first: building where the work already happens comes before a new
path. Vendors already sell memo drafting and policy Q&A (nCino Banking Advisor, Moody's agents, S&P Global); compare them with vendor risk at 2.2 before building (K14). Microsoft publishes a Copilot Studio credit memo pattern close to our starting point (a how-to scenario, not a bank result).

**What ships when:** in feature waves of capabilities (the capabilities and their waves
are in PM Detail, Part 3), with a release every week or two in between.

**The quality bar for PMs.** For PMs, accuracy means every number in a draft matches its
source exactly (zero tolerance on financial figures, ⚠️ our proposal to the risk partner),
sources shown means every figure and statement links to its document and page, and
permissions mean no PM sees a borrower they aren't allowed to see (zero tolerance).

---

## 6. The project plan (estimate)

Building starts on day one, on sample borrowers. The plan is organized around what most
often holds banks up (our assumption for Associated, to confirm): access to borrower data
and the higher-risk review. The risk partner and the credit policy owner see each version
as it is built. No real borrower data goes into the assistant or its tests before gate 2 (sizing counts and watching PMs at work aside).

**What lets us move this fast.** The six conditions in the [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ#what-lets-a-project-move-fast), each checked in the first days, with one exception: the drafts can't meet condition 3 (low risk by design), because they inform credit decisions. What keeps them moving is that the AI never writes the judgment: the borrower risk rating and the recommendation stay with the PM.

**The backup plan, for four things that could run long** (the call is made at gate 2):
- **The industry background draft's review.** If it runs long, it is no worse than today: the outside firm keeps writing the section until sign-off. If the risk partner puts it on the higher-risk path (2.4), it goes through step 4 with the drafts and goes live at about week 12.
- **Approval to use borrower data.** Everything waits for it; the prototype keeps running on sample borrowers with pilot PMs, and the live dates are reset at gate 2.
- **The borrower file is put on the higher-risk path too** (the risk partner's call at 2.4). Then it goes through step 4 with the drafts and both go live together, at about week 12.
- **The higher-risk review of the drafts.** The borrower file stays live on its own. The version under review is frozen (K17); the frozen drafts are tested on a pinned version of the borrower file, and borrower-file changes that reach the drafts wait for sign-off or go through step 4 with them. Improvements wait in the backlog and ship after sign-off through the release routine (B15), and any material change goes back through step 4.

**Wave 1: the first 13 weeks**

| Week | What gets done | Owner | Proof it's done |
|---|---|---|---|
| Days 1–5 | Sponsor kickoff; risk partner and credit policy owner briefed; the industry background draft started on public sources; data access and test environments requested; vendor risk asked whether AWS Bedrock and the model provider are approved for borrower data (K14, K19); IT asked to approve each connection (2.2, K20); working prototype on sample borrowers; the review templates collected; a first count of reviews per PM, from credit administration's review calendar if one exists (⚠️ to confirm) | Product manager, platform team | Prototype shown to the sponsor |
| 1 | **Gate 1:** target lever, main measure and provisional baseline agreed; wave 1 confirmed | Sponsor, with the risk partner | Decision log entry |
| 1–3 | Shadow 4–6 PMs and analysts through a real review (our estimate); time each part, which gives the final baseline; improve the prototype every few days | Product manager, pilot PMs, analyst | Time map; feedback log |
| 1–4 | Borrower file and drafts built and tested on sample borrowers | Platform team | Prototype test results |
| 1–5 | Industry background draft built and tested on public sources (it needs no client data): test set graded by PMs, every statement cited and dated (K7); the approved source list and its license terms agreed with the content owner and vendor risk (K5, K14); evidence pack | Platform team, product manager, vendor risk | Test results against the quality bar |
| About 4 | **Gate 2:** final baseline, data contract (with the approved industry source list), the product's early risk rating (which capabilities take the higher-risk path), what drafts may contain (credit policy owner), measures and value model; the order of feature waves 2 and 3 agreed; their dates set once the wave 1 drafts' higher-risk review is signed (about week 11), when its real length is known. Aimed for weeks 2 to 4, paced by the data owners' signatures (⚠️) | Sponsor, data owners, content owner of the credit file, risk partner, credit policy owner | Signed data contract; decision log |
| 5 | Industry background draft: frozen version, sign-offs (after gate 2); monitoring plan (4.8); readiness: training, incident process (5.1) | Risk partner, vendor risk, product manager | Gate 3 and 4 entries |
| About 6 | **Industry background draft live with pilot PMs** | Product manager | Sections drafted; sections kept with light edits |
| 5–6 | Borrower file on real data, after gate 2: test set, controls tested, frozen version, sign-offs; monitoring plan (4.8); readiness: training, incident process, comparison group (5.1) | Platform team, risk partner | Gate 3 and 4 entries |
| About 7 | **Borrower file live with pilot PMs** | Product manager | First weekly usage report |
| 5–9 | Review and memo drafts on real past reviews, after gate 2; test set graded by PMs, with must-refuse cases; fairness check agreed with compliance; evidence pack | Platform teams, product manager, compliance | Test results against the quality bar |
| 10–11 | Higher-risk review of the frozen drafts: sign-offs, including the credit policy owner's; readiness (training, incident process, comparison group) | Risk, compliance, privacy, security, credit policy owner | Sign-offs recorded |
| About 12 | **Annual review and credit memo drafts live with pilot PMs** | Product manager | Drafts used; sections kept with light edits |

**By day 90 (about week 13):** the industry background draft has been live for about eight weeks,
the borrower file for about seven and the drafts for about one or two; the first leading measures are coming in. Feature waves 2 and 3 get
dates once the drafts' higher-risk review is signed (about week 11), when its real length is known.

---

## 7. Top risks and how I'd handle them

| Risk | How I'd handle it |
|---|---|
| **A wrong number in a credit draft** | Every number traced to its source and checked in code before the PM sees the draft; zero tolerance in the test set; drafts marked as drafts |
| **The AI drifts into the credit decision** | It never writes the borrower risk rating or the recommendation; must-refuse tests; guardrails (K8); the credit officer named on every draft (K3) |
| **Approval to use borrower data takes longer** | Request it on day one; keep the prototype running on sample borrowers; the data contract is aimed at weeks 2 to 4 |
| **The higher-risk review takes longer** | Brief the credit policy owner in week one; the borrower file goes ahead of the drafts (backup plan) |
| **Documents are scanned, messy or spread across systems** (⚠️ to confirm) | Start with the documents already in a standard form; the borrower file shows what's missing instead of guessing (K25) |
| **PMs don't trust the drafts** | A source on every figure; build it with pilot PMs on their own past reviews; PMs edit freely |
| **Uneven quality across borrower types** | The fairness check compares draft accuracy and completeness across borrower types and sizes |
| **Loan review or examiners question AI-drafted text in the credit file** | Every draft stamped AI-drafted and approved by the named PM, with sources kept; brief loan review early |
| **Copyright and license terms of the industry sources** | Only sources on the approved list, each with its license terms recorded in the data contract (K5) and reviewed by vendor risk (K14); nothing copied from a licensed report beyond what its license allows; every statement cited and dated (K7) |
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
- Is there an approval-authority list (who may decide which credits), and who keeps it?
- Who is the credit officer for each kind of decision?
- How does the bank watch credit quality today (a watchlist, a portfolio review), and who runs it?
- Which PM teams would make a good pilot group? Is the new Franchise Banking team, announced with a portfolio manager working alongside a relationship manager (Bank Business Briefing, section 4), a good first one?
- How are PMs measured, and what team and budget does the pilot have?
- Does Finance accept costs saved and loan losses avoided as returns, and how are PM hours valued?
- Are American National's borrowers and credit files on the bank's systems yet?
- The industry background section: which outside firm writes it, what each section costs, how many a year, how long each takes, the contract's notice period, which sources the firm uses, and does the bank already license industry data? ⚠️

---

## Appendix A: Agent specs

The product's own agents. PM agents are numbered on from the RM ones (A7 onward) so no
number means two things. **[X]** values are set in Define.

**Rules for every agent:**
- **One job.** If a request falls outside it, the agent says so and stops.
- **Read-only by default.** Any change to a record, or anything that reaches a borrower or client, needs a named person's click (K1, K2).
- **Approved models and data only.** Uses only AI models and data sources approved for this product (K19, K5).
- **Never guesses.** If its inputs are missing, stale or fail a check, it stops, says what's missing and alerts its owner (K25).
- **Never decides credit.** It never sets or suggests a borrower risk rating, never approves or declines and never sets a price (K3). Wave 1 drafts leave the recommendation blank; whether a later draft may carry one is the credit policy owner's call at 2.4 (our assumption).
- **Everything logged.** Each run records who, what, when, which sources and what it produced.

### Agents PMs use (the product)

**A7. Borrower file builder** · wave 1 · runs on Snowflake and AWS Bedrock (Knowledge Bases)
- **Job:** pull everything about one borrower into one file: the financials and their trend, loans and their terms, covenants and their latest tests, deposits and payment history, the last review and the RM's recent notes; list what's missing or late. (Public news about the borrower would be a later addition, through the data contract and a vendor review.)
- **Inputs:** certified views of loans, covenants, deposits and payments; the spread of the financial statements; the credit file documents; the RM's approved call notes, if the bank's RM tools hold them (optional; the file works without them).
- **Allowed actions:** read the inputs; write the file to the assistant's own workspace.
- **Not allowed:** changing any record; filling a gap with an estimate; reading borrowers outside the PM's permissions; showing a field the data contract marks as hidden (K6).
- **Outputs:** one borrower file, every figure with its source (document and page, or system and date), and a "missing or late" list.
- **Stops when:** the file is built, or a required input is missing or older than [X] days (it says which and stops).
- **Proof it worked:** a sample of files matches the source systems exactly; missing items are listed, never filled.
- **Starts when:** a review comes due in [X] days, a credit request arrives or the PM asks (B10).
- **Person in charge:** the PM; the data owners for the inputs.
- **To confirm:** ⚠️ which systems hold each input.

**A8. Review and memo drafter** · wave 1 · runs on AWS Bedrock or a Copilot Studio agent · higher-risk path (K3)
- **Job:** draft the routine sections of an annual review or a credit memo in the bank's template, from A7's file: the borrower, the relationship, financial performance, covenant compliance, collateral facts and changes and items to note (plain facts with sources; the PM draws the conclusions).
- **Inputs:** the borrower file from A7; the bank's template; the bank's approval-authority list (who decides what, to name the credit officer; see To confirm); for a credit memo, the request as the RM or PM wrote it.
- **Allowed actions:** read the inputs; create a draft for the PM.
- **Not allowed:** writing a borrower risk rating, an approve or decline, or a price; writing the recommendation (left for the PM; later only if the credit policy owner allows it at 2.4); stating any number not in the borrower file.
- **Outputs:** a draft marked "AI draft" with the judgment sections left blank for the PM, every figure linked to its source, and the credit officer who decides named at the top.
- **Stops when:** the draft is delivered, or the file has a gap a section needs (it marks the section "needs input" and stops there).
- **Proof it worked:** test-set score meets the quality bar (accuracy zero tolerance, sources, usefulness graded by PMs); every must-refuse case refused.
- **Starts when:** a borrower file is ready (B11, B12). For a credit memo, the industry background section comes from A11 (B16) once the PM approves it.
- **Person in charge:** the PM writes the judgment and owns the final document; the credit officer decides.
- **To confirm:** ⚠️ the bank's review and memo templates; whether an approval-authority list exists and who keeps it.

**A9. Early warning watcher** · wave 2 · runs on Snowflake (Cortex) · higher-risk path (K3)
- **Job:** each night, check each PM's borrowers against the agreed early warning rules (for example: financial statements late, a covenant within [X]% of its limit or breached, deposits down [X]%, overdrafts, a payment past due) and explain each flag in plain English.
- **Inputs:** certified views of covenants, deposits, payments and statement due dates; the rule set owned by credit risk.
- **Allowed actions:** read; write flags to the assistant's own list of flags.
- **Not allowed:** changing a borrower risk rating or a watchlist status; inventing flags outside the rule set; telling the borrower.
- **Outputs:** a list of flags per PM, each flag with the rule that fired and the numbers behind it.
- **Stops when:** every borrower is checked, or the data is older than [X] hours (it alerts the data owner and produces nothing).
- **Proof it worked:** a sample of flags matches the source numbers; flags acted on ≥ [X]%.
- **Starts when:** nightly.
- **Person in charge:** the PM decides what to do; credit risk owns the rules.
- **To confirm:** ⚠️ which team owns early warning rules; how a flag relates to the bank's own watchlist process.

**A10. Credit policy Q&A** · wave 3 · runs on a Copilot Studio agent or AWS Bedrock (Knowledge Bases)
- **Job:** answer PMs' and analysts' questions from the bank's credit policy, citing the section.
- **To confirm:** the full spec is written at sub-step 3.1, when feature wave 3 is scoped.

**A11. Industry background drafter** · wave 1 · runs on AWS Bedrock (Knowledge Bases over the approved industry sources) or a Copilot Studio agent
- **Job:** draft the industry background section of a credit memo: the borrower's industry, its size and trend, main drivers and risks, and outlook, from approved and licensed sources only, every statement cited and dated, for the PM to edit and approve. It uses no borrower data and writes no judgment about the borrower.
- **Inputs:** the industry (for example from the borrower's industry code); the approved industry source list (part of the data contract, K5). Never borrower financials or any other borrower data.
- **Allowed actions:** read the approved sources; create a draft section for the PM.
- **Not allowed:** reading or using borrower data; writing any judgment about the borrower; any statement without a source; sources not on the approved list; copying a licensed report beyond what its license allows (K14). Guardrails (K8) block borrower data and off-topic requests.
- **Outputs:** a draft section marked "AI draft", every statement with its source and date, and a list of anything the sources didn't cover.
- **Stops when:** the section is delivered, or the approved sources don't cover the industry or are older than [X] months (it says which and stops).
- **Proof it worked:** test-set score meets the quality bar (every statement cited and dated, facts match the source, usefulness graded by PMs); outside fees saved once the contract changes; share of sections kept with light edits [X].
- **Starts when:** a credit memo is started (a new request, renewal or line change), or the PM asks (B16).
- **Person in charge:** the PM edits, approves and owns the section; the content owner keeps the approved source list.
- **To confirm:** ⚠️ which sources the outside firm uses today and whether the bank already licenses industry data; each source's license terms; whether annual reviews carry an industry section too.

### Agents the team uses

The team uses the product machine's general agents, specified in full in the
[Agent Library](https://claude.ai/artifact/Cn9nANQoqp2BP7yrmy61zn); which ones each step uses is in section 4.

## Appendix B: Workflows

Each PM-facing capability as a step-by-step flow. Every PM-facing flow (B10–B14 and B16) has one
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
- **Steps:** 1. A8 drafts the memo's routine sections, restating the requested terms as written; the industry background section the PM approved in B16 goes in as written. 2. The number check runs. 3. **Decision point:** the PM writes the analysis and the recommendation (in wave 1 always written by the PM) and sends it to the credit officer through the bank's normal approval route.
- **Logged:** drafts, edits, time from request to submission.
- **Measures:** turnaround; hours per memo.

**B13. Early warning flags** (wave 2)
- **Trigger:** A9's nightly check finds a flag.
- **Steps:** 1. A9 explains it with the numbers. 2. The flag appears in the PM's early warning flags and in a weekly summary. 3. **Decision point:** the PM dismisses it (with a reason), watches it, or raises it through the bank's own process, telling the RM.
- **Logged:** flags, decisions, reasons, outcomes.
- **Measures:** flags acted on; how many weeks earlier than today's process (⚠️ to measure against the bank's watchlist).

**B14. Covenant and statement tracker** (wave 2)
- **Trigger:** a statement or compliance certificate due date, or a new spread.
- **Steps:** 1. Rules in code calculate each covenant test from the spread and list what's due or late. 2. **Decision point:** the PM confirms the result and decides any follow-up; reminders to the RM or borrower are drafted for the PM to send.
- **Logged:** tests, confirmations, reminders.
- **Measures:** late items; analyst hours saved.

**B16. Industry background draft** (wave 1)
- **Trigger:** a credit memo is started (a new request, renewal or line change), or the PM asks.
- **Steps:** 1. A11 takes the borrower's industry (for example from its industry code), and nothing else about the borrower. 2. It drafts the section from the approved industry sources only, every statement cited and dated. 3. **Decision point:** the PM edits and approves the section (K1), or rejects it with a reason. 4. The approved section goes into the memo (B12), and the PM submits the memo as usual. Nothing is submitted by the assistant.
- **Logged:** sections drafted, edits, approved or rejected, sources used.
- **Measures:** outside fees saved once the contract changes; turnaround (days from request to an approved section); share of each section kept with light edits.

Wave 3 workflows (credit policy Q&A, renewal radar, deal screening) are not written yet.

**B15. Every release (every week or two)**
- **Trigger:** any change to prompts, rules, templates, data or models.
- **Steps:** 1. M32 re-runs the test set, including every must-refuse case. 2. If the score is below the quality bar, the release stops. 3. If the change is material (Product Framework), it goes back through step 4, with the credit policy owner on the higher-risk path. 4. Release; M32 watches live quality for [X] days.
- **Logged:** test scores, approvals, release notes.
- **Measures:** quality trend; releases rolled back.

_Last updated: 2026-10-19_
