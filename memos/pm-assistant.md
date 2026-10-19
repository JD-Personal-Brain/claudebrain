# The PM Assistant

> ⚠️ **A working hypothesis**, built from outside research and public Associated job postings. The first interviews with portfolio managers (PMs) and their leaders confirm or change it.

## The product in one line
Each PM gets **their own AI assistant**, inside the tools we expect they use (Word, Teams, the loan system and the bank's data; ⚠️ to confirm), to take the gathering and routine writing off their plate, so their time goes to credit judgment, and to spot weakening borrowers sooner. Its users are PMs and the credit analysts who support them. It starts with three **capabilities** and gains more, feature wave by feature wave.

## 1. Its limits
These limits make it safe to give every PM one.
- **Jobs:** only the capabilities below. Anything else, it says so and stops.
- **Workflows (where it works):** Word from the bank's templates, Teams and the loan system (⚠️ to confirm). No new app.
- **Data:** borrower data the bank has approved as trusted (certified) and the credit file's documents, only for the borrowers the PM may already see; for the industry background, approved industry sources only.
- **Controls:** it gathers, drafts and flags; the PM writes the judgment and submits. It never sets or suggests a borrower risk rating, never approves or declines credit and never sets a price. The recommendation is left for the PM. Every draft names the credit officer who decides. Everything is logged.
- **Feedback:** one click on every output (use, change or reject), which steers what gets better next.

## 2. Capabilities, by moment in the PM's work
Each capability is one AI product and answers one credit core use case (our proposal, to agree; see the [Use Case Library](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X#portfolio-managers) for the value and the research).

| Moment | Capability | What it does | Credit core use case | Wave |
|---|---|---|---|---|
| **Review and renew** (and new requests) | [Industry background draft](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b16) | The industry background section of a credit memo (the industry's size and trend, main drivers and risks, outlook), from approved sources only, every statement cited and dated, for the PM to edit and approve; it uses no borrower data and writes no judgment about the borrower | Credit memo and annual review drafts | 1 |
| | [Borrower file](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b10) | Everything about one borrower in one place, every figure with its source, and what's missing or late | Credit memo and annual review drafts | 1 |
| | Annual review and credit memo drafts ([review](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b11), [memo](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b12)) | The routine sections drafted in the bank's template; the borrower risk rating and the recommendation left for the PM | Credit memo and annual review drafts | 1 |
| | Renewal radar | Loans coming up for renewal, and borrowers whose results suggest a bigger or smaller line (higher-risk path, our assumption) | Renewals and line changes | 3 |
| **Watch the portfolio** | [Early warning flags](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b13) | Flags borrowers whose signals are weakening, with the numbers (higher-risk path, our assumption); the PM decides whether a flag goes to the bank's own watchlist or rating review (⚠️ to confirm how that runs today) | Early warning on credit quality | 2 |
| | [Covenant and statement tracker](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b14) | Covenant tests, and statements and certificates due or late | Spreading, document intake and covenant tracking | 2 |
| **New requests** | Deal screening | A quick check that a request fits the bank's credit appetite (higher-risk path, our assumption); it never declines, only notes where a request sits against the appetite | Deal screening | 3 |
| **Know the policy** | Credit policy Q&A | Answers from the credit policy, citing the section | Credit policy Q&A and coaching | 3 |
| **Left out on purpose** | Borrower risk rating support; approve or decline; pricing | Kept out because they are the credit decision itself | Risk rating support | Out |

## 3. What it's built on
Every capability runs on one shared foundation, built once:
- borrower data: loans, covenants, deposits and payments (⚠️ where they live is to confirm);
- the credit file: financial statements, the spread (the borrower's statements entered in the bank's standard format), prior reviews and other documents, read with the page cited. Wave 1 reads the spread already in the bank's spreading tool; it doesn't spread statements itself (⚠️ to confirm);
- an approved list of industry sources, each with its license terms;
- the bank's review and memo templates and its credit policy;
- a set of warning rules (simple, explainable, agreed with credit risk; ⚠️ which team owns early warning rules is to confirm), with AI explaining each flag in plain English;
- drafting, with every number checked against its source, and the controls and feedback above.

Every detail is in [PM Detail](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg); see it working in the [PM Assistant Prototype](https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE).

_Last updated: 2026-10-19_
