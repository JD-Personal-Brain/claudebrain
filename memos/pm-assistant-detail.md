# The PM Assistant: full detail

The detailed working file behind The PM Assistant page. People read the short page (The PM Assistant); this file goes into PM Detail.

> ⚠️ **A hypothesis, not a plan yet** (reviewed and agreed 2026-10-19). Built from our commercial credit research, the Use Case Library and public Associated job postings, not from how the bank's portfolio managers work today. The first conversations with credit leaders test it; Discover confirms or changes the rest.

## The product in one line
Each portfolio manager (PM) gets **their own AI assistant**, inside the tools we expect the PM already uses (Word, Teams, the loan system and the bank's data; ⚠️ to confirm). Its job is to take the gathering and routine writing off the PM's plate, so the PM's time goes to credit judgment, and to spot weakening borrowers sooner. It starts with three **capabilities**, each doing one specific job in the PM's work, and gains more feature wave by feature wave. Every later AI product for PMs is a new capability of the same assistant.

## 1. A personal AI, with limits
The assistant is personal to each PM, and it is constrained in five ways. These limits are what make it safe to give every PM one.

| Limit | What it means |
|---|---|
| **Jobs** | It does only the capabilities listed on this page. Anything else, it says so and stops. |
| **Workflows** | It works where we expect the PM already works (to confirm in Discover): Word from the bank's templates, Teams, the loan system. No new app to learn. |
| **Data** | Certified borrower data only (financials, loans, covenants, deposits, payments), the credit file's documents and the relationship manager's (RM's) approved notes, always limited to the borrowers the PM may already see; for the industry background, approved industry sources only. |
| **Controls** | It gathers, drafts and flags; the PM writes the judgment and submits. It never sets or suggests a borrower risk rating, never approves or declines credit and never sets a price. Wave 1 drafts leave the recommendation blank; whether a later draft may carry one is the credit policy owner's call at 2.4 (our assumption). Every draft names the credit officer who decides. Everything is logged. |
| **Feedback** | Every output has one-click feedback (use, change or reject, with a reason). The feedback steers what gets better next. |

## 2. What a PM's job is
From Associated's public PM postings (seen through search results on job boards, 2026-10-14; ⚠️ check against the bank's own careers site):

| Part of the job | What it means | Where the assistant helps |
|---|---|---|
| **Underwrite new credit** | Analyze a borrower's financials and write the credit memo for a new loan, renewal or line change | Industry background draft, borrower file, credit memo draft |
| **Review the portfolio** | Annual reviews of each borrower: financial performance, covenants, collateral, borrower risk rating | Borrower file, annual review draft |
| **Monitor credit quality** | Watch for weakening borrowers; track statements, compliance certificates and covenants | Early warning flags, covenant and statement tracker |
| **Partner with RMs** | Work closely with the RM on each relationship and each request | Faster drafts mean faster answers for the RM |
| **Know the policy** | Apply the bank's credit policy and procedures | Credit policy Q&A |

## 3. Capabilities, by moment in the PM's work
Each capability is one AI product (glossary) and answers one credit core use case, the credit counterpart of an RM core use case (the Use Case Library's portfolio manager section; the pairing is our proposal, to agree). The core use case "Credit memo and annual review drafts" covers all three wave 1 capabilities: the industry background draft, the borrower file and the drafts.

| Moment | Capability | What it does | Credit core use case | Wave |
|---|---|---|---|---|
| **Review and renew** (and new requests) | Industry background draft | The industry background section of a credit memo (the borrower's industry: its size and trend, main drivers and risks, outlook), drafted from approved and licensed sources only, every statement cited and dated, for the PM to edit and approve; it uses no borrower data and writes no judgment about the borrower | Credit memo and annual review drafts | 1 |
| | Borrower file | Everything about one borrower in one place, every figure with its source, and what's missing or late | Credit memo and annual review drafts | 1 |
| | Annual review and credit memo drafts | The routine sections drafted in the bank's template; the borrower risk rating and the recommendation left for the PM | Credit memo and annual review drafts | 1 |
| | Renewal radar | Loans coming up for renewal, and borrowers whose results suggest a bigger or smaller line (higher-risk path, our assumption) | Renewals and line changes | 3 |
| **Watch the portfolio** | Early warning flags | Flags borrowers whose signals are weakening, with the numbers | Early warning on credit quality | 2 |
| | Covenant and statement tracker | Covenant tests from the spread, and statements and certificates due or late | Spreading, document intake and covenant tracking | 2 |
| **New requests** | Deal screening | A quick check that a request fits the bank's credit appetite before the RM pitches (higher-risk path, our assumption) | Deal screening | 3 |
| **Know the policy** | Credit policy Q&A | Answers from the bank's credit policy, citing the section | Credit policy Q&A and coaching | 3 |
| **Left out on purpose** | Borrower risk rating support; approve or decline; pricing | Closest to the credit decision; kept out under control K3 | Risk rating support | Out |

**Wave 1 at a glance:** three capabilities. The industry background draft goes first: it drafts the section of the credit memo an outside firm writes today, and needs no borrower data. Then two that work as one flow: the borrower file, then the draft built from it. Together they cover the PM's most frequent writing job, the annual review, and the credit memo for a request. The order follows the credit order agreed on 2026-10-15: memo and review drafts first, early warning second, borrower risk ratings out of the first waves.

**How each capability is built.** Our measures' targets are set in Define; outside figures are benchmarks in the Use Case Library, never our targets.

| Wave | Capability (AI product) | Credit core use case | Agents | Built mainly on | Our measure (target set in Define) |
|---|---|---|---|---|---|
| **Wave 1** (industry background draft by week [X], set at gate 2; borrower file by week [X], set at gate 2; drafts by about week 12; each once its approvals are in) | Industry background draft | Credit memo and annual review drafts | A11 | AWS Bedrock (Knowledge Bases over the approved industry sources) or Copilot Studio | Outside fees we could replace; turnaround; share of each section kept with light edits [X] |
| | Borrower file | Credit memo and annual review drafts | A7 | Snowflake, AWS Bedrock (Knowledge Bases) | Hours spent gathering per review [X] |
| | Annual review and credit memo drafts (higher-risk path) | Credit memo and annual review drafts | A7, A8 | AWS Bedrock or Copilot Studio; Word templates | Hours per review; share of sections used with light edits [X] |
| **Wave 2** (dates set once the wave 1 drafts' review is signed, about week 11) | Early warning flags (higher-risk path) | Early warning on credit quality | A9 | Snowflake signals, Teams | Flags acted on; how much earlier than today [X] |
| | Covenant and statement tracker | Spreading, document intake and covenant tracking | Rules in code (workflow B14) | Snowflake, the spreading tool (⚠️ to confirm) | Late items; analyst hours saved [X] |
| **Wave 3** (dates set once the wave 1 drafts' review is signed, about week 11) | Credit policy Q&A | Credit policy Q&A and coaching | A10 | Copilot Studio or Bedrock Knowledge Bases | Questions answered; answer ratings [X] |
| | Renewal radar; deal screening (higher-risk path, our assumption) | Renewals and line changes; deal screening | Specs to come | Snowflake, the loan system | Renewals on time; screening turnaround [X] |

**Why the industry background draft goes first (2026-10-19):** The bank's credit lead (2026-10-19; ⚠️ details to confirm: which firm, cost per section, how many a year, turnaround, the contract's terms, and which sources the firm uses) told us the bank pays an outside firm to write the industry background section of its credit memos, and wants AI to draft that section as one of the first use cases. It uses no borrower data and makes no credit judgment, so we assume a lighter review (⚠️ the risk partner decides at 2.4 whether it takes the higher-risk path, since it sits inside a credit memo). It could replace a cost the bank pays today, so the saving would be direct and measurable: outside fees saved, counted once the contract changes (its terms are to confirm). And the bank's credit lead named it. Because it needs no client data, it can be built and tested on public sources before gate 2. If its review runs long, it is no worse than today: the outside firm keeps writing the section.

**Why the borrower file is its own capability (our call, 2026-10-19):** it gathers and cites but writes no judgment, so we assume it needs less review than the drafts (⚠️ the risk partner decides) and can go live ahead of them if the higher-risk review of the drafts runs long. It also saves PMs time on its own. K3's wording (output that informs a credit decision) could cover it, which is why it is the first question for the risk partner at 2.4, and why the backup plan covers it.

**Why the judgment sections stay blank:** the borrower risk rating and the recommendation are where the credit decision lives. Leaving them to the PM keeps the AI on the right side of control K3 and keeps the PM accountable. Wave 1 drafts leave the recommendation blank; whether a later draft may carry one is the credit policy owner's call at 2.4 (our assumption).

**Why early warning is wave 2:** it is the area most credit risk leaders in McKinsey's survey of 24 institutions are pursuing (the Use Case Library), but it needs agreed rules from credit risk (⚠️ which team owns early warning rules is to confirm) and its own fairness check, and it touches the bank's own watchlist process, which we don't know yet. We call ours "early warning flags" so they are never mistaken for the bank's watchlist.

**Why deal screening and the renewal radar's line suggestions wait for wave 3:** both sit close to a credit decision, so we assume they take the higher-risk path (K3); the risk partner rates each at 2.4 before it is specified ⚠️.

## 4. The foundation underneath
Built once and shared by every capability.

| Part | What it is | Used by |
|---|---|---|
| **Borrower data** | Loans, covenants, deposits and payments, which we expect in Snowflake (⚠️ or Fabric; certified data only) | Every capability |
| **The credit file** | Financial statements, the spread (the statements in the bank's standard format), prior reviews, appraisals and other documents (⚠️ where they live is to confirm), read with their page cited | Borrower file, drafts |
| **An approved industry source list** | The industry sources the industry background draft may read, each with its license terms; part of the data contract (K5), with any licensed source reviewed by vendor risk (K14) (⚠️ which sources is to confirm) | Industry background draft |
| **The bank's templates and policy** | The annual review and credit memo templates; the credit policy | Drafts, policy Q&A |
| **Signals engine** | Simple, explainable rules agreed with credit risk (⚠️ which team owns early warning rules is to confirm); AI explains each flag with the numbers | Early warning, covenant tracker, renewal radar |
| **Drafting** | Drafts marked as AI drafts, with every number checked against its source in code | Drafts |
| **Controls and logs** | The limits in section 1, built once and tested for every capability | Every capability |
| **Feedback loop** | One-click feedback on every output, sorted and fed into the next release | Every capability |

Spreading and document intake stay with the bank's spreading tool (⚠️ to confirm); the tracker reads its spread, as the Evalueserve covenant case does (vendor case study).

## 5. How we'll know it works
- **An outside cost we could replace:** outside fees for industry sections (counted once the contract changes; its terms are to confirm), and the section's turnaround [X].
- **More PM time for judgment:** hours per annual review and credit memo, against PMs not yet using it [X].
- **Faster answers:** days from a complete request to a decision [X].
- **Earlier sight of trouble:** flags acted on, and how early (wave 2) [X].
- **Use:** PMs using it every week, and the share of drafts used with light edits [X].

Targets are [X] until the bank's own numbers are in.

## 6. Working with the RM side
The PM and the RM work each relationship together. The RM Assistant's approved call notes are one input to the borrower file, and early warning on credit quality shares its signals engine with the RM side's "client may leave" early warning, while each flag goes only to its own user group. A credit request draft from the RM (an idea on the RM side, not decided) would be where the two assistants meet. These links are notes for the detail document; each group's pages stand on their own.

## 7. What to confirm
The one full list is in the full plan, section 8 ("What I'd confirm in the first weeks").

## 8. How it maps to the agents
The core use cases, in their credit counterparts, are the **needs** the capabilities answer, and each capability is one AI product. The product agents do the work: A11 drafts the industry background section from approved sources; A7 builds the borrower file; A8 drafts reviews and memos; A9 watches for early warning signs (the **signals engine**); A10 answers credit policy questions (wave 3). The covenant tracker is rules in code inside workflow B14, not an agent.

_Last updated: 2026-10-19_
