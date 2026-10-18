# RM Assistant

> ⚠️ **A working hypothesis** (agreed 2026-10-17), built from outside research and public Associated job postings. Conversations with the leaders of relationship managers (RMs) and Discover confirm or change it.

## The product in one line
Each RM gets **their own AI assistant**, inside Salesforce, Teams and Outlook, to help them win business and free up the time to win it. It starts with three **capabilities** and gains more, feature wave by feature wave. Every later AI product for RMs is a new capability of the same assistant.

## 1. Its limits
These limits make it safe to give every RM one.
- **Jobs:** only the capabilities below. Anything else, it says so and stops.
- **Where it works:** the Salesforce client record, Teams and Outlook. No new app.
- **Data:** certified client data, only for the clients the RM may already see, plus the RM's own calendar, email and meetings.
- **Controls:** it drafts and suggests; the RM approves anything saved or sent. It never contacts a client, never makes a credit decision and never sets or suggests a price. Meetings are recorded only with client consent. Everything is logged.
- **Feedback:** one click on every output (use, change or reject), which steers what gets better next.

## 2. Capabilities, by moment in the RM's work
Each capability is one AI product and answers one core use case (see the [Use Case Library](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X) for the value and the research).

| Moment | Capability | What it does | Core use case | Wave |
|---|---|---|---|---|
| **Find business** | Monday opportunity list | Each Monday, the top clients to call, with the reason and the numbers | Prospecting and next best opportunities | 1 |
| | Prospect lookalikes | Companies that look like the bank's best clients | Prospecting and next best opportunities | 2 |
| | Referral prompts | Flags a client need for a partner team, such as treasury management | Lead nurturing, including cross-sell | 2 |
| **Before the meeting** | Pre-meeting client brief | One page before each client meeting | Account intelligence and meeting prep | 1 |
| | Client Q&A | Answers "what should I know about this client?" | Account intelligence and meeting prep | 3 |
| **During and after** | Meeting follow-up | Drafts the recap, the follow-up email and the call notes for Salesforce, for the RM to approve | Admin off the RM's plate | 1 |
| | AI sales coaching | Private guidance for the RM after a call | AI sales coaching | 3 |
| **Keep the book** | Early warning | Flags clients who may be drifting away | Keep clients | 2 |
| **Left out on purpose** | Pricing suggestions; contacting prospects on its own | — | Deal scoring and pricing; lead nurturing (full version) | Out |

## 3. What it's built on
One shared foundation, built once for every capability: client data from Salesforce and Snowflake, the RM's own work (calendar, email, meetings; transcripts only with client consent), outside prospect data the bank licenses (to confirm), a **signals engine** (simple, explainable rules find opportunities and risks; AI explains them in plain English with the numbers), drafting, and the controls and feedback above.

Every detail (the RM's job, the foundation part by part, what to confirm) is in [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n), the fourth page in the RM section.

_Last updated: 2026-10-18_
