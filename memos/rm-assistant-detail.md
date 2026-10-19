# The RM Assistant: full detail

The detailed working file behind the RM Assistant page. People read the short page (`memos/rm-assistant.md`); this file goes into RM Detail.

> ⚠️ **A hypothesis, not a plan yet** (agreed as our working hypothesis on 2026-10-17). Built from McKinsey's research, the RM plan and public Associated job postings, not from how the bank works today. The first conversations with RM leaders test it; Discover confirms or changes the rest.

## The product in one line
Each relationship manager (RM) gets **their own AI assistant**, inside the tools we expect the RM already uses (Salesforce, Teams and Outlook; ⚠️ to confirm). Its job is to help the RM win business and to free up the time they need to win it. It starts with three **capabilities**, each doing one specific job in the RM's work, and gains more feature wave by feature wave. It is the base everything else builds on: every later AI product for RMs is a new capability of the same assistant.

## 1. A personal AI, with limits
The assistant is personal to each RM, and it is constrained in five ways. These limits are what make it safe to give every RM one.

| Limit | What it means |
|---|---|
| **Jobs** | It does only the capabilities listed on this page. Anything else, it says so and stops. |
| **Workflows** | It works where we expect the RM already works (to confirm in Discover): the Salesforce client record, Teams and Outlook. No new app to learn. |
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
Each capability is one AI product (glossary). The **Need it answers** column names one of McKinsey's five frontline use cases, our own core use cases (admin off the RM's plate, keep clients), or the RM's job.

| Moment | Capability | What it does | Need it answers | Wave |
|---|---|---|---|---|
| **Find business** | Monday opportunity list | Each Monday, the RM's top clients to call, with the reason and the numbers behind it | McKinsey: prospecting and next best opportunities | 1 |
| | Prospect lookalikes | Companies that look like the bank's best clients | McKinsey: prospecting and next best opportunities | 2 |
| | Referral prompts | Flags a client need for a partner team (for example treasury management); the RM decides and makes the referral | McKinsey: lead nurturing, including cross-sell | 2 |
| **Before the meeting** | Pre-meeting client brief | One page before each client meeting: the relationship, recent activity, open opportunities and talking points | McKinsey: account intelligence and meeting prep | 1 |
| | Client Q&A | Answers "what should I know about this client?" at any time | McKinsey: account intelligence and meeting prep | 3 |
| **During and after** | Meeting follow-up | During: Teams transcribes the meeting, only if the bank allows recording and the client consents (without it, the assistant drafts from the RM's own notes), so the RM can listen instead of typing. After: drafts the recap, the follow-up email and the call notes for Salesforce; the RM approves before anything is saved or sent | Our own: admin off the RM's plate | 1 |
| | AI sales coaching (after calls) | Private guidance for the RM after a call, seen only by that RM | McKinsey: AI sales coaching | 3 |
| **Keep the book** | Early warning | Flags clients who may be drifting away (falling balances, less activity) | Our own: keep clients | 2 |
| **Credit hand-off** | Credit request draft | ⚠️ New idea, not decided: pulls the client's financials into a draft for the portfolio manager. Would take the higher-risk path (control K3) | The RM's job: credit and advice | Not planned |
| **Left out on purpose** | Pricing suggestions; contacting clients or prospects on its own | — | McKinsey: deal scoring and pricing; lead nurturing (full version) | Out (decided 2026-10-15) |

**Wave 1 at a glance:** three capabilities: the pre-meeting client brief, the meeting follow-up and the Monday opportunity list. Together they cover the RM's whole meeting, before, during and after, plus the Monday call list. The order is the hypothesis; dates for waves 2 and 3 are proposed at gate 2 (the Define go/no-go) and confirmed at each wave's own quick-pass gates, once data access and review times are known. How the waves get delivered is in the [RM Assistant Plan](https://claude.ai/artifact/KxPNQLCj6HASThmQpYtfhk).

**How each capability is built** (moved here from the full plan on 2026-10-18). Our measures' targets are set in Define; McKinsey's returns for each core use case are outside benchmarks in the [Use Case Library](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X), never our targets.

| Wave | Capability (AI product) | Core use case it answers | Agents | Built mainly on | Our measure (target set in Define) |
|---|---|---|---|---|---|
| **Wave 1** (follow-up live by about week 4; the rest by about week 6; each once its approvals are in) | Pre-meeting client brief | Account intelligence and meeting prep | A3 | Salesforce (Agentforce or Prompt Builder), Snowflake | Prep time per meeting; client-facing hours [X] |
| | Meeting follow-up: recap, email draft and call notes into Salesforce (the RM approves) | Admin off the RM's plate | A3 | M365 Copilot in Teams and Outlook; Salesforce Agentforce for the notes | Hours saved per week; share of meetings logged [X] |
| | Monday opportunity list (deposit and treasury gaps in wave 1) | Prospecting and next best opportunities | A1, A2, then a scheduled Monday send (workflow B1) | Snowflake signals, Power Automate | AI-sourced pipeline and wins, against the comparison group [X] |
| **Wave 2** (dates proposed at gate 2) | Early warning: client may leave | Keep clients | A1, A2 | Snowflake signals, Salesforce | Clients kept, against the comparison group [X] |
| | Referral prompts (for example, RM to treasury specialist) | Lead nurturing, including cross-sell | A1, A2 | Salesforce, Power Automate | Referrals made and won [X] |
| | Prospect lookalikes | Prospecting and next best opportunities | A1, A2 | Snowflake, Salesforce | New clients, against the comparison group [X] |
| **Wave 3** (dates proposed at gate 2) | Client Q&A ("what should I know about this client?") | Account intelligence and meeting prep | A5 | Salesforce Agentforce or Copilot Studio | Questions answered; answer ratings [X] |
| | AI sales coaching (after calls; private to the RM, measured only in aggregate) | AI sales coaching | Spec to come | M365 Copilot (Teams transcripts), Copilot Studio | Coaching used after calls; win rate and new-RM ramp-up time [X] |
| **Left out on purpose** | Pricing suggestions; contacting clients or prospects on its own | Deal scoring and pricing; lead nurturing (the full version) | — | — | — |

**Why wave 1's Monday list suggests only deposit and treasury gaps (decided 2026-10-18):** credit products, such as a line of credit, wait for the portfolio manager work, which avoids a fair-lending review in wave 1 (control K3).

**Why the follow-up and call notes are one capability (decided 2026-10-17):** both
come from the same meeting recap and the same agent (A3), so RMs get one flow:
the recap and email first (live by about week 4: drafted from the RM's own notes,
which we assume needs the least new data and review, ⚠️ to confirm), then saving the call
notes to Salesforce once that's signed off (by about week 6). Teams transcripts come
later, only where the bank allows recording and the client agrees (control K24), so
recording isn't on wave 1's critical path (Elon mode, 2026-10-18). Call notes are in
wave 1 because in McKinsey's survey of about 400 bankers, admin is one of the top
two problems at every stage of the sales funnel (decided 2026-10-10).

**How the follow-up passes its gates.** Because the recap and email go live first, the follow-up passes gates 3 and 4 twice: first for the recap and email (weeks 2–3), then for saving call notes to Salesforce, which is a material change (a new action, a record write) and goes back through step 4 (weeks 4–5; Product Framework, change after launch). Gate 5 is decided once, for wave 1 as a whole, after the brief, the list and call notes have been live for [X] weeks.

**Why there's no how-to helper (decided 2026-10-17):** a pilot group of a few RMs
learns from training on their own clients, champions and a Teams channel. A
separate help agent (A6) was one more build and review for little gain; its
number isn't reused. It can come back if the pilot shows the need.

**Why prospecting and coaching sit where they do (decided 2026-10-15; waves agreed 2026-10-17):**
McKinsey reports its biggest revenue numbers for prospecting, so prospect lookalikes
are in wave 2. AI sales coaching is in wave 3, because it needs call
transcripts, client consent before recording (control K24) and more review. Its agent
spec and workflow are not written yet. Autonomous lead nurturing stays out because nothing reaches a client without the RM;
pricing stays out under control K3 (the AI never sets or suggests a price).

**Why this works:** standard capabilities on platforms the bank already runs
need less build and, we assume, fit existing approvals (⚠️ to confirm). Each feature wave is internal-only and
assistive: the assistant suggests and drafts, and the RM decides. If the bank's
AI review applies to every new capability, the review sets the real pace, which is
why the risk partner is involved from week one.

## 4. The foundation underneath
Built once and shared by every capability, and later by portfolio managers.

| Part | What it is | Used by |
|---|---|---|
| **Client data** | The Salesforce client record and activity; balances, products and trends, which we expect in Snowflake (⚠️ or Fabric; to confirm; certified data only) | Every capability |
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
Portfolio managers (PMs) get the same kind of assistant on the same foundation, with their own capabilities: credit memo and annual review drafts first, early warning second (decided 2026-10-15). It now exists, reviewed (2026-10-19): The PM Assistant page and PM Detail. The credit request draft (section 3) would be where the two assistants meet.

## 7. What to confirm
The one full list is in the full plan, section 8 ("What I'd confirm in the first weeks").

## 8. How it maps to the agents
The seven core use cases are the **needs** the capabilities answer, and each capability is one AI product. The product agents do the work: A1 finds signals and A2 writes the reason for each (the **signals engine**); A3 does the **drafting** (briefs, recaps, emails and call notes); A5 answers client questions (wave 3). The Monday send is a scheduled step in workflow B1, not an agent (A4 was merged into B1 on 2026-10-18).

_Last updated: 2026-10-18_
