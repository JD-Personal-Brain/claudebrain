# The RM Assistant

> ⚠️ **A working hypothesis**, built from outside research and public Associated job postings. The first interviews with relationship managers (RMs) and their leaders confirm or change it.

## The product in one line
Each RM gets **their own AI assistant**, inside the tools we expect they use (Salesforce, Teams and Outlook; ⚠️ to confirm), to help them win business and free up the time to win it. It starts with three **capabilities** and gains more, feature wave by feature wave.

## 1. Its limits
These limits make it safe to give every RM one.
- **Jobs:** only the capabilities below. Anything else, it says so and stops.
- **Workflows (where it works):** the Salesforce client record, Teams and Outlook (⚠️ to confirm). No new app.
- **Data:** client data the bank has approved as trusted (certified), only for the clients the RM may already see, plus the RM's own calendar, email and meetings.
- **Controls:** it drafts and suggests; the RM approves anything saved or sent. It never contacts a client, never makes a credit decision and never sets or suggests a price. Meetings are recorded only with client consent. Everything is logged.
- **Feedback:** one click on every output (use, change or reject), which steers what gets better next.

## 2. Capabilities, by moment in the RM's work
Each capability is one AI product and answers one core use case (see the [Use Case Library](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X#relationship-managers) for the value and the research).

| Moment | Capability | What it does | Core use case | Wave |
|---|---|---|---|---|
| **Find business** | Monday opportunity list | Each Monday, the top clients to call, with the reason and the numbers ([how it works](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b1)) | Prospecting and next best opportunities | 1 |
| | Prospect lookalikes | Companies that look like the bank's best clients ([how it works](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b8)) | Prospecting and next best opportunities | 2 |
| | Referral prompts | Flags a client need for a partner team, such as treasury management ([how it works](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b6)) | Lead nurturing, including cross-sell | 2 |
| **Before the meeting** | Pre-meeting client brief | One page before each client meeting ([how it works](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b2)) | Account intelligence and meeting prep | 1 |
| | Client Q&A | Answers the RM's own questions about a client at any time, with the source for each answer ([how it works](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b7)) | Account intelligence and meeting prep | 3 |
| **During and after** | Meeting follow-up | Drafts the recap, the follow-up email and the call notes for Salesforce from the RM's own notes (from the Teams transcript later, only where recording is allowed and the client agrees) ([how it works](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b3)) | Admin off the RM's plate | 1 |
| | AI sales coaching | Private guidance for the RM after a call | AI sales coaching | 3 |
| **Keep the book** | Early warning | Flags clients who may be drifting away ([how it works](https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX#b5)) | Keep clients | 2 |
| **Left out on purpose** | Pricing suggestions; contacting clients or prospects on its own | Kept out to protect fair lending and client trust | Deal scoring and pricing; lead nurturing (the full, automated version) | Out |

## 3. What it's built on
Every capability runs on one shared foundation, built once:
- client data from Salesforce and Snowflake (⚠️ to confirm);
- the RM's own calendar, email and meetings (transcripts only with client consent);
- outside prospect data the bank licenses (⚠️ to confirm);
- a **signals engine**: simple, explainable rules spot opportunities and risks, and AI explains each one in plain English with the numbers;
- drafting, and the controls and feedback above.

Every detail is in [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n); see it working in the [RM Assistant Prototype](https://claude.ai/artifact/RFM2o7cdren3TxesQBsjky).

_Last updated: 2026-10-19_
