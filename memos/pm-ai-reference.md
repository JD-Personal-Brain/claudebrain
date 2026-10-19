# PM Detail

Everything about the portfolio manager (PM) work at Associated Bank in one document, for an AI to read. Give this whole document to an AI model so it has the full context: the product, the plan, every step, the agent specs, the workflows and the credit market research. People should read the three short pages for people above it in the PM section (the PM Executive Summary, The PM Assistant and the PM Assistant Plan), and can try the PM Assistant Prototype, the fourth row.

> **How to read it (for the AI).** The parts below are the working files, copied in whole and in this order. Later parts give more detail on earlier ones. Lines marked ⚠️ are guesses or hypotheses to confirm at the bank; [X] marks a number not yet known: never invent a value for it. The product is a working hypothesis until Discover with the bank's PMs. Built automatically from the working files; never edit this file by hand.

## Part 1: Executive summary

Working file: `memos/pm-executive-summary.md`.

For the leaders of the credit business · Associated Bank · October 2026

> ⚠️ **A working hypothesis** (first cut, 2026-10-19). Built from outside research and public Associated job postings, not yet from how the bank's portfolio managers (PMs) work today. The first conversations with credit leaders test it.

### The problem
PMs underwrite and monitor the bank's commercial loans, but we expect much of their time goes to gathering financials from many systems, re-typing numbers and writing the routine parts of annual reviews and credit memos. At DBS, where the bankers write their own credit memos, the bank estimates memos and related work take up to 40% of those bankers' time (DBS's estimate). ⚠️ How much of a PM's time they take here is a first question. Time spent assembling a review is time not spent judging the credit or watching for trouble.

### The product: The PM Assistant
Each PM gets **their own AI assistant**, inside the tools we expect they already use (Word, Teams and the loan system; ⚠️ to confirm). It gathers the borrower's file, drafts the routine sections of reviews and memos with a source on every number, and later flags borrowers whose signals are weakening. **The PM always writes the judgment, and a named credit officer decides.** It never sets a risk rating, never approves or declines credit and never sets a price. [What it is and all its capabilities](https://claude.ai/artifact/BrBLWQzQggQPtqCgLLGf3C).

### What PMs get first (wave 1)
| Capability | What the PM gets | Why it matters |
|---|---|---|
| **Borrower file** | Everything about one borrower in one place: financials and their trend, loans, covenants, deposits, payments, the last review and the RM's notes, every figure with its source, and a list of what's missing or late | Hours of gathering back on every review; goes live first |
| **Annual review and credit memo drafts** | The routine sections drafted in the bank's template from the borrower file; the risk rating and recommendation left blank for the PM | Faster reviews and faster answers to RMs and clients |

**See it working:** the [PM Assistant Prototype](https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE) runs its agents on sample borrowers, with a short tour.

Later waves add early warning flags and a covenant and statement tracker, then credit policy Q&A, a renewal radar and deal screening.

### The value
- **More PM time for judgment:** hours saved on each annual review and credit memo. DBS targets at least 30% less time; Moody's says its agents write about 35–40% of each memo at a tier-one US bank (outside figures, not our targets).
- **Faster answers:** fewer days from a complete request to a decision.
- **Earlier sight of trouble (wave 2):** flags acted on, and how early they came.
- Time is proven against similar PMs not yet using it; targets are set from the bank's own numbers. [Outside evidence for each credit core use case](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X#portfolio-managers)

### How fast
The build takes days. What sets the pace is approval: drafts inform credit decisions, so they take the bank's deeper review, including the credit policy owner's sign-off. On our first estimates, to confirm, that's the borrower file by about week 7 and the drafts by about week 12. [The plan, week by week](https://claude.ai/artifact/UKMBCCxBns8YuCJyEo4Zkv)

**What could slow us down:** not known yet. Possible hold-ups include approval to use borrower data and the deeper credit review. If the review runs long, the borrower file still goes first, because it gathers and cites but writes no judgment; if data approval runs long, the prototype keeps running on sample borrowers until it lands.

### What I need, and what I'd confirm
1. A sponsor for the PM work: about an hour a week, plus each go/no-go decision (our estimate).
2. Time with 4–6 PMs and credit analysts, shadowing a real annual review in the first three weeks (our estimate), and a willing pilot group.
3. The credit policy owner, early: what a draft may contain, and their sign-off.
4. Named owners for borrower data and the credit file, and the review and memo templates.

To confirm in the first weeks: what usually holds up a new AI tool here; how many reviews and memos PMs write a year and how long each takes; which loan system and spreading tool the bank uses; and whether a draft may carry a recommendation.

## Part 2: The product: The PM Assistant (short version for people)

Working file: `memos/pm-assistant.md`.

> ⚠️ **A working hypothesis** (first cut, 2026-10-19), built from outside research and public Associated job postings. The first interviews with the leaders of portfolio managers (PMs) and with PMs confirm or change it.

### The product in one line
Each PM gets **their own AI assistant**, inside the tools we expect they use (Word, Teams, the loan system and the bank's data; ⚠️ to confirm), to take the gathering and routine writing off their plate, so their time goes to credit judgment, and to spot weakening borrowers sooner. It starts with two **capabilities** and gains more, feature wave by feature wave. Every later AI product for PMs is a new capability of the same assistant.

### 1. Its limits
These limits make it safe to give every PM one.
- **Jobs:** only the capabilities below. Anything else, it says so and stops.
- **Workflows (where it works):** Word from the bank's templates, Teams and the loan system (⚠️ to confirm). No new app.
- **Data:** borrower data the bank has approved as trusted (certified) and the credit file's documents, only for the borrowers the PM may already see.
- **Controls:** it gathers, drafts and flags; the PM writes the judgment and submits. It never sets or suggests a risk rating, never approves or declines credit and never sets a price. Every draft names the credit officer who decides. Everything is logged.
- **Feedback:** one click on every output (use, change or reject), which steers what gets better next.

### 2. Capabilities, by moment in the PM's work
Each capability is one AI product and answers one credit core use case (the pairing with the RM core use cases is our proposal, to agree; see the [Use Case Library](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X#portfolio-managers) for the value and the research).

| Moment | Capability | What it does | Credit core use case | Wave |
|---|---|---|---|---|
| **Review and renew** | Borrower file | Everything about one borrower in one place, every figure with its source, and what's missing or late | Credit memo and annual review drafts | 1 |
| | Annual review and credit memo drafts | The routine sections drafted in the bank's template; the risk rating and recommendation left for the PM | Credit memo and annual review drafts | 1 |
| | Renewal radar | Loans coming up for renewal, and borrowers whose results suggest a different line | Renewals and line changes | 3 |
| **Watch the portfolio** | Early warning flags | Flags borrowers whose signals are weakening, with the numbers | Early warning on credit quality | 2 |
| | Covenant and statement tracker | Covenant tests, and statements and certificates due or late | Spreading, document intake and covenant tracking | 2 |
| **New requests** | Deal screening | A quick check that a request fits the bank's credit appetite | Deal screening | 3 |
| **Know the policy** | Credit policy Q&A | Answers from the credit policy, citing the section | Credit policy Q&A and coaching | 3 |
| **Left out on purpose** | Risk rating support; approve or decline; pricing | Kept out because they are the credit decision itself | Risk rating support | Out |

### 3. What it's built on
Every capability runs on one shared foundation, built once:
- borrower data: loans, covenants, deposits and payments (⚠️ where they live is to confirm);
- the credit file: financial statements, the spread (the borrower's statements entered in the bank's standard format), prior reviews and other documents, read with the page cited;
- the bank's review and memo templates and its credit policy;
- a **signals engine**: simple, explainable rules agreed with credit risk, with AI explaining each flag in plain English;
- drafting, with every number checked against its source, and the controls and feedback above.

Every detail (the PM's job, the foundation part by part, what to confirm) is in [PM Detail](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg), for AI to read. To see the assistant working, try the [PM Assistant Prototype](https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE).

## Part 3: The PM Assistant in full detail

Working file: `memos/pm-assistant-detail.md`.

The detailed working file behind The PM Assistant page. People read the short page (`memos/pm-assistant.md`); this file goes into PM Detail.

> ⚠️ **A hypothesis, not a plan yet** (first cut, 2026-10-19). Built from our commercial credit research, the Use Case Library and public Associated job postings, not from how the bank's portfolio managers work today. The first conversations with credit leaders test it; Discover confirms or changes the rest.

### The product in one line
Each portfolio manager (PM) gets **their own AI assistant**, inside the tools we expect the PM already uses (Word, Teams, the loan system and the bank's data; ⚠️ to confirm). Its job is to take the gathering and routine writing off the PM's plate, so the PM's time goes to credit judgment, and to spot weakening borrowers sooner. It starts with two **capabilities**, each doing one specific job in the PM's work, and gains more feature wave by feature wave. Every later AI product for PMs is a new capability of the same assistant.

### 1. A personal AI, with limits
The assistant is personal to each PM, and it is constrained in five ways. These limits are what make it safe to give every PM one.

| Limit | What it means |
|---|---|
| **Jobs** | It does only the capabilities listed on this page. Anything else, it says so and stops. |
| **Workflows** | It works where we expect the PM already works (to confirm in Discover): Word from the bank's templates, Teams, the loan system. No new app to learn. |
| **Data** | Certified borrower data only (financials, loans, covenants, deposits, payments), the credit file's documents and the RM's approved notes, always limited to the borrowers the PM may already see. |
| **Controls** | It gathers, drafts and flags; the PM writes the judgment and submits. It never sets or suggests a risk rating, never approves or declines credit, never sets a price, and writes a recommendation only if the credit policy owner allows it. Every draft names the credit officer who decides. Everything is logged. |
| **Feedback** | Every output has one-click feedback (use, change or reject, with a reason). The feedback steers what gets better next. |

### 2. What a PM's job is
From Associated's public PM postings (seen through search results on job boards, 2026-10-14; ⚠️ check against the bank's own careers site):

| Part of the job | What it means | Where the assistant helps |
|---|---|---|
| **Underwrite new credit** | Analyze a borrower's financials and write the credit memo for a new loan, renewal or line change | Borrower file, credit memo draft |
| **Review the portfolio** | Annual reviews of each borrower: financial performance, covenants, collateral, risk rating | Borrower file, annual review draft |
| **Monitor credit quality** | Watch for weakening borrowers; track statements, compliance certificates and covenants | Early warning flags, covenant and statement tracker |
| **Partner with RMs** | Work closely with the RM on each relationship and each request | Faster drafts mean faster answers for the RM |
| **Know the policy** | Apply the bank's credit policy and procedures | Credit policy Q&A |

### 3. Capabilities, by moment in the PM's work
Each capability is one AI product (glossary) and answers one credit core use case, the credit counterpart of an RM core use case (the Use Case Library's portfolio manager section; the pairing is our proposal, to agree).

| Moment | Capability | What it does | Credit core use case | Wave |
|---|---|---|---|---|
| **Review and renew** | Borrower file | Everything about one borrower in one place, every figure with its source, and what's missing or late | Credit memo and annual review drafts | 1 |
| | Annual review and credit memo drafts | The routine sections drafted in the bank's template; the rating and recommendation left for the PM | Credit memo and annual review drafts | 1 |
| | Renewal radar | Loans coming up for renewal, and borrowers whose results suggest a bigger or smaller line | Renewals and line changes | 3 |
| **Watch the portfolio** | Early warning flags | Flags borrowers whose signals are weakening, with the numbers | Early warning on credit quality | 2 |
| | Covenant and statement tracker | Covenant tests from the spread, and statements and certificates due or late | Spreading, document intake and covenant tracking | 2 |
| **New requests** | Deal screening | A quick check that a request fits the bank's credit appetite before the RM pitches | Deal screening | 3 |
| **Know the policy** | Credit policy Q&A | Answers from the bank's credit policy, citing the section | Credit policy Q&A and coaching | 3 |
| **Left out on purpose** | Risk rating support; approve or decline; pricing | Closest to the credit decision; kept out under control K3 | Risk rating support | Out |

**Wave 1 at a glance:** two capabilities that work as one flow: the borrower file, then the draft built from it. Together they cover the PM's most frequent writing job, the annual review, and the credit memo for a request. The order follows the agreed credit order (closed item C33): memo and review drafts first, early warning second, risk ratings out of the first waves.

**How each capability is built.** Our measures' targets are set in Define; outside figures are benchmarks in the Use Case Library, never our targets.

| Wave | Capability (AI product) | Credit core use case | Agents | Built mainly on | Our measure (target set in Define) |
|---|---|---|---|---|---|
| **Wave 1** (borrower file by about week 7; drafts by about week 12; each once its approvals are in) | Borrower file | Credit memo and annual review drafts | A7 | Snowflake, AWS Bedrock (Knowledge Bases) | Hours spent gathering per review [X] |
| | Annual review and credit memo drafts (higher-risk path) | Credit memo and annual review drafts | A7, A8 | AWS Bedrock or Copilot Studio; Word templates | Hours per review; share of sections used with light edits [X] |
| **Wave 2** (dates proposed at gate 2) | Early warning flags (higher-risk path) | Early warning on credit quality | A9 | Snowflake signals, Teams | Flags acted on; how much earlier than today [X] |
| | Covenant and statement tracker | Spreading, document intake and covenant tracking | Rules in code (workflow B14) | Snowflake, the spreading tool (⚠️ to confirm) | Late items; analyst hours saved [X] |
| **Wave 3** (dates proposed at gate 2) | Credit policy Q&A | Credit policy Q&A and coaching | A10 | Copilot Studio or Bedrock Knowledge Bases | Questions answered; answer ratings [X] |
| | Renewal radar; deal screening | Renewals and line changes; deal screening | Specs to come | Snowflake, the loan system | Renewals on time; screening turnaround [X] |

**Why the borrower file is its own capability (our call, 2026-10-19):** it gathers and cites but writes no judgment, so we assume it needs the least review (⚠️ the risk partner decides) and can go live first if the higher-risk review of the drafts runs long. It also saves PMs time on its own.

**Why the judgment sections stay blank:** the risk rating and the recommendation are where the credit decision lives. Leaving them to the PM keeps the AI on the right side of control K3 and keeps the PM accountable. Whether a draft may carry a recommendation at all is the credit policy owner's call at sub-step 2.4.

**Why early warning is wave 2:** it is where most banks are working (the Use Case Library), but it needs agreed rules from credit risk and its own fairness check, and it touches the bank's own watchlist process, which we don't know yet. We call ours "early warning flags" so they are never mistaken for the bank's watchlist.

### 4. The foundation underneath
Built once and shared by every capability.

| Part | What it is | Used by |
|---|---|---|
| **Borrower data** | Loans, covenants, deposits and payments, which we expect in Snowflake (⚠️ or Fabric; certified data only) | Every capability |
| **The credit file** | Financial statements, the spread (the statements in the bank's standard format), prior reviews, appraisals and other documents (⚠️ where they live is to confirm), read with their page cited | Borrower file, drafts |
| **The bank's templates and policy** | The annual review and credit memo templates; the credit policy | Drafts, policy Q&A |
| **Signals engine** | Simple, explainable rules agreed with credit risk; AI explains each flag with the numbers | Early warning, covenant tracker, renewal radar |
| **Drafting** | Drafts marked as AI drafts, with every number checked against its source in code | Drafts |
| **Controls and logs** | The limits in section 1, built once and tested for every capability | Every capability |
| **Feedback loop** | One-click feedback on every output, sorted and fed into the next release | Every capability |

### 5. How we'll know it works
- **More PM time for judgment:** hours per annual review and credit memo, against PMs not yet using it [X].
- **Faster answers:** days from a complete request to a decision [X].
- **Earlier sight of trouble:** flags acted on, and how early (wave 2) [X].
- **Use:** PMs using it every week, and the share of drafts used with light edits [X].

Targets are [X] until the bank's own numbers are in.

### 6. Working with the RM side
The PM and the RM work each relationship together. The RM Assistant's approved call notes are one input to the borrower file, and early warning on credit quality shares its signals engine with the RM side's "client may leave" early warning, while each flag goes only to its own user group. A credit request draft from the RM (an idea on the RM side, not decided) would be where the two assistants meet. These links are notes for the detail document; each group's pages stand on their own.

### 7. What to confirm
The one full list is in the full plan, section 8 ("What I'd confirm in the first weeks").

### 8. How it maps to the agents
The core use cases, in their credit counterparts, are the **needs** the capabilities answer, and each capability is one AI product. The product agents do the work: A7 builds the borrower file; A8 drafts reviews and memos; A9 watches for early warning signs (the **signals engine**); A10 answers credit policy questions (wave 3). The covenant tracker is rules in code inside workflow B14, not an agent.

## Part 4: The plan (short version for people)

Working file: `memos/pm-plan.md`.

How The PM Assistant gets delivered to portfolio managers (PMs) · Associated Bank · October 2026

[PM Executive Summary](https://claude.ai/artifact/Cvw3mkUohNFLwVr4H2wURd) · [The PM Assistant](https://claude.ai/artifact/BrBLWQzQggQPtqCgLLGf3C) · [PM Assistant Prototype](https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE) (see it working) · [PM Detail](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg) (everything in full) · [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ) (the rules every product follows)

### The plan at a glance
The first 13 weeks (about 90 days), as estimates to confirm in the first days. Each live bar starts only once its borrower data is approved and the bank's review signs it off, so the bars move with those approvals. Week 1 starts at kickoff. Gates (◆) are go/no-go decisions; the data contract is the signed list of borrower data the assistant may use. Each row links to its detail in PM Detail.

```gantt
weeks 13
Kickoff and a working prototype on sample borrowers | 0 | 1 | build | https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE
Gate 1: target, measure and first baseline agreed | 1 | 1 | gate | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-4-how-the-work-flows
Shadowing PMs through real reviews, giving the final baseline | 0 | 3 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Borrower file and drafts built on sample borrowers | 0 | 4 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Gate 2: borrower data approved, higher-risk path set, business case agreed | 4 | 4 | gate | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-4-how-the-work-flows
Borrower file: tested on real data and signed off | 4 | 6 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
**Borrower file live** | 6 | 13 | live | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Review and memo drafts: tested on real past reviews | 4 | 9 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Higher-risk review and sign-offs, including the credit policy owner | 9 | 11 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
**Review and memo drafts live** | 11 | 13 | live | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Small releases every week or two | 7 | 13 | ongoing | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
```

No real borrower data is used before gate 2. The borrower file can move first because it gathers and cites but writes no judgment (our assumption, to confirm: it needs less review). The drafts inform credit decisions, so they take the deeper review the bank's process calls the higher-risk path: a fairness check, tests that it refuses a rating, a decision or a price, and the credit policy owner's sign-off. The risk partner and the credit policy owner see each version as it's built. Waves 2 and 3 get proposed dates at gate 2.

### 1. What could slow us down (to confirm)
The real blockers aren't known yet; they're a first question for the bank. Possible ones:
- **Approval to use borrower data and credit files.** Nothing reaches pilot PMs on real data until the people responsible for it approve which data the assistant may use.
- **The deeper review for credit drafts.** Nothing goes live until risk, compliance, privacy, security and the credit policy owner sign off. To keep that short, they review each version as it's built.
- **Backup plan.** If data approval runs long, the prototype keeps running on sample borrowers and the dates are reset at gate 2. If the risk partner puts the borrower file on the higher-risk path too, it goes live with the drafts at about week 12. If the deeper review of the drafts runs long, the borrower file stays live and the version under review stays frozen; improvements ship after sign-off. The call is made at gate 2.

Detail: [the backup plan and how we move fast](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate).

### 2. Who decides
| Role | For the PM project |
|---|---|
| Sponsor | A credit or commercial banking leader [name needed]: the outcome, funding and every gate |
| User leaders | PM team leaders and credit managers: choose the pilot group, use the early warning flags in a portfolio review they already run (⚠️ to confirm), and decide with the sponsor whether to scale |
| Pilot PMs and analysts | Co-design and test, and grade the drafts; their feedback steers what gets built |
| Credit policy owner | What a draft may contain, and a sign-off before drafts reach PMs [name needed] |
| Credit officer | Makes every credit decision a draft informs; named on every draft |
| Data owners | Borrower data and credit files (⚠️ which systems is to confirm) [names needed]: sign the data contract, with the credit file's content owner signing the list of documents |
| Risk partner | Rates the product's risk and approves it before it reaches PMs; the sponsor can't overrule that approval |
| Compliance, privacy and security | Sign off before it reaches PMs; compliance runs the fairness check |
| Finance | Agrees how hours saved are valued, and joins the sponsor for the quarterly call to invest more, adjust or stop |

Detail: [who's involved and who decides](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-3-who-s-involved-and-who-decides).

### 3. How we'll prove the value
- **Time:** hours per annual review and credit memo, against similar PMs not yet using it, by a method Finance agrees before the pilot.
- **Speed:** days from a complete request to a decision, judged once enough requests have gone through.
- **Quality:** every number in a draft matches its source; the share of sections PMs keep with light edits.
- **Use:** pilot PMs using it each week.
- **Payback:** the target is set at gate 2 from the bank's own numbers, as are all the other targets. Loan losses avoided are tracked, not counted, until Finance and credit risk agree a method.

Detail: [the value model](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-2-the-value-model).

### 4. Top risks
| Risk | How I'd handle it |
|---|---|
| A wrong number in a credit draft | Every number traced to its source and checked before the PM sees it; zero tolerance in testing |
| The AI drifts into the credit decision | It never writes the rating or the recommendation; tests that it refuses; the credit officer named on every draft |
| Approval to use borrower data takes longer | Request it on day one; keep the prototype running on sample borrowers |
| The deeper review takes longer | Brief the credit policy owner in week one; the borrower file goes first (section 1) |
| Documents are scanned, messy or in many systems (⚠️ to confirm) | Start with documents already in a standard form; the file lists what's missing instead of guessing |
| PMs don't trust the drafts | A source on every figure; built with pilot PMs on their own past reviews |

Detail: [every risk and how I'd handle it](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-7-top-risks-and-how-i-d-handle-them).

## Part 5: The full delivery plan, with every step, agent spec and workflow

Working file: `memos/pm-assistant-framework.md`.

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
the data owners [names needed]; aimed for weeks 2 to 4), and the higher-risk review. Credit
memo and annual review drafts inform a credit decision, so the wave 1 drafts take the
higher-risk path (control K3): a fairness check, must-refuse tests and the credit
policy owner's sign-off as well as the usual ones.

---

### 1. The outcome

The assistant has two goals that work together:

- **More PM time for judgment ("banker capacity"):** less time gathering financials, re-typing numbers and writing the routine parts of annual reviews and credit memos.
- **Earlier sight of credit trouble:** spotting a weakening borrower sooner, so the PM and RM can act while there are still options.

The return comes from three places. Finding out which is biggest is the first job:

| Lever | What the assistant does | Capabilities |
|---|---|---|
| **Save time on each review** | Gathers the borrower's file and drafts the routine sections of the annual review or credit memo, with a source on every number | Borrower file, review and memo drafts |
| **Faster answers for RMs and clients** | Shorter time from a credit request to a decision, because the first draft is ready sooner | Review and memo drafts, deal screening |
| **Fewer surprises in the portfolio** | Flags borrowers whose signals are weakening (late statements, a covenant near its limit, falling deposits) | Early warning flags, covenant and statement tracker |

---

### 2. The value model

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

### 3. Who's involved and who decides

The roles, what each one decides and the gates each joins are set once in the
[Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ). For the PM project they are:

| Role (Product Framework) | For the PM project |
|---|---|
| Sponsor | A credit or commercial banking leader [name needed] ⚠️ (whether credit or the business sponsors it is a first question) |
| User leaders | PM team leaders and credit managers: they choose the pilot group, decide with the sponsor whether to scale (gate 5), and use the early warning flags in a portfolio review they already run (⚠️ to confirm) |
| Pilot users | Pilot PMs and credit analysts: they co-design and test, and grade the test set |
| Credit policy owner | What a draft may contain (for example, whether it may carry a recommendation), the must-refuse cases, and a sign-off at step 4 (higher-risk path, control K3) [name needed] |
| Credit officer | Makes every credit decision a draft or flag informs; named on every draft (K3) ⚠️ (may be the PM or a credit approver; to map) |
| Data owners | The owners of borrower financials, loan and covenant data and credit files (⚠️ which systems hold them is to confirm) [names needed] |
| Content owner of the credit file | Signs the list of documents the assistant may read (statements, tax returns, appraisals, prior reviews; sub-step 2.3), for example credit administration [name needed] |
| Platform teams | Microsoft, AWS, data engineering and the loan system's team (⚠️ which loan system the bank uses is not yet known) |
| Long-term owner | To be decided by a date set in Define (sub-step 2.8); confirmed before scaling (5.7); for example, someone in credit administration |
| Also for PMs: credit risk review | Whether early warning flags change how loans are watched, and how a flag relates to the bank's own watchlist process (⚠️ to confirm); from wave 2, owns the early warning rules and signs them at 4.7 |

The risk partner, compliance, privacy and security (who sign off at step 4), vendor
risk, IT, Finance, Analytics and Operations join as the Product Framework sets out;
the risk partner's step 4 approval can't be overruled by the sponsor. **The review and memo drafts take
the higher-risk path**, so the credit policy owner joins at 2.4 and signs at 4.7, and
compliance runs the fairness check (4.4). We assume the borrower file does not, because
it gathers and cites but drafts nothing (⚠️ the risk partner decides at 2.4).

**Keeping partners aligned.** Decisions go in the decision log, and dependencies,
risks and issues in the risk and issue list (Product Framework). Its top item is the
limiting factor, named with its owner once the bank confirms what is actually
holding the work up (⚠️ not known yet).

---

### 4. How the work flows

Six steps, each ending in a go/no-go gate, run as the [Product Workflow](https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv)
sets out: its questions, gates and sub-steps aren't repeated here. The first pass overlaps:
a working prototype in week 1, the borrower file live in about week 7 and the drafts
in about week 12 (later than for RMs, because of the higher-risk path); then steps 3–6
repeat in cycles of a week or two, and each new feature wave takes the quick pass through
Discover and Define. What's different for PMs:

| Step | Gate for PMs | What's specific to PMs | General agents used (M20 to M33; M1 to M19 run every step as the Product Machine sets out) |
|---|---|---|---|
| **1. Discover** | The sponsor, with the risk partner, agrees the target lever, the main measure (hours per review is our first guess) and today's baseline (provisional; confirmed at gate 2), and confirms wave 1 | Count reviews and memos per PM per year and time each part (gathering, spreading, writing, approvals); interview and shadow PMs and credit analysts through one real annual review, starting from the PM user workflow; collect the bank's review and memo templates; learn how PMs are measured; test the prototype on sample borrowers every few days | M20 interview synthesizer, M21 opportunity sizer, M22 time-use analyst |
| **2. Define** | The brief, data contract and risk rating agreed (higher-risk path set); the credit policy owner agrees what drafts may contain; the value model shows payback within [X] months | The data contract covers documents (financial statements, tax returns, appraisals, prior reviews: their source, owner and who may see them) and the bank's approval-authority list; the risk intake marks the drafts for the higher-risk path (K3) and lists the must-refuse cases (a risk rating, approve or decline, a price, a recommendation if the policy owner says no); Finance agrees how hours are valued | M23 requirements drafter, M24 data contract checker, M25 risk intake assistant |
| **3. Build** | Meets the quality bar in testing; every control is built and passes its control test | Every number in a draft traces to a source document or system (K7) and is checked in code; the "judgment" sections (risk rating, recommendation) are left for the PM, clearly marked; each PM sees only borrowers they may already see (K4); the test set uses real past reviews graded by experienced PMs, with must-refuse cases | M26 test grader |
| **4. Govern and test** | All sign-offs recorded, including the credit policy owner's, and the monitoring plan agreed | Register the product in the model inventory (⚠️ to confirm) and confirm its rating (SR 11-7; ⚠️ SR 26-2 may replace it, item W17); red-team for a credit decision, a rating, a price and other PMs' borrowers; fairness check, with the groups set by compliance (4.4; are drafts equally complete and accurate across borrower types and sizes? is our first proposal ⚠️); every draft names the credit officer who decides, from the bank's approval-authority list | M27 red-team agent, M28 fairness monitor, M29 evidence pack assembler |
| **5. Release and adopt** | Weekly use and leading results hit targets (at least [X]% of pilot PMs using the assistant weekly; at least [X]% of draft sections kept with light edits); no serious incidents; long-term owner confirmed before scaling. Hours per review and turnaround are judged in step 6, once enough reviews are done | A pilot group of PMs, with a comparison group; build it into the annual review cycle and the portfolio review managers already run (⚠️ to confirm); train on PMs' own borrowers; champions answer "how do I…?" | M30 feedback triage |
| **6. Measure and iterate** | Each month, keep, change or stop each AI product; each quarter, the sponsor with Finance decides to invest more, adjust or stop | Leading measures first (drafts used, hours per review, turnaround), visible within weeks; early warning judged on flags acted on and how early they came, not on losses avoided until Finance and credit risk agree a method | M31 impact analyst, M32 quality watchdog, M33 improvement scout |

---

### 5. How we deploy AI

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

### 6. The project plan (estimate)

Building starts on day one, on sample borrowers. The plan is organized around what most
often holds banks up (our assumption for Associated, to confirm): access to borrower data
and the higher-risk review. The risk partner and the credit policy owner see each version
as it is built. No real borrower data, past reviews included, is used before gate 2.

**What lets us move this fast.** The same six conditions as every product (build from day
one, standard features, low risk by design, review as we go, data access on day one, fast
decisions), with one change: the drafts are **not** low risk by design, because they inform
credit decisions. What keeps them moving is that the AI never writes the judgment: the
rating and the recommendation stay with the PM.

**The backup plan, for three things that could run long** (the call is made at gate 2):
- **Approval to use borrower data.** Everything waits for it; the prototype keeps running on sample borrowers with pilot PMs, and the live dates are reset at gate 2.
- **The borrower file is put on the higher-risk path too** (the risk partner's call at 2.4). Then it goes through step 4 with the drafts and both go live together, at about week 12.
- **The higher-risk review of the drafts.** The borrower file stays live on its own. The version under review is frozen; improvements wait in the backlog and ship after sign-off through the release routine (B15), and any material change goes back through step 4.

**Wave 1: the first 13 weeks**

| Week | What gets done | Owner | Proof it's done |
|---|---|---|---|
| Days 1–5 | Sponsor kickoff; risk partner and credit policy owner briefed; data access and test environments requested; vendor risk asked whether AWS Bedrock and the model provider are approved for borrower data; IT asked to approve each connection (2.2); working prototype on sample borrowers; the review templates collected; a first count of reviews per PM, from credit administration's review calendar if one exists (⚠️ to confirm) | Product manager, platform team | Prototype shown to the sponsor |
| 1 | **Gate 1:** target lever, main measure and provisional baseline agreed; wave 1 confirmed | Sponsor, with the risk partner | Decision log entry |
| 1–3 | Shadow 4–6 PMs and analysts through a real review (our estimate); time each part, which gives the final baseline; improve the prototype every few days | Product manager, pilot PMs, analyst | Time map; feedback log |
| 1–4 | Borrower file and drafts built and tested on sample borrowers | Platform team | Prototype test results |
| About 4 | **Gate 2:** final baseline, data contract, early risk rating (which capabilities take the higher-risk path), what drafts may contain (credit policy owner), measures and value model. Aimed for weeks 2 to 4, paced by the data owners' signatures (⚠️) | Sponsor, data owners, content owner of the credit file, risk partner, credit policy owner | Signed data contract; decision log |
| 4–6 | Borrower file on real data: test set, controls tested, frozen version, sign-offs | Platform team, risk partner | Gate 3 and 4 entries |
| About 7 | **Borrower file live with pilot PMs** | Product manager | First weekly usage report |
| 4–9 | Review and memo drafts on real past reviews; test set graded by PMs, with must-refuse cases; fairness check agreed with compliance; evidence pack | Platform teams, product manager, compliance | Test results against the quality bar |
| 9–11 | Higher-risk review of the frozen drafts: sign-offs, including the credit policy owner's; readiness (training, incident process, comparison group) | Risk, compliance, privacy, security, credit policy owner | Sign-offs recorded |
| About 12 | **Annual review and credit memo drafts live with pilot PMs** | Product manager | Drafts used; sections kept with light edits |

**By day 90 (about week 13):** the borrower file has been live for about six weeks and the
drafts for about one or two; the first leading measures are coming in. Waves 2 and 3 get
dates at gate 2.

---

### 7. Top risks and how I'd handle them

| Risk | How I'd handle it |
|---|---|
| **A wrong number in a credit draft** | Every number traced to its source and checked in code before the PM sees the draft; zero tolerance in the test set; drafts marked as drafts |
| **The AI drifts into the credit decision** | It never writes the rating or the recommendation; must-refuse tests; guardrails; the credit officer named on every draft (K3) |
| **Approval to use borrower data takes longer** | Request it on day one; keep the prototype running on sample borrowers; the data contract is aimed at weeks 2 to 4 |
| **The higher-risk review takes longer** | Brief the credit policy owner in week one; the borrower file goes first (backup plan) |
| **Documents are scanned, messy or spread across systems** (⚠️ to confirm) | Start with the documents already in a standard form; the borrower file shows what's missing instead of guessing (K25) |
| **PMs don't trust the drafts** | A source on every figure; build it with pilot PMs on their own past reviews; PMs edit freely |
| **Uneven quality across borrower types** | The fairness check compares draft accuracy and completeness across borrower types and sizes |
| **Early warning floods PMs with flags** | Few, explainable rules agreed with credit risk; every flag shows its numbers; measure flags acted on and tune |

---

### 8. What I'd confirm in the first weeks

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
- Which PM teams would make a good pilot group? Is the new franchise banking team, where RMs and PMs sit together, a good first one (B4)?
- How are PMs measured, and what team and budget does the pilot have?

---

### Appendix A: Agent specs

The product's own agents. PM agents are numbered on from the RM ones (A7 onward) so no
number means two things. **[X]** values are set in Define.

**Rules for every agent:**
- **One job.** If a request falls outside it, the agent says so and stops.
- **Read-only by default.** Any change to a record needs a named person's click.
- **Approved models and data only.** Uses only AI models and data sources approved for this product.
- **Never guesses.** If its inputs are missing, stale or fail a check, it stops and says what's missing (K25).
- **Never decides credit.** It never sets or suggests a risk rating, never approves or declines, never sets a price, and writes a recommendation only if the credit policy owner allows it (K3).
- **Everything logged.** Each run records who, what, when, which sources and what it produced.

#### Agents PMs use (the product)

**A7. Borrower file builder** · wave 1 · runs on Snowflake and AWS Bedrock (Knowledge Bases)
- **Job:** pull everything about one borrower into one file: the financials and their trend, loans and their terms, covenants and their latest tests, deposits and payment history, the last review and the RM's recent notes; list what's missing or late. (Public news about the borrower would be a later addition, through the data contract and a vendor review.)
- **Inputs:** certified views of loans, covenants, deposits and payments; the spread of the financial statements; the credit file documents; the RM's approved call notes, if the bank's RM tools hold them (optional; the file works without them) (⚠️ which systems hold each is to confirm).
- **Allowed actions:** read the inputs; write the file to the assistant's own workspace.
- **Not allowed:** changing any record; filling a gap with an estimate; reading borrowers outside the PM's permissions.
- **Outputs:** one borrower file, every figure with its source (document and page, or system and date), and a "missing or late" list.
- **Stops when:** the file is built, or a required input is missing or older than [X] days (it says which and stops).
- **Proof it worked:** a sample of files matches the source systems exactly; missing items are listed, never filled.
- **Person in charge:** the PM; the data owners for the inputs.

**A8. Review and memo drafter** · wave 1 · runs on AWS Bedrock or a Copilot Studio agent · higher-risk path (K3)
- **Job:** draft the routine sections of an annual review or a credit memo in the bank's template, from A7's file: the borrower, the relationship, financial performance, covenant compliance, collateral facts and the risks the numbers show.
- **Inputs:** the borrower file from A7; the bank's template; the bank's approval-authority list (who decides what, to name the credit officer); for a credit memo, the request as the RM or PM wrote it.
- **Allowed actions:** read the inputs; create a draft for the PM.
- **Not allowed:** writing a risk rating, an approve or decline, or a price; writing a recommendation unless the credit policy owner allows it; stating any number not in the borrower file.
- **Outputs:** a draft marked "AI draft" with the judgment sections left blank for the PM, every figure linked to its source, and the credit officer who decides named at the top.
- **Stops when:** the draft is delivered, or the file has a gap a section needs (it marks the section "needs input" and stops there).
- **Proof it worked:** test-set score meets the quality bar (accuracy zero tolerance, sources, usefulness graded by PMs); every must-refuse case refused.
- **Person in charge:** the PM writes the judgment and owns the final document; the credit officer decides.

**A9. Early warning watcher** · wave 2 · runs on Snowflake (Cortex) · higher-risk path (K3)
- **Job:** each night, check each PM's borrowers against the agreed early warning rules (for example: financial statements late, a covenant within [X]% of its limit or breached, deposits down [X]%, overdrafts, a payment past due) and explain each flag in plain English.
- **Inputs:** certified views of covenants, deposits, payments and statement due dates; the rule set owned by credit risk.
- **Allowed actions:** read; write flags to the assistant's own list of flags.
- **Not allowed:** changing a risk rating or a watchlist status; inventing flags outside the rule set; telling the borrower.
- **Outputs:** a list of flags per PM, each flag with the rule that fired and the numbers behind it.
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

#### Agents the team uses

The team uses the product machine's general agents, specified in full in the
[Agent Library](https://claude.ai/artifact/Cn9nANQoqp2BP7yrmy61zn); which ones each step uses is in section 4.

### Appendix B: Workflows

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

Wave 3 workflows (credit policy Q&A, renewal radar, deal screening) are not written yet.

**B15. Every release (every week or two)**
- **Trigger:** any change to prompts, rules, templates, data or models.
- **Steps:** 1. M32 re-runs the test set, including every must-refuse case. 2. If the score is below the quality bar, the release stops. 3. If the change is material (Product Framework), it goes back through step 4, with the credit policy owner. 4. Release; M32 watches live quality for [X] days.
- **Logged:** test scores, approvals, release notes.
- **Measures:** quality trend; releases rolled back.

## Part 6: Core use cases and outside research

Working file: `memos/use-case-library.md`.


**The need in one line:** PMs are the bank's credit people paired with RMs. The value is in drafting credit memos and reviews and in monitoring credit quality, with a person always deciding. At DBS, credit memos and related work take up to 40% of an RM's time (DBS's estimate); ⚠️ how much of a PM's time goes to them here is to confirm.

> ⚠️ **A proposal, not yet agreed.** Each RM core use case has a credit counterpart; the pairing is our own. Built from a web scan on 2026-10-13 through search summaries; the primary pages would not open.

| Core use case (credit counterpart) | Where the value is | Outside evidence | Strength |
|---|---|---|---|
| **Credit memo and annual review drafts** (account intelligence) | A review-ready first draft from many systems, with sources | DBS: live for about 1,500 bankers (August 2026), targets at least 30% less time. Moody's: writes about 35–40% of each memo at a tier-one US bank. nCino, S&P and Microsoft all offer it | **Strongest.** First in our order |
| **Early warning on credit quality** (keep clients) | Spotting a weakening borrower early | Nearly 60% of credit risk leaders are pursuing it, more than any other area (McKinsey survey of 24 institutions). Moody's live across 19 countries at a large Asian bank | **Strong.** Second in our order |
| **Spreading, document intake and covenant tracking** (admin) | Analyst hours back | Vendors claim 40–60% less analyst time per deal (vendor claims; Evalueserve and nCino sell these tools) | Vendor claims |
| **Renewals and line changes** (lead nurturing) | Renewals caught on time; lines matched to results | Part of most memo tools (vendor material) | Thin |
| **Credit policy Q&A and coaching** (coaching) | Newer analysts up to speed faster | nCino Banking Advisor answers policy questions; American Banker reports AI helps newer bankers most | Thin |
| **Deal screening** (prospecting) | Checking fit with credit appetite before the RM pitches | Vendor claims only | Thin |
| **Risk rating support** (deal scoring) | Faster, consistent rationale | Little public evidence | Out of the first waves: closest to a credit decision |

**What the market shows.** No bank reports letting AI make the credit decision: every example has the AI draft or flag and a person decide. We found no public announcement from a large US bank naming its own AI tool for commercial credit memos (search of 2026-10-13); Moody's reports one unnamed tier-one US bank using its agents.

**Order agreed 2026-10-15:** credit memo and annual review drafts first, early warning second, risk ratings out of the first waves. The full scan, with every source, is kept in the working files (`memos/credit-market-scan.md`).

## Part 7: What banks are deploying in commercial credit, in full

Working file: `memos/credit-market-scan.md`.

As of 2026-10-13. A web scan of what banks are deploying in credit, lined up with the seven core use cases in the RM plan.

> ⚠️ **How much to trust this.** The web search worked, but the primary pages
> would not open from this session (mckinsey.com, federalreserve.gov and
> dbs.com were all blocked). Every fact below comes from search summaries of
> those pages, press coverage or vendor material. Vendor numbers are the
> vendor's own claims, not audited results. Check the original source before
> quoting any number to the bank.

### Summary
- **Credit memos are where banks are furthest along.** DBS rolled an agent that drafts credit memos out to about 1,500 bankers in August 2026, and Moody's says a tier-one US bank uses its agents to write about 35–40% of each memo.
- **Portfolio monitoring (early warning) is where most banks are working.** In McKinsey's survey of credit risk leaders, nearly 60% were pursuing it, more than any other area.
- **Nobody reports letting AI make the credit decision.** Every named example has the AI draft or flag, and a banker or credit officer decides and stays accountable.
- **All six credit processes we parked on 2026-10-09 show up in the market**, and each one lines up with one of the RM plan's seven core use cases (table below).
- **New regulatory guidance to check:** SR 26-2 (April 2026) reportedly replaces SR 11-7, the model risk guidance our files cite. Sources disagree on whether it covers generative AI.

### What banks and vendors have deployed

| Who | What | Status | Evidence quality |
|---|---|---|---|
| **DBS** (Singapore) | Agentic AI tool for relationship managers and credit risk managers. Specialised agents handle more than 70 tasks and pull from annual reports, industry research and internal records to produce a review-ready first draft of a credit memo for large and mid-sized corporate clients. Bankers can ask for more research and revise; they remain responsible for the final memo | Live: announced 19 August 2026, about 1,500 users after a 150-user pilot. DBS estimates credit memos and related work take up to 40% of an RM's time and targets a cut of at least 30% (a target, not a reported result) | Bank announcement, reported by several outlets; bank page itself not opened |
| **A tier-one US bank** (not named) | Moody's agents automate credit memo creation, generating roughly 35–40% of each memo | Deployed, per Moody's Q4 2025 prepared remarks | Vendor's investor remarks; bank not named |
| **A US bank** (not named) | Multi-agent credit memo workflow, reported as 30% faster credit turnaround and 20–60% analyst productivity | Pilot (2025), attributed to McKinsey | **Unconfirmed:** second-hand reports only; McKinsey's page would not open |
| **A top-three Southeast Asian bank** (not named) | Moody's AI early warning solution moved from proof of concept to production across 19 countries | Live, per Moody's earnings call | Vendor's earnings call, via a news summary |
| **A Middle East commercial bank** (not named) | Covenant module added to Evalueserve's spreading platform: the same spread data calculates covenants, and alerts flag breaches | Live | Vendor case study. Vendor reports 70% productivity gains and 99.6% data accuracy (a separate case) |
| **A bank** (not named), via **S&P Global** | Credit memos produced with AI on S&P data | Case study dated 29 May 2026 | Vendor case study |
| **Zions Bancorporation** (US regional) | Chose nCino to digitise commercial loan origination (not described as an AI project) | Selected April 2025 | Press coverage |
| **nCino** (loan platform many US banks use) | Banking Advisor: drafts deal and credit memo narratives, sorts uploaded documents to the right relationship, answers banker questions from uploaded credit policy. Also sells Automated Spreading | Generally available | Vendor press releases |
| **Microsoft** | "Speed credit memo generation" scenario: Copilot Studio agents gather documents, assess the loan and draft the memo from a template; M365 Copilot Chat summarises it for review | Published how-to scenario, not a bank result | Microsoft's own scenario library (search summary) |
| **Salesforce** | Agentforce for Financial Services (launched 21 May 2025): role-based agents in Financial Services Cloud, including a loan officer agent for consumer loans | Generally available; no commercial credit results found | Vendor launch material |

**Not found:** any public announcement from a large US bank (JPMorgan, Wells Fargo, Citi, PNC, U.S. Bank, Fifth Third, Huntington, Citizens, KeyBank, Truist, Regions, BMO) of an AI tool for commercial credit memos, reviews or covenants. Also not found: which loan platform Associated Bank uses. Both are worth asking about inside the bank.

### Industry figures (directional only)
- **Where credit teams are working (McKinsey, "Embracing generative AI in credit risk"; survey of senior credit risk executives at 24 institutions, including nine of the top ten US banks; publication date not confirmed):** portfolio monitoring nearly 60%; credit application processes just over 40%; controls and reporting just over 40%. Respondents see slightly more potential in wholesale (business) credit than retail. Use cases are "mostly narrow, noncustomer-facing."
- **IACPM and McKinsey study (March 2025 deck):** 44 institutions (33 interviewed in Q3 2024, 33 surveyed in December 2024). The use-case percentages are in the deck, which I couldn't open.
- **McKinsey, "The future is agentic: AI's role in the end-to-end corporate credit process" (12 December 2025):** agents can check data quality and consistency and run routine policy checks; the blockers to full automation are system compatibility, data quality and regulation. Deutsche Bank's chief risk officer is reported as calling its agentic work early but already useful (I could not confirm his exact words).
- **Credit memo time:** 20–60% less time, attributed to McKinsey by second-hand sources (unconfirmed). Backbase also cites 20–60% productivity for memo drafting, without saying whether it was measured.
- **Spreading and underwriting time:** vendors claim 40–60% less analyst time per deal and 50–75% shorter time to decision. Vendor claims only.
- **Early warning:** one vendor page claims 12–25% fewer non-performing loans; no primary source given. Treat as unsupported.
- **Budgets:** a 2026 Celent study, commissioned by Zest AI, found 83% of lenders plan to increase generative AI budgets this year.

### Portfolio manager core use cases: each RM core use case and its credit counterpart

The RM plan is organized on seven core use cases. Each has a natural credit
counterpart, often built on the same client data, so an RM AI product and a credit
AI product can share a data contract and agents. ⚠️ The pairing is my own
proposal, not something a source says.

| RM core use case | Credit counterpart (user: portfolio manager or credit analyst) | Parked credit process it covers | What the market shows |
|---|---|---|---|
| **1. Prospecting and next best opportunities** | **Deal screening:** a quick check that a prospect or new request fits the bank's credit appetite before the RM pitches | New (not on our list) | Thin: vendor claims only |
| **2. Lead nurturing, including cross-sell** | **Renewals and line changes:** flag loans coming up for renewal, and clients whose results suggest a bigger or smaller line | Renewals | Vendor material; part of most memo tools |
| **3. Account intelligence and meeting prep** | **Credit memo and annual review first drafts:** one client file pulled together from many systems, drafted in the bank's template, with sources | Credit memos and annual reviews | **Strongest:** DBS live at scale; Moody's at a tier-one US bank; nCino, S&P and Microsoft all offer it |
| **4. Deal scoring and pricing** | **Risk rating support:** AI drafts the rationale and checks it against policy; a person sets the rating | Risk ratings | Little public evidence; it is the closest to a credit decision, so fair-lending rules apply (the same reason pricing is out of the RM plan for now) |
| **5. AI sales coaching** | **Credit policy Q&A and coaching for analysts:** answers from the bank's credit policy, with the page cited | New (not on our list) | nCino Banking Advisor answers policy questions; American Banker reports AI helps newer bankers most |
| **Admin off the RM's plate** | **Spreading, document intake and covenant tracking:** read financial statements into the bank's spread, file documents, test covenants and chase compliance certificates | Spreading financial statements; covenant checks | Vendor case studies (Evalueserve, nCino); widely sold |
| **Keep clients** | **Early warning on credit quality:** signals that a borrower is weakening (late statements, falling deposits, news) | Early warning | McKinsey's most-pursued area (about 60%); Moody's live at a large Asian bank. Shares signals with the RM plan's "Early warning: client may leave" AI product |

**What this shows:** all six parked processes are covered, and two new ones
appear (deal screening, and policy Q&A and coaching). The evidence is strongest
for credit memos and early warning, and weakest for risk ratings and deal
screening.

### Regulatory note: SR 26-2
- **What sources say:** SR 26-2, revised interagency guidance on model risk management, was issued on 17 April 2026 by the Federal Reserve, OCC and FDIC. It reportedly supersedes SR 11-7 (and possibly SR 21-8; sources differ). The Fed's letter reportedly says it is most relevant to banks with over $30 billion in assets. Associated Bank had $51.8 billion at 30 June 2026 (Bank Business Briefing), so it would likely apply.
- **What's unclear:** sources disagree on whether it covers generative and agentic AI. Two (Lumenova, Enzai) say it excludes them; one (Openlayer) says it extends to them. The Fed's own text decides it; I couldn't open it.
- **What it touches in our files:** `tech-stack.md`, `playbook/4-govern-and-test.md`, `playbook/2-define.md` and the RM plan all cite SR 11-7. Not changed yet, because the scope question is open (item W17 in the Open Items log).

### What it means for the credit plan
**The RM structure carries over.** Each RM core use case has a credit
counterpart, so the credit plan can be built on the same seven lines, the same
six steps and the same agents.

**The order (agreed 2026-10-15, closed item C33 in the Open Items log):**
1. **Start with credit memo and annual review drafts.** It has the strongest evidence, it reuses the RM plan's client brief data, and the person stays the decider.
2. **Put early warning second.** It's where most banks are working, and it shares signals with the RM plan's "Early warning: client may leave" AI product.
3. **Keep risk ratings out of the first waves**, for the same reason pricing is out of the RM plan.

### Sources
Opened through web search summaries on 2026-10-13; the pages themselves were not opened unless noted.
- DBS rollout: [Crowdfund Insider, Aug 2026](https://www.crowdfundinsider.com/2026/08/300467-dbs-rolls-out-agentic-ai-tools-to-1500-bankers-aiming-to-significantly-cut-credit-assessment-time/), [The Asian Banker](https://www.theasianbanker.com/press-releases/dbs-rolls-out-agentic-ai-tool-to-support-corporate-credit-assessment-process), [finews.asia](https://www.finews.asia/finance/45058-dbs-rolls-out-agentic-ai-to-1500-bankers), [DBS newsroom](https://www.dbs.com/newsroom/DBS_scales_agentic_AI_to_transform_way_of_working_for_corporate_bankers_freeing_up_time_for_more_strategic_client_engagements) (would not open)
- Moody's: [Q4 2025 prepared remarks](https://s203.q4cdn.com/694693571/files/doc_financials/2025/q4/4Q25-Prepared-Remarks-vFinal.pdf), [Q2 earnings call highlights](https://www.nasdaq.com/articles/moodys-q2-earnings-call-highlights), [Agentic Solutions](https://www.moodys.com/web/en/us/capabilities/gen-ai/agentic-solutions.html), [CRE early warning launch, Jul 2024](https://fintech.global/2024/07/16/moodys-launches-genai-powered-early-warning-system-for-cre-risk-management/)
- McKinsey: [Embracing generative AI in credit risk](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/embracing-generative-ai-in-credit-risk), [The future is agentic (Dec 2025)](https://www.mckinsey.com/industries/financial-services/our-insights/the-future-is-agentic-ais-role-in-the-end-to-end-corporate-credit-process), [IACPM–McKinsey deck (Mar 2025)](https://iacpm.org/wp-content/uploads/2025/03/IACPM-McKinsey-Gen-AI-Webinar-2025.pdf), [Digital Commerce 360 on McKinsey's agent research](https://www.digitalcommerce360.com/2025/07/28/mckinsey-ai-agents-enterprise-value/amp/)
- nCino: [Banking Advisor (Nasdaq press release)](https://www.nasdaq.com/press-release/ncino-deploying-banking-advisor-generative-ai-solution-drive-new-efficiencies), [Data, AI and analytics](https://www.ncino.com/solutions/data-ai-analytics), [Zions selects nCino](https://www.crowdfundinsider.com/2025/04/238581-intelligent-banking-solutions-provider-ncino-selected-by-zions-bancorporation-to-digitally-transform-loan-orginations/)
- S&P Global: [case study, 29 May 2026](https://www.spglobal.com/market-intelligence/en/news-insights/case-studies/a-bank-uses-ai-backed-by-trusted-data-to-quickly-and-reliably-produce-credit-memos)
- Microsoft: [Speed credit memo generation scenario](https://adoption.microsoft.com/en-us/scenario-library/financial-services/speed-credit-memo-generation/)
- Salesforce: [Agentforce for Financial Services launch](https://smallbiztrends.com/salesforce-agentforce-financial-services-ai-launch/)
- Evalueserve: [covenant monitoring case study](https://www.evalueserve.com/case-study/global-bank-automates-covenant-monitoring-using-ai/)
- Backbase: [AI in commercial banking](https://www.backbase.com/blog/ai-in-commercial-banking)
- Vendor claims on spreading, underwriting and early warning: [multimodal.dev](https://www.multimodal.dev/agentic-workflows/commercial-lending-ai), [V7 Labs](https://www.v7labs.com/blog/ai-commercial-loan-underwriting)
- Lending budgets (Celent for Zest AI): [AI in lending statistics](https://www.sci-tech-today.com/stats/ai-in-lending-statistics/)
- American Banker: [How generative AI gives novice bankers a boost](https://www.americanbanker.com/news/at-banks-generative-ai-helps-novices-not-skilled-workers)
- SR 26-2: [Baker Tilly](https://www.bakertilly.com/insights/updated-interagency-guidance-on-model-risk-management), [Lumenova](https://www.lumenova.ai/blog/sr-26-2-model-risk-management-banking/), [Enzai](https://www.enz.ai/glossary/sr-26-2), [Openlayer](https://www.openlayer.com/blog/post/sr-26-2-mrm-guide-ai-teams), [Fed letter](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) (would not open)

## Part 8: The prototype: what it shows and how it's built

Working file: `prototypes/pm-assistant/README.md`.

A clickable concept of **The PM Assistant**: one AI assistant for each portfolio manager (PM), the credit
partner paired with a relationship manager (RM). It shows the plan's wave 1 capabilities working (the
borrower file and the review and memo drafts) and a wave 2 preview (early warning), with three agents
running live on Claude, on made-up sample data. Current version: **2** (`prototype-v2.html`; version 1 is kept unchanged). It's a prototype to show we can build; the real product
comes from the six steps (Discover onward), so every fact about the bank in it is an assumption to confirm.

- **Live page:** https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE (private until shared from its Share menu)
- **The tour as a video:** `pm-assistant-tour-v2.mp4` (under 2 minutes, with a voiceover read by Kokoro, an open-source voice; the script is `video/narration.json`). Re-recorded for version 2 because the screens in the tour changed (the "Early warning flags" name, "Approve as final"); the narration didn't change, so the version 1 voice clips were reused. The version 1 video, `pm-assistant-tour-v1.mp4`, is kept.
- **Built from:** Prompt 4 in `prompt-library.md`, with the user group changed to PMs; the product page (`memos/pm-assistant.md`), agents A7 to A9 and workflows B10 to B14 in the full plan (`memos/pm-assistant-framework.md`); controls in `playbook/controls.md`. Copied from the RM Assistant Prototype (`prototypes/rm-assistant/`, version 4), so both share one house style and structure.
- **The same sample world as the RM prototype:** Sam Okafor is the portfolio manager the RM prototype's Jordan Ellis refers credit to, and the 12 borrowers are Jordan's 12 clients, with the same loans.
- **Added for the prototype only:** the outside data feed (the 10-year Treasury yield), shown only as background in the borrower file. **The Treasury yield never enters a draft:** the sample loans are Prime-based, so it says nothing direct about their rates, and rate commentary is the PM's analysis; A8 drafts from the file without it, and a draft that mentions it is flagged and can't be approved. It isn't in the plan's agent specs or data contract; a real build would add it through the data contract (K5) first.

### What's in it

| Screen | Plan reference | What happens |
|---|---|---|
| Today | Ties the capabilities together | The PM's day on one screen: four numbers to click (reviews due, borrowers with early warning flags, drafts waiting, items missing or late), reviews and requests coming due, and what's waiting for a decision. The flags count and the early warning decisions are tagged "Wave 2 preview". |
| Borrower file | Workflow B10, agent A7 | A7 checks the PM may see the borrower (K4), then calls five page tools (financials, loans and covenants, deposits and payments, documents and notes, market data), each step shown. Every figure carries its source, and code lists what's missing or late. Claude summarizes the file. The PM uses it, asks the RM for what's missing (a drafted note the PM sends) or flags an error. |
| Review and memo drafts | Workflows B11 and B12, agent A8 | Claude drafts the five routine sections of an annual review or credit memo from A7's file. The draft is marked "AI draft" and names the credit officer who decides; the risk rating and recommendation are left blank "For the PM's judgment". Code checks every number (K7), marks sections "needs input" where the file has a gap (K25), removes any rating or recommendation section the AI writes and scans for decisions and prices (K3, K8). The draft states facts with sources and draws no conclusions. The recommendation box notes it's "required only if the bank's credit policy asks for a recommendation (to confirm)". Approval is held until the PM writes the judgment; the button is "Approve as final", and **the assistant never submits**: the PM submits it through the bank's normal approval route. |
| Early warning flags (wave 2 preview) | Workflows B13 and B14, agent A9 | Five sample rules in code (K22), EW1 to EW5; a sample set for the prototype, since the real rules are credit risk's to set: statements late, covenant within 10% of its limit, covenant breached, deposits down 25% or more over 3 months, payment past due. Claude explains the flags with the numbers. The PM dismisses (with a reason), watches, or raises it through the bank's process. Below, the covenant and statement tracker (B14) lists every test and due item. |
| Controls and audit log | K1, K2, K3, K4, K7, K8, K12, K22, K25 | "Try to break it" (risk ratings, approvals, recommendations, prices, other PMs' borrowers, record changes and contacting borrowers are stopped in code, while a PM's ordinary credit questions pass); A9's rule set; the live audit log. |
| How we'd measure it | The five kinds of measures | Usage, quality, business impact, adoption, and risk and controls, counted from the session, each with a made-up sample pilot week. |
| How it's built | | The agents, the data, how it's tested, what a pilot would need, and where this sits in the product machine (sub-step 1.6). |

The **guided tour** plays on a first visit (under 2 minutes, voiced), and anyone can pause, skip, mute or replay it.

**One borrower is incomplete on purpose:** Chequamegon Timber Works hasn't sent its FY2025 statements or its Q2 2026
compliance certificate, so its file lists them as late, its review draft marks two sections "needs input", and
approval is held until they're resolved (K25).

### How it works

- **Live AI:** inside claude.ai the page asks Claude through the artifact's `sample` capability (the same mechanism as the RM prototype), on the viewer's own Claude account (the first run asks the viewer's permission). A7's summary and A9's explanations use the quick model tier; A7 calls the page tools itself when tools are available; A8's draft uses the default tier. The page must be published with `capabilities: {sample: {}}`.
- **Without live AI** (outside claude.ai, or if the viewer says no), every screen plays the **recorded run** in `src/replay.js`, written by Claude during the build and labeled "Recorded run" on screen. A7's gathering is code, so it works for every borrower; the recorded summary covers three of them. The tour always uses recorded runs, so it never spends anyone's usage.
- **Number check (K7 and the accuracy bar):** as soon as an AI output is finished, every number in it is matched against the borrower file (including numbers written inside rates and requested terms, such as "Prime + 0.50%"); anything it can't trace is highlighted, and approval is held until the PM changes the draft so it matches. Dates, fiscal years and codes are skipped, and so are small whole numbers under 10.
- **Ratios and growth** are calculated in code by A7 from the statement figures and labeled "A7 calculation", so the AI never has to calculate a number.
- **Guardrails (K3, K8, K4, K2, K1):** checked in code before Claude is asked; Claude's prompt carries the same rules as a second line of defense, and every finished draft is scanned again. The code check is pattern matching, so it catches common phrasings, not every possible one; `tests/run-tests.js` lists the phrasings it must block and the ordinary questions it must allow.
- **Outside data:** the US 10-year Treasury yield (monthly average, Federal Reserve H.15, public domain), via the datahub.io copy on GitHub. A published page can't reach outside websites, so `scripts/fetch_market.py` saves a dated copy into `src/data/market.js` and the page shows that date. (The Federal Reserve's and FRED's own sites weren't reachable from the build sandbox; GitHub was.)

### Files

| Path | What it is |
|---|---|
| `src/page.html` | The page's markup |
| `src/styles.css` | The house style (the RM prototype's, plus the PM additions at the end), light and dark |
| `src/data/portfolio.js` | The sample PM, 12 borrowers (plus 2 of another PM's) |
| `src/data/market.js` | The outside data (generated; don't edit) |
| `src/agents.js` | A7's page tools and missing list, A9's rules, the guardrails, the number check, the audit log and the prompts |
| `src/replay.js` | The recorded runs |
| `src/app.js` | The screens |
| `src/tour.js` | The guided tour |
| `build.py` | Inlines everything (and the voice clips) into one file, `prototype-v<N>.html` |
| `tests/run-tests.js` | Automated tests of the "done" checklist, with a test double standing in for Claude |
| `tests/record-video.js` | Records the tour as a video, each step timed to its voiceover line |
| `video/narration.json` | The voiceover script, one line per tour step |
| `video/narrate.py` | Reads the script aloud with Kokoro (code MIT, model Apache 2.0), one clip per step |
| `video/make-video.py` | Retimes the recording to real time and lays the voice down in sync |
| `voice/` | The tour's voice, one MP3 per step, and their lengths |
| `prototype-v1.html`, `prototype-v2.html` | The delivered versions, each kept unchanged (version 2 is current) |
| `pm-assistant-tour-v1.mp4`, `pm-assistant-tour-v2.mp4` | The tour as a video, one per version that changed the tour |
| `CHANGELOG.md` | What changed in each version |

### How to change it

1. Edit the files in `src/` (or refresh the outside data: `python3 scripts/fetch_market.py`).
2. Build the next version: `python3 build.py 3` writes `prototype-v3.html`. Delivered versions are never overwritten, so every step is kept.
3. Test it: `PW=$(npm root -g)/playwright CHROMIUM=/opt/pw-browsers/chromium node tests/run-tests.js prototype-v3.html` (screenshots go to `$SHOTS`).
4. If the tour changed: `pip install kokoro-onnx soundfile`, get `kokoro-v1.0.onnx` and `voices-v1.0.bin` (see `video/narrate.py`), run `python3 video/narrate.py video/narration.json <clips folder>`, convert the clips to MP3 into `voice/` (`ffmpeg -i stepNN.wav -ac 1 -b:a 48k voice/stepNN.mp3`) with `lens.json`, rebuild, then `NARRATION=voice/lens.json OUT=<folder> node tests/record-video.js prototype-v3.html` and `python3 video/make-video.py <folder> <clips folder> pm-assistant-tour-v3.mp4`. If only the screens changed and not the narration, skip Kokoro: convert `voice/stepNN.mp3` back to 16-bit WAV clips (`ffmpeg -i voice/stepNN.mp3 -ac 1 -ar 24000 -sample_fmt s16 <clips folder>/stepNN.wav`, plus a copy of `lens.json`) and record.
5. Add a line to `CHANGELOG.md`, publish the new file to the same page link, and save a draft to GitHub.

_Last updated: 2026-10-19_
