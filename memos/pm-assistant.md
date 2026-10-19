# The PM Assistant

> ⚠️ **A working hypothesis** (first cut, 2026-10-19), built from outside research and public Associated job postings. The first interviews with the leaders of portfolio managers (PMs) and with PMs confirm or change it.

## The product in one line
Each PM gets **their own AI assistant**, inside the tools we expect they use (Word, Teams, the loan system and the bank's data; ⚠️ to confirm), to take the gathering and routine writing off their plate, so their time goes to credit judgment, and to spot weakening borrowers sooner. It starts with two **capabilities** and gains more, feature wave by feature wave. Every later AI product for PMs is a new capability of the same assistant.

## 1. Its limits
These limits make it safe to give every PM one.
- **Jobs:** only the capabilities below. Anything else, it says so and stops.
- **Workflows (where it works):** Word from the bank's templates, Teams and the loan system (⚠️ to confirm). No new app.
- **Data:** borrower data the bank has approved as trusted (certified) and the credit file's documents, only for the borrowers the PM may already see.
- **Controls:** it gathers, drafts and flags; the PM writes the judgment and submits. It never sets or suggests a risk rating, never approves or declines credit and never sets a price. Every draft names the credit officer who decides. Everything is logged.
- **Feedback:** one click on every output (use, change or reject), which steers what gets better next.

## 2. Capabilities, by moment in the PM's work
Each capability is one AI product and answers one credit core use case (see the [Use Case Library](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X#portfolio-managers) for the value and the research).

| Moment | Capability | What it does | Credit core use case | Wave |
|---|---|---|---|---|
| **Review and renew** | Borrower file | Everything about one borrower in one place, every figure with its source, and what's missing or late | Credit memo and annual review drafts | 1 |
| | Annual review and credit memo drafts | The routine sections drafted in the bank's template; the risk rating and recommendation left for the PM | Credit memo and annual review drafts | 1 |
| | Renewal radar | Loans coming up for renewal, and borrowers whose results suggest a different line | Renewals and line changes | 3 |
| **Watch the portfolio** | Early warning watchlist | Flags borrowers whose signals are weakening, with the numbers | Early warning on credit quality | 2 |
| | Covenant and statement tracker | Covenant tests, and statements and certificates due or late | Spreading, document intake and covenant tracking | 2 |
| **New requests** | Deal screening | A quick check that a request fits the bank's credit appetite | Deal screening | 3 |
| **Know the policy** | Credit policy Q&A | Answers from the credit policy, citing the section | Credit policy Q&A and coaching | 3 |
| **Left out on purpose** | Risk rating support; approve or decline; pricing | Kept out because they are the credit decision itself | Risk rating support | Out |

## 3. What it's built on
Every capability runs on one shared foundation, built once:
- borrower data: loans, covenants, deposits and payments (⚠️ where they live is to confirm);
- the credit file: financial statements, the spread, prior reviews and other documents, read with the page cited;
- the bank's review and memo templates and its credit policy;
- a **signals engine**: simple, explainable rules agreed with credit risk, with AI explaining each flag in plain English;
- drafting, with every number checked against its source, and the controls and feedback above.

Every detail (the PM's job, the foundation part by part, what to confirm) is in [PM Detail](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg), for AI to read. To see the assistant working, try the [PM Assistant Prototype](https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE).

_Last updated: 2026-10-19_
