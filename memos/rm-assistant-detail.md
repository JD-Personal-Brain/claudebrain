# The RM Assistant: full detail

The detailed working file behind The RM Assistant page. People read the short page (`memos/rm-assistant.md`); this file goes into RM Product Information for AI.

> ⚠️ **A hypothesis, not a plan yet** (agreed as our working hypothesis on 2026-10-17). Built from McKinsey's research, the RM plan and public Associated job postings, not from how the bank works today. The first test is the talk with the RM lead on Tuesday October 20; Discover confirms or changes the rest.

## The product in one line
Each relationship manager (RM) gets **their own AI assistant**, inside Salesforce, Teams and Outlook. Its job is to help the RM win business and to free up the time they need to win it. It starts with three **capabilities**, each doing one specific job in the RM's work, and gains more feature wave by feature wave. It is the base everything else builds on: every later AI product for RMs is a new capability of the same assistant.

## 1. A personal AI, with limits
The assistant is personal to each RM, and it is constrained in five ways. These limits are what make it safe to give every RM one.

| Limit | What it means |
|---|---|
| **Jobs** | It does only the capabilities listed on this page. Anything else, it says so and stops. |
| **Workflows** | It works where the RM already works: the Salesforce client record, Teams and Outlook. No new app to learn. |
| **Data** | Client data: certified data only. It also uses the RM's own calendar, email and meetings (transcripts only with consent) and any outside prospect data the bank licenses. Client data is always limited to the clients the RM is already allowed to see. |
| **Controls** | It drafts and suggests; the RM approves anything saved or sent. It never contacts a client on its own, never makes a credit decision and never sets or suggests a price. Meetings are recorded only with client consent. Everything it does is logged. |
| **Feedback** | Every output has one-click feedback (use, change or reject, with a reason). The feedback steers what gets better next. |

## 2. What an RM's job is
From Associated's public RM postings (seen through search results on job boards, 2026-10-17; ⚠️ check against the bank's own careers site):

| Part of the job | What it means | Where the assistant helps |
|---|---|---|
| **Find new business** | Prospecting: steady calling, centers of influence, new clients | Prospect lookalikes |
| **Grow and keep the book** | Manage a book of middle-market business clients; keep and deepen each relationship | Monday opportunity list, early warning, client briefs |
| **Cross-sell and refer** | Bring in deposits, loans and fee income; refer clients to treasury management, capital markets, private banking and wealth | Referral prompts |
| **Credit and advice** | Analyze client financials, recommend credit structures, present loans and take part in approval, within the bank's credit policy | Later, and only as drafts for the portfolio manager (see section 3) |
| **The work around it all** | Meeting prep, follow-ups, call notes and CRM updates | Client brief, meeting follow-up |

## 3. Capabilities, by moment in the RM's work
Each capability is one AI product (glossary). **Comes from** says which need it answers: one of McKinsey's five frontline use cases, our own core use cases (admin off the RM's plate, keep clients), or the RM's job.

| Moment | Capability | What it does | Comes from | Wave |
|---|---|---|---|---|
| **Find business** | Monday opportunity list | Each Monday, the RM's top clients to call, with the reason and the numbers behind it | McKinsey: prospecting and next best opportunities | 1 |
| | Prospect lookalikes | Companies that look like the bank's best clients | McKinsey: prospecting | 2 |
| | Referral prompts | Flags a client need for a partner team (for example treasury management); the RM decides and makes the referral | McKinsey: lead nurturing, including cross-sell | 2 |
| **Before the meeting** | Pre-meeting client brief | One page before each client meeting: the relationship, recent activity, open opportunities and talking points | McKinsey: account intelligence and meeting prep | 1 |
| | Client Q&A | Answers "what should I know about this client?" at any time | McKinsey: account intelligence and meeting prep | 3 |
| **During and after the meeting** | Meeting follow-up | During: Teams transcribes the meeting, only with client consent (without it, the assistant drafts from the RM's own notes), so the RM can listen instead of typing. After: drafts the recap, the follow-up email and the call notes for Salesforce; the RM approves before anything is saved or sent | Our own: admin off the RM's plate | 1 |
| **After the meeting** | AI sales coaching (after calls) | Private guidance for the RM after a call, seen only by that RM | McKinsey: AI sales coaching | 3 |
| **Grow and keep the book** | Early warning | Flags clients who may be drifting away (falling balances, less activity) | Our own: keep clients | 2 |
| **Credit hand-off** | Credit request draft | ⚠️ New idea, not decided: pulls the client's financials into a draft for the portfolio manager. Would take the higher-risk path (control K3) | The RM's job: credit and advice | Not planned |
| **Left out on purpose** | Pricing suggestions; contacting prospects on its own | — | McKinsey: deal scoring and pricing; lead nurturing (full version) | Out (decided 2026-10-15) |

**Wave 1 at a glance:** three capabilities: the pre-meeting client brief, the meeting follow-up and the Monday opportunity list. Together they cover the RM's whole meeting, before, during and after, plus the Monday call list. The order is the hypothesis; dates for waves 2 and 3 are proposed at gate 2 (the Define go/no-go) and confirmed at each wave's own quick-pass gates, once data access and review times are known. How the waves get delivered is in the [RM Assistant Plan](https://claude.ai/artifact/KxPNQLCj6HASThmQpYtfhk).

## 4. The foundation underneath
Built once and shared by every capability, and later by portfolio managers.

| Part | What it is | Used by |
|---|---|---|
| **Client data** | The Salesforce client record and activity; balances, products and trends in Snowflake (certified data only) | Every capability |
| **The RM's own work** | Their calendar, email and Teams meetings (transcripts only with client consent) | Brief, meeting follow-up, AI sales coaching |
| **Outside prospect data** | ⚠️ To confirm: what the bank already licenses | Prospect lookalikes |
| **Signals engine** (the "analytics") | Simple, explainable rules find opportunities and risks in the data; AI writes the reason in plain English and shows the numbers | Opportunity list, referral prompts, early warning, prospect lookalikes |
| **Drafting** | Briefs, recaps, emails and notes, always marked as drafts | Brief, follow-up, Q&A, coaching |
| **Controls and logs** | The limits in section 1, built in once and tested for every capability | Every capability |
| **Feedback loop** | One-click feedback on every output, sorted and fed into the next release | Every capability |

## 5. How we'll know it works
- **More revenue per RM:** pipeline and wins from the assistant's suggestions, against RMs not yet using it [X].
- **More time with clients:** hours saved per week and client-facing hours [X].
- **Use:** RMs using it every week, and the share of suggestions acted on [X].

Targets are [X] until the bank's own numbers are in.

## 6. Portfolio managers next
Portfolio managers (PMs) get the same kind of assistant on the same foundation, with their own capabilities: credit memo and annual review drafts first, early warning second (decided 2026-10-15). It waits until we move into PM work. The credit request draft (section 3) would be where the two assistants meet.

## 7. What to confirm
- Are meeting prep, admin and the Monday call list the RM's biggest needs? How do RMs prepare for and log meetings today?
- Where do RMs spend their day: Salesforce, or Outlook and Teams?
- Is recording client meetings in Teams allowed, and how is consent handled?
- Which client data is certified, and who owns it? What outside prospect data does the bank license?
- How long does the bank's AI review take?

## 8. How it maps to the RM plan
The RM Assistant Plan (rebuilt around the assistant on 2026-10-17) delivers this page: the seven core use cases are the **needs** the capabilities answer, each capability is one AI product, and the product agents (A1 to A5) do the work: A1 and A2 are the signals engine and drafting in the **foundation**; A3, A4 and A5 deliver the capabilities. The plan's old "RM assistant" (wave 3) is the Client Q&A capability here.

_Last updated: 2026-10-18_
