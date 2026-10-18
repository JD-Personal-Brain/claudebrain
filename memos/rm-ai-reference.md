# RM Detail

Everything about the relationship manager (RM) work at Associated Bank in one document, for an AI to read. Give this whole document to an AI model so it has the full context: the product, the plan, every step, the agent specs, the workflows and the McKinsey research (the earlier RM audit and market scan are kept as separate working files). People should read the three short pages for people above it in the RM section (the RM Executive Summary, The RM Assistant and the RM Assistant Plan), and can try the RM Assistant Prototype, the fourth row.

> **How to read it (for the AI).** The parts below are the working files, copied in whole and in this order. Later parts give more detail on earlier ones. Lines marked ⚠️ are guesses or hypotheses to confirm at the bank; [X] marks a number not yet known: never invent a value for it. The product is a working hypothesis until Discover with the bank's RMs. Built automatically from the working files; never edit this file by hand.

## Part 1: Executive summary

Working file: `memos/rm-executive-summary.md`.

For the leaders of the relationship manager business · Associated Bank · October 2026

> ⚠️ **A working hypothesis.** Built from outside research and public Associated job postings, not yet from how the bank's relationship managers (RMs) work today. The first conversations with RM leaders test it.

### The problem
RMs win the bank's commercial business, but at many commercial banks they spend only about 25–30% of their time with clients (McKinsey). Much of the rest goes to meeting prep, call notes, updating client records and hunting for the next opportunity. Better insight only pays off if RMs have the time to act on it.

### The product: The RM Assistant
Each RM gets **their own AI assistant**, inside the tools we expect they already use (Salesforce, Teams and Outlook; ⚠️ to confirm). It helps the RM win business and frees up the time to win it. It drafts and suggests; **the RM always decides**. It never contacts a client on its own, never sets or suggests a price and never makes a credit decision. [What it is and all its capabilities](https://claude.ai/artifact/RBaZS636CtycDwZyDrgum2).

### What RMs get first (wave 1)
| Capability | What the RM gets | Why it matters |
|---|---|---|
| **Pre-meeting client brief** | One page before each client meeting: the relationship, recent activity, open opportunities, talking points | Less prep time, better meetings |
| **Meeting follow-up** | The recap, the follow-up email and the call notes for Salesforce, drafted for the RM to approve from the RM's own notes; from the Teams transcript later, only where recording is allowed and the client agrees. Recap and email come first; saving call notes to Salesforce follows once it is signed off | Admin off the RM's plate; better client records |
| **Monday opportunity list** | Each Monday, the clients to call this week, with the reason and the numbers behind it | New revenue from existing clients |

**See it working:** the [RM Assistant Prototype](https://claude.ai/artifact/RFM2o7cdren3TxesQBsjky) runs all three on sample data, with a 2-minute tour.

Later waves add early warning on clients who may leave, referral prompts and prospect lookalikes, then client Q&A and AI sales coaching.

### The value
- **More revenue per RM:** pipeline and wins from the assistant's suggestions. McKinsey reports about 3–15% higher revenue per RM where banks rework a frontline area end to end (an outside benchmark, not our target).
- **More time with clients:** hours saved each week.
- Revenue is proven against similar RMs not yet using it; time is reported as hours saved. Targets are set from the bank's own numbers. [Outside evidence for each core use case](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X#relationship-managers)

### How fast
The build takes days. What sets the pace is approval: each piece goes live once its client data is approved and the bank's AI review signs it off. On our first estimates, to confirm, that's the meeting recap and email by about week 4, then the client brief, Monday opportunity list and call notes by about week 6. The first read on closed revenue comes at about month 6. [The plan, week by week](https://claude.ai/artifact/KxPNQLCj6HASThmQpYtfhk)

**What could slow us down:** not known yet. Possible hold-ups include getting approval to use client data and the bank's AI review, but the real ones are a question for the first conversations (below). If they run long, the meeting recap and email still go first and the rest follows by about week 10.

### What I need, and what I'd confirm
1. A business sponsor for the RM work: about an hour a week, plus each go/no-go decision (our estimate).
2. Time with 6–10 RMs and their managers, about two hours each in the first two weeks (our estimate), and a willing pilot group.
3. Named owners for the client data (in Salesforce and Snowflake; ⚠️ to confirm).
4. An early risk partner, reviewing each version as it's built.

To confirm in the first weeks: what usually holds up a new AI tool here; which revenue lever matters most now (new, growing or keeping clients); how RMs are measured and paid today; how long the AI review takes and whether recording client meetings in Teams is allowed; and what team and budget the pilot has.

## Part 2: The product: The RM Assistant (short version for people)

Working file: `memos/rm-assistant.md`.

> ⚠️ **A working hypothesis** (agreed 2026-10-17), built from outside research and public Associated job postings. The first interviews with the leaders of relationship managers (RMs) and with RMs confirm or change it.

### The product in one line
Each RM gets **their own AI assistant**, inside the tools we expect they use (Salesforce, Teams and Outlook; ⚠️ to confirm), to help them win business and free up the time to win it. It starts with three **capabilities** and gains more, feature wave by feature wave. Every later AI product for RMs is a new capability of the same assistant.

### 1. Its limits
These limits make it safe to give every RM one.
- **Jobs:** only the capabilities below. Anything else, it says so and stops.
- **Workflows (where it works):** the Salesforce client record, Teams and Outlook (⚠️ to confirm). No new app.
- **Data:** client data the bank has approved as trusted (certified), only for the clients the RM may already see, plus the RM's own calendar, email and meetings.
- **Controls:** it drafts and suggests; the RM approves anything saved or sent. It never contacts a client, never makes a credit decision and never sets or suggests a price. Meetings are recorded only with client consent. Everything is logged.
- **Feedback:** one click on every output (use, change or reject), which steers what gets better next.

### 2. Capabilities, by moment in the RM's work
Each capability is one AI product and answers one core use case (see the [Use Case Library](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X#relationship-managers) for the value and the research).

| Moment | Capability | What it does | Core use case | Wave |
|---|---|---|---|---|
| **Find business** | Monday opportunity list | Each Monday, the top clients to call, with the reason and the numbers | Prospecting and next best opportunities | 1 |
| | Prospect lookalikes | Companies that look like the bank's best clients | Prospecting and next best opportunities | 2 |
| | Referral prompts | Flags a client need for a partner team, such as treasury management | Lead nurturing, including cross-sell | 2 |
| **Before the meeting** | Pre-meeting client brief | One page before each client meeting | Account intelligence and meeting prep | 1 |
| | Client Q&A | Answers the RM's own questions about a client at any time, with the source for each answer | Account intelligence and meeting prep | 3 |
| **During and after** | Meeting follow-up | Drafts the recap, the follow-up email and the call notes for Salesforce from the RM's own notes (from the Teams transcript later, only where recording is allowed and the client agrees); the RM approves before anything is saved or sent | Admin off the RM's plate | 1 |
| | AI sales coaching | Private guidance for the RM after a call | AI sales coaching | 3 |
| **Keep the book** | Early warning | Flags clients who may be drifting away | Keep clients | 2 |
| **Left out on purpose** | Pricing suggestions; contacting clients or prospects on its own | Kept out to protect fair lending and client trust | Deal scoring and pricing; lead nurturing (the full, automated version) | Out |

### 3. What it's built on
Every capability runs on one shared foundation, built once:
- client data from Salesforce and Snowflake (⚠️ to confirm);
- the RM's own calendar, email and meetings (transcripts only with client consent);
- outside prospect data the bank licenses (⚠️ to confirm);
- a **signals engine**: simple, explainable rules spot opportunities and risks, and AI explains each one in plain English with the numbers;
- drafting, and the controls and feedback above.

Every detail (the RM's job, the foundation part by part, what to confirm) is in [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n), for AI to read. To see the assistant working, try the [RM Assistant Prototype](https://claude.ai/artifact/RFM2o7cdren3TxesQBsjky).

## Part 3: The RM Assistant in full detail

Working file: `memos/rm-assistant-detail.md`.

The detailed working file behind the RM Assistant page. People read the short page (`memos/rm-assistant.md`); this file goes into RM Detail.

> ⚠️ **A hypothesis, not a plan yet** (agreed as our working hypothesis on 2026-10-17). Built from McKinsey's research, the RM plan and public Associated job postings, not from how the bank works today. The first conversations with RM leaders test it; Discover confirms or changes the rest.

### The product in one line
Each relationship manager (RM) gets **their own AI assistant**, inside the tools we expect the RM already uses (Salesforce, Teams and Outlook; ⚠️ to confirm). Its job is to help the RM win business and to free up the time they need to win it. It starts with three **capabilities**, each doing one specific job in the RM's work, and gains more feature wave by feature wave. It is the base everything else builds on: every later AI product for RMs is a new capability of the same assistant.

### 1. A personal AI, with limits
The assistant is personal to each RM, and it is constrained in five ways. These limits are what make it safe to give every RM one.

| Limit | What it means |
|---|---|
| **Jobs** | It does only the capabilities listed on this page. Anything else, it says so and stops. |
| **Workflows** | It works where we expect the RM already works (to confirm in Discover): the Salesforce client record, Teams and Outlook. No new app to learn. |
| **Data** | Client data: certified data only. It also uses the RM's own calendar, email and meetings (transcripts only with consent) and any outside prospect data the bank licenses. Client data is always limited to the clients the RM is already allowed to see. |
| **Controls** | It drafts and suggests; the RM approves anything saved or sent. It never contacts a client on its own, never makes a credit decision and never sets or suggests a price. Meetings are recorded only with client consent. Everything it does is logged. |
| **Feedback** | Every output has one-click feedback (use, change or reject, with a reason). The feedback steers what gets better next. |

### 2. What an RM's job is
From Associated's public RM postings (seen through search results on job boards, 2026-10-17; ⚠️ check against the bank's own careers site):

| Part of the job | What it means | Where the assistant helps |
|---|---|---|
| **Find new business** | Prospecting: steady calling, centers of influence, new clients | Prospect lookalikes |
| **Grow and keep the book** | Manage a book of middle-market business clients; keep and deepen each relationship | Monday opportunity list, early warning, client briefs |
| **Cross-sell and refer** | Bring in deposits, loans and fee income; refer clients to treasury management, capital markets, private banking and wealth | Referral prompts |
| **Credit and advice** | Analyze client financials, recommend credit structures, present loans and take part in approval, within the bank's credit policy | Later, and only as drafts for the portfolio manager (see section 3) |
| **The work around it all** | Meeting prep, follow-ups, call notes and CRM updates | Client brief, meeting follow-up |

### 3. Capabilities, by moment in the RM's work
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

### 4. The foundation underneath
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

### 5. How we'll know it works
- **More revenue per RM:** pipeline and wins from the assistant's suggestions, against RMs not yet using it [X].
- **More time with clients:** hours saved per week and client-facing hours [X].
- **Use:** RMs using it every week, and the share of suggestions acted on [X].

Targets are [X] until the bank's own numbers are in.

### 6. Portfolio managers next
Portfolio managers (PMs) get the same kind of assistant on the same foundation, with their own capabilities: credit memo and annual review drafts first, early warning second (decided 2026-10-15). It waits until we move into PM work. The credit request draft (section 3) would be where the two assistants meet.

### 7. What to confirm
The one full list is in the full plan, section 8 ("What I'd confirm in the first weeks").

### 8. How it maps to the agents
The seven core use cases are the **needs** the capabilities answer, and each capability is one AI product. The product agents do the work: A1 finds signals and A2 writes the reason for each (the **signals engine**); A3 does the **drafting** (briefs, recaps, emails and call notes); A5 answers client questions (wave 3). The Monday send is a scheduled step in workflow B1, not an agent (A4 was merged into B1 on 2026-10-18).

## Part 4: The plan (short version for people)

Working file: `memos/rm-plan.md`.

How The RM Assistant gets delivered to relationship managers (RMs) · Associated Bank · October 2026

[RM Executive Summary](https://claude.ai/artifact/LPPq2gt5PSoiB8GzX8ZBE2) · [The RM Assistant](https://claude.ai/artifact/RBaZS636CtycDwZyDrgum2) · [RM Assistant Prototype](https://claude.ai/artifact/RFM2o7cdren3TxesQBsjky) (see it working) · [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n) (everything in full) · [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ) (the rules every product follows)

### The plan at a glance
The first 13 weeks (about 90 days), as estimates to confirm in the first days. Each live bar starts only once its client data is approved and the bank's AI review signs it off, so the bars move with those approvals. Week 1 starts at kickoff. Gates (◆) are go/no-go decisions; the data contract is the signed list of client data the assistant may use. Each row links to its detail in RM Detail.

```gantt
weeks 13
Kickoff and a working prototype on sample data | 0 | 1 | build | https://claude.ai/artifact/RFM2o7cdren3TxesQBsjky
Gate 1: target, measure and baseline (from first sizing) agreed | 1 | 1 | gate | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-4-how-the-work-flows
Interviews with RMs, improving the prototype every few days | 0 | 2 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Gate 2: client data approved, risk level rated, business case agreed | 2 | 2 | gate | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-4-how-the-work-flows
Meeting recap and email: set up and tested, signed off after gate 2 | 1 | 3 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
**Meeting recap and email live** | 3 | 13 | live | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Brief, opportunity list and call notes: built and tested on real data | 1 | 5 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Sign-offs for the brief and list, plus a separate one to save call notes in Salesforce | 3 | 5 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
**Brief, opportunity list and call notes live** | 5 | 13 | live | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Small releases every week or two | 6 | 13 | ongoing | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
```

The recap and email can move first because they're drafted from the RM's own notes, not client account data or meeting recordings (our assumption, to confirm: it needs the least review), and the risk partner reviews each version as it's built. Interviews keep going after gate 1 to refine the target. Waves 2 and 3 get proposed dates at gate 2, once data access and review times are known.

### 1. What could slow us down (to confirm)
The real blockers aren't known yet; they're a first question for the bank. Possible ones:
- **Approval to use client data.** Nothing reaches pilot RMs on real client data until the people responsible for it approve which data the assistant may use.
- **The bank's AI review.** Nothing goes live until risk, compliance, privacy and security sign off. To keep that short, the risk partner reviews each version as it's built, so the sign-off has no surprises.
- **Backup plan.** If either runs long, the meeting recap and email go first (drafted from the RM's own notes, which we assume needs the least new data and review), and the rest stays ready in the test environment, live by about week 10. The call is made at gate 2.

Detail: [the backup plan and the six conditions for moving fast](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate).

### 2. Who decides
| Role | For the RM project |
|---|---|
| Sponsor | A commercial banking leader [name needed]: the outcome, funding and every gate |
| User leaders | RM leaders and market managers: choose the pilot group, use the assistant in a team meeting they already run, such as a weekly pipeline meeting (⚠️ to confirm), and decide with the sponsor whether to scale |
| Pilot RMs | Co-design and test; their feedback steers what gets built |
| Data owners | The client data, in Salesforce and Snowflake (⚠️ to confirm) [names needed]: sign the data contract |
| Risk partner | Rates the product's risk and approves it before it reaches RMs; the sponsor can't overrule that approval |
| Compliance, privacy and security | Sign off before it reaches RMs |
| Finance | Agrees how results are counted, and joins the sponsor for the quarterly call to invest more, adjust or stop |
| Sales leadership and HR | Whether acting on the assistant's insights counts in how RMs are measured and paid |

Detail: [who's involved and who decides](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-3-who-s-involved-and-who-decides).

### 3. How we'll prove the value
- **Revenue:** pipeline and wins from the assistant's suggestions, against similar RMs not yet using it. Every AI-sourced opportunity is tagged in Salesforce from day one, and Finance agrees the method before the pilot.
- **Time:** hours saved per week and client-facing time, reported as hours, not turned into revenue.
- **Use:** pilot RMs active each week, and the share of suggestions acted on.
- **Payback:** the target is set at gate 2 from the bank's own numbers, as are all the other targets.

Detail: [the value model](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-2-the-value-model).

### 4. Top risks
| Risk | How I'd handle it |
|---|---|
| Data access or the AI review takes longer | Start both on day one; keep wave 1 internal, to drafts and suggestions the RM checks, on platforms we expect the bank has already approved (⚠️ to confirm) (the backup plan is in section 1) |
| RMs don't trust the insights | Show the reason and the numbers behind every insight; build it with pilot RMs; managers use it in their routines |
| Client records (CRM) may be incomplete (⚠️ to confirm) | Lean on account data first; approved call notes improve the records over time |
| Incentives don't reward acting on insights | Agree recognition for AI-sourced wins with sales leadership before launch |
| Client privacy in recorded meetings | Record only with client consent and under any recording policy the bank has (⚠️ to confirm); notes stay drafts until the RM approves |

Detail: [every risk and how I'd handle it](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-7-top-risks-and-how-i-d-handle-them).

## Part 5: The full delivery plan, with every step, agent spec and workflow

Working file: `memos/rm-analytics-framework.md`.

Principal Applied AI Product Manager · Associated Bank · October 2026 (memo v11, 2026-10-18)

The detail behind the three short RM pages (the RM Executive Summary, The RM Assistant and the RM
Assistant Plan), read in RM Detail. What the product is, its capabilities and waves, and the decisions
behind them are in RM Detail, Part 3 (The RM Assistant in full detail); the rules every product follows are in the
[Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ) and aren't repeated here.
Appendix A specifies the product's agents and Appendix B its workflows (B1 to B9), so the team can
build directly from them. It is a working hypothesis until Discover with the bank's RMs.

**The limiting factor: not known yet.** ⚠️ The real blockers are a first question
for the bank (what usually holds up a new AI tool there?). Possible ones, our
assumptions to confirm: approval to use client data (the data contract, the signed
list of data the product may use, needs the data owners' signatures [names needed];
aimed for week 2), and the bank's AI review, which for the very first capability
(the follow-up's recap and email, in M365 Copilot) would matter most, together with
any recording policy the bank has.

---

### 1. The outcome

The assistant has two goals that work together:

- **More revenue opportunities:** better insight into which clients to call, and why.
- **More time to act on them ("banker capacity"):** less time on meeting prep, call notes and CRM updates.

New revenue can come from three places. Finding out which is biggest is the
first job:

| Lever | What the assistant looks for | Capabilities |
|---|---|---|
| **Win new clients** | Prospects that look like our best clients, and referrals from other parts of the bank | Prospect lookalikes |
| **Grow existing clients** | Clients who need a product they don't have yet, such as treasury management, including referrals between teams (for example, RM to treasury specialist) | Monday opportunity list, referral prompts |
| **Keep clients** | Early signs a client may leave, such as falling balances or less activity | Early warning |

---

### 2. The value model

The business case is built in Discover from real data. The structure is set
now, and the **[X]** values are filled in with the bank's numbers, not
invented here.

| Part | How it's calculated |
|---|---|
| **Revenue from insights** | RMs in scope [X] × qualified opportunities surfaced per RM per month [X] × share acted on [X]% × win rate [X]% × average first-year revenue per win [$X] |
| **Time freed** | RMs in scope [X] × hours saved per week [X]. Reported as hours and client-facing time, not turned into revenue: any revenue that time creates already shows up in the results against the comparison group, so counting it again would count the same win twice (decided 2026-10-17) |
| **Costs** | Licenses (for example, Copilot or Agentforce seats) + build effort + running costs (AI usage, data) + change management |
| **Net value** | Revenue above the comparison group, minus costs. Target payback: [X] months, judged for wave 1 as a whole; the time savers are judged on hours freed and client-facing time against an hours target the sponsor agrees [X], not on payback |

Each core use case gets its own line once targets are set in Define.

**How it's proven:** pilot RMs are compared with similar RMs not yet using
the assistant, and every AI-sourced opportunity is tagged in Salesforce from day
one. Finance agrees the method before the pilot starts.

---

### 3. Who's involved and who decides

The roles, what each one decides and the gates each joins are set once in the
[Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ). For the RM project they are:

| Role (Product Framework) | For the RM project |
|---|---|
| Sponsor | A commercial banking leader [name needed] |
| User leaders | RM leaders and market managers: they choose the pilot group, use the assistant's insights in the weekly pipeline meeting, or whatever team meeting managers already run (⚠️ to confirm), and decide with the sponsor whether to scale (gate 5) |
| Pilot users | Pilot RMs: they co-design and test, and their feedback steers the backlog |
| Data owners | The owners of the client data, which we expect sits in Salesforce and Snowflake (⚠️ to confirm) [names needed] |
| Platform teams | Salesforce, Microsoft, AWS and data engineering (⚠️ to confirm how the bank's teams are set up) |
| Long-term owner | To be decided by a date set in Define (sub-step 2.8); confirmed before scaling (5.7); for example, someone in a revenue line |
| Also for RMs: sales leadership and HR | Whether acting on the assistant's insights is recognized in how RMs are measured and paid |

The risk partner, compliance, privacy and security (who sign off at step 4), vendor risk, IT, Finance
(who joins the sponsor for the quarterly invest, adjust or stop call), Analytics and Operations join as the Product Framework sets out; the risk partner's
step 4 approval can't be overruled by the sponsor. No planned RM capability
takes the higher-risk path, so the credit policy owner isn't involved; any insight
that suggests a credit product goes to compliance (control K3; none in wave 1, whose list suggests only deposit and treasury gaps).

**Keeping partners aligned.** Decisions go in the decision log, and dependencies,
risks and issues in the risk and issue list (Product Framework). Its top item is
the limiting factor, named with its owner once the bank confirms what is actually
holding the work up (⚠️ not known yet).

---

### 4. How the work flows

Six steps, each ending in a go/no-go gate, run as the [Product Workflow](https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv)
sets out: its questions, gates and sub-steps (the Product Playbook) aren't repeated here. The first pass
overlaps: a working prototype in week 1, wave 1 live in about weeks 2–6 (the meeting follow-up first);
then steps 3–6 repeat in cycles of a week or two, and each new feature wave takes the quick pass through
Discover and Define (Product Framework). Governance runs through every step; step 4 is the formal approval,
not the first time risk partners see the product. What's different for RMs:

| Step | Gate for RMs | What's specific to RMs | General agents used (the analysis agents, M20 to M33; M1 to M19 run every step as the Product Machine sets out) |
|---|---|---|---|
| **1. Discover** | The sponsor, with the risk partner, agrees the target lever, the main measure and today's baseline (from a first rough sizing; confirmed at gate 2), and confirms the wave 1 capabilities | Frame "new revenue" as three levers (section 1) and two goals; size them with pipeline, win/loss, balances and products; interview and shadow RMs and managers, starting from the RM user workflow (how they find opportunities today, and what gets in the way); learn how RMs are measured and paid; test the prototype on sample data every few days | M20 interview synthesizer (Teams transcripts only with consent), M21 opportunity sizer, M22 time-use analyst |
| **2. Define** | The brief, data contract and risk rating agreed; the full set of measures and the value model show payback within [X] months; dates proposed for waves 2 and 3 | The data contract covers documents too (meeting recaps and call transcripts: their source, owner, re-indexing and who may see them); the risk intake lists consent before recording (control K24) for the meeting follow-up; Finance agrees how AI-sourced revenue is tagged and compared; any insight that suggests a credit product, such as a line of credit, is reviewed by compliance (control K3: the AI never makes a credit decision and never sets or suggests a price; fair-lending rules apply to business credit too) | M23 requirements drafter, M24 data contract checker (then on every data refresh), M25 risk intake assistant |
| **3. Build** | Meets the quality bar in testing; every control is built and passes its control test | Simple, explainable rules find the opportunities and AI only explains them (K22); every insight shows the numbers behind it (K7); one-click use, change or reject with a reason (K1); each RM sees only clients they may already see (K4); filters block sensitive data and off-topic answers (K8); every AI action logged (K12); the test set uses real client examples graded by experienced RMs | M26 test grader |
| **4. Govern and test** | All sign-offs recorded and the monitoring plan agreed, for each AI product | Register the product in the bank's model inventory (⚠️ to confirm) and confirm its rating (model risk guidance SR 11-7; ⚠️ SR 26-2 may replace it, item W17); red-team for other RMs' clients and credit requests; check opportunities are spread fairly across client segments and regions; show consent captured before any recording (K24); the monitoring plan watches the share of recaps from consented recordings versus the RM's own notes | M27 red-team agent, M28 fairness monitor (then monthly), M29 evidence pack assembler |
| **5. Release and adopt** | Weekly use and leading results hit targets (at least [X]% of pilot RMs active weekly, at least [X]% of insights acted on); no serious incidents; long-term owner confirmed before scaling | A pilot group of RMs and their managers, with a comparison group; build it into a routine managers already run, such as a weekly pipeline meeting (⚠️ to confirm), so use becomes a habit; train on RMs' own clients; champions and a Teams channel answer "how do I…?"; recognize AI-sourced wins with sales leadership | M30 feedback triage |
| **6. Measure and iterate** | Each month, keep, change or stop each AI product; each quarter, the sponsor with Finance decides to invest more, adjust or stop, on results against the comparison group | Leading measures first (insights acted on, pipeline created, client time gained), visible within weeks; closed revenue against the comparison group from about month 6; plus cost per active RM and per acted-on insight, because the goal is a product that pays for itself | M31 impact analyst, M32 quality watchdog, M33 improvement scout |

---

### 5. How we deploy AI

The AI principles (assistive first, cut first then automate, one job each, built
where the work happens) are the Product Framework's; the assistant's own limits
(its jobs, workflows, data, controls and feedback) are on The RM Assistant page.
What's specific to RMs:

**Choosing the platform.** The pilot picks one delivery platform, using five criteria:
1. Where RMs spend most of their day.
2. What data the assistant needs, and where it lives.
3. Fit with the bank's existing approvals and controls.
4. Cost model (per user vs. per use).
5. Speed to a working pilot.

**Starting point, our assumption to confirm in Discover:** if RMs work mainly in Salesforce,
show insights on the Salesforce client record (Agentforce, Prompt Builder),
with Snowflake (or Fabric; which holds what is to confirm) as the data and signal engine. Send the Monday opportunity list through
Teams or Outlook (Power Automate). Keep to as few AI paths as wave 1 needs: M365 Copilot for the meeting
follow-up's recap and email, and one Salesforce path (Agentforce or Prompt Builder) for insights, the brief and call notes. Add AWS
Bedrock only where custom AI work is needed beyond that. Every extra platform adds build work and another review.

**What ships when:** in feature waves of capabilities (the capabilities and their waves are in RM Detail, Part 3, section 3),
with a release every week or two in between.

**The data flywheel.** The meeting follow-up's call notes, which RMs approve,
also improve the quality of the client records (the CRM). Better data makes better
insights; better insights earn more use; more use produces more data. That
loop compounds over time and is a reason to build both goals together.

**The quality bar for RMs.** The tests and who may accept a gap are the Product
Framework's; thresholds are set in Define. For RMs, accuracy means every number
in an insight matches the source data, and permissions mean no RM ever sees a
client they aren't allowed to see (zero tolerance).

---

### 6. The project plan (estimate)

Building starts on day one. With today's AI tools, a working version takes
days, not months, so the plan is organized around what most often holds banks
up (our assumption for Associated, to confirm): access to real client data and sign-off from the AI review. The risk
partner sees each version as it is built. Weeks are estimates to confirm in
the first days.

**What lets us move this fast.** Six conditions, each checked in the first days:

| Condition | Why it matters | Checked by |
|---|---|---|
| **1. Build from day one** | A working prototype on sample data in week 1; no real client data is needed until it's tested. | Product manager, platform team, week 1 |
| **2. Standard features only** | Wave 1 configures features already in Salesforce, M365 Copilot and Power Platform, which we assume already have bank approval for this kind of use (⚠️ to confirm with IT and risk in week 1). | Product manager, platform teams, week 1 |
| **3. Low risk by design** | Internal only, assistive, read-only by default, nothing near credit decisions or pricing. We expect a low rating (⚠️ the risk partner decides). | Risk partner gives an early rating, week 2 |
| **4. Review as we go** | The risk partner sees each version as it's built, so sign-off confirms what they already know. | Product manager and risk partner, every week |
| **5. Data access on day one** | Requests go in on day one and wave 1 uses only certified data, because access is often the slowest step. | Data owners sign the data contract, week 2 |
| **6. Fast decisions** | Each gate is decided within days, in writing when every criterion is met, because waiting for decisions adds weeks. | Sponsor, with the people named for each gate |

**Backup plan if data access or review runs long.** The meeting follow-up's
recap and email go first: they're drafted from the RM's own notes in M365 Copilot (Teams transcripts
come later, only where recording is allowed and the client agrees, control K24), so we assume they
need the least new data and review (⚠️ to confirm). RMs keep shaping the brief,
opportunity list and call notes in the test environment, so they're ready the day access and
sign-off land, by about week 10. The dates for later waves, proposed at gate 2, allow for it. The
call is made at gate 2 (week 2).

**Wave 1: the first six weeks**

| Week | What gets done | Owner | Proof it's done |
|---|---|---|---|
| Days 1–5 | Sponsor kickoff; risk partner briefed; data access and test environments requested; working prototype built on sample data; a first rough sizing of the levers | Product manager, platform team | Prototype shown to the sponsor |
| 1 | **Gate 1:** the sponsor, with the risk partner, sees the prototype and agrees the target lever, the main measure and today's baseline (from a first rough sizing in days 1–5; confirmed at gate 2), and confirms wave 1 | Sponsor, with the risk partner | Decision log entry |
| 1–2 | RM interviews and shadowing with 6–10 RMs and their managers (our estimate), using the prototype; improve it every few days; sizing of the levers refined | Product manager, pilot RMs, analyst | RM feedback log; sized levers |
| 2 | **Gate 2:** data contract, early risk rating, the full set of measures and the value model, Finance attribution method, dates proposed for waves 2 and 3; split decision if needed | Sponsor, data owners, risk partner | Signed data contract; early risk rating |
| 2–3 | Recap and email set up in M365 Copilot: a small test set graded by RMs (gate 3); controls tested, including consent before recording (K24); evidence pack and sign-offs (gate 4); readiness for this part: incident dry run, comparison group, training | Platform team, risk partner, operations | Gate 3 and gate 4 entries in the decision log; readiness checklist |
| About 2–4 | **Meeting follow-up live with pilot RMs** | Product manager | First weekly usage report |
| 2–5 | Connect real data in the test environment; build the test set and evidence pack; risk partner reviews each version | Platform teams, product manager | Test results against the quality bar |
| 4–5 | Sign-offs for the brief, the opportunity list and saving call notes (a material change to the follow-up, back through step 4); release readiness (training, support, incident process, comparison group) | Risk, compliance, privacy, security, operations | Sign-offs recorded; readiness checklist complete |
| About 4–6 | **Client brief, Monday opportunity list and call notes into Salesforce live with pilot RMs** | Product manager | Usage and act-on rates in Power BI; share of meetings logged |

**By day 90 (about week 13):** wave 1 has been live with pilot RMs for about
two months and leading measures are coming in (if the backup plan is used, the recap and email are still live from about week 4; the rest has about three weeks). How far waves 2 and 3 have
got depends on the dates proposed at gate 2 and confirmed at each wave's quick-pass gates.

---

### 7. Top risks and how I'd handle them

| Risk | How I'd handle it |
|---|---|
| **CRM data may be incomplete** (common at banks when RMs skip logging; ⚠️ to confirm) | Lean on account data first (we expect it in Snowflake); the time-saving features improve CRM data over time (the flywheel) |
| **RMs don't trust the insights** | Show the reason and the numbers behind every insight; co-design with pilot RMs; managers model use |
| **Governance takes longer than planned** | Brief risk partners in week one; keep each feature wave low-risk, internal-only and on approved platforms; build the evidence pack as we go; if it still runs long, split wave 1 (see the backup plan in section 6) |
| **Incentives don't reward acting on insights** | Agree recognition for AI-sourced wins with sales leadership before launch |
| **Costs grow with usage** | Track cost per active RM; use the smallest AI model that meets the quality bar |
| **Revenue attribution is disputed** | Agree the comparison-group method and tagging with Finance in Define |
| **Data access takes longer than planned** | Request access on day one; start with data that's already certified; keep the first release's data needs small |
| **Client privacy in recorded meetings** | Client consent and any recording policy the bank has (⚠️ to confirm) apply; notes are drafts until the RM approves |

---

### 8. What I'd confirm in the first weeks

This approach is built on the platforms named in the role: Salesforce,
Snowflake, Microsoft Fabric and Power BI, Microsoft 365 Copilot, Power
Platform and AWS Bedrock. I've been told all of them are live, so the plan
builds on them. I'd confirm early (this is the one full list; the Executive Summary asks the top few):

- What usually holds up a new AI tool at the bank?
- Which revenue lever matters most to the business right now?
- How will success be judged in the first 6 months?
- Which RM teams would make a good pilot group?
- Who owns the client data in Snowflake and Salesforce?
- How are RMs measured and rewarded today?
- How long does AI governance review usually take?
- Is recording client meetings in Teams allowed, how is consent captured, and who owns the recording policy?
- What team and budget are available for the pilot?
- How each platform is set up for RMs today: which features, licenses and connections? Do RMs work mainly in Salesforce, or in Outlook and Teams?
- Which client data sits in Snowflake and which in Fabric?
- Do managers run a weekly pipeline meeting, or another team routine the assistant could plug into?

---

### Appendix A: Agent specs

The product's own agents. AI sales coaching (wave 3): agent spec not written
yet (step 4 of the use case kit, item W3 in the Open Items log). The product's agents (A1, A2, A3 and A5) are written so a
platform team can build them and a risk partner can review them; the team's
agents are the product machine's general agents, specified in full in the
agent library. **[X]** values are set in Define.

**Rules for every agent:**
- **One job.** If a request falls outside it, the agent says so and stops.
- **Read-only by default.** Any change to a record, or anything that reaches a client, needs a named person's click.
- **Approved models and data only.** Uses only AI models and data sources approved for this product.
- **Never guesses.** If its inputs are missing, stale or fail a check, it stops and alerts its owner rather than producing a weaker answer.
- **Everything logged.** Each run records who, what, when, which sources and what it produced, for audit and for measuring.

#### Agents RMs use (the product)

**A1. Signal finder** · wave 1 · runs on Snowflake (Cortex)
- **Job:** each night, scan each RM's clients for opportunity signals using the agreed rules and scores (product gaps, deposit and treasury only in wave 1; from wave 2, early warnings and referral needs). From wave 2, also monthly: find prospect lookalikes in the licensed prospect data, using the criteria compliance approves.
- **Inputs:** certified Snowflake views of balances, products, activity and trends; the rule set owned by the business; from wave 2, the licensed prospect data named in the data contract.
- **Allowed actions:** read the certified views and the licensed prospect data; write signals to a signals table.
- **Not allowed:** contacting clients; changing Salesforce; inventing signals outside the rule set.
- **Outputs:** a list of signals per RM, each with the rule that fired and the numbers behind it.
- **Stops when:** every in-scope client has been scanned, or the data is older than [X] hours (then it alerts the data owner and produces nothing).
- **Proof it worked:** run log with clients scanned and signals found; a sample of signals matches the source numbers exactly.
- **Person in charge:** business owner of the rules; data owner for the inputs.

**A2. Insight writer** · wave 1 · runs on Salesforce Prompt Builder (or AWS Bedrock if needed)
- **Job:** turn each signal into a plain-English reason, talking points and a suggested next step, citing the numbers.
- **Inputs:** signals from A1; the Salesforce client record.
- **Allowed actions:** read signals and the client record; write a draft insight to the assistant's own insights panel, shown on the client record; it changes no client record field.
- **Not allowed:** recommending credit decisions or pricing; stating any number not in its inputs.
- **Outputs:** one insight per signal, with its sources shown.
- **Stops when:** every signal has an insight, or a guardrail blocks one (logged and sent to the product manager).
- **Proof it worked:** test-set score meets the quality bar (accuracy, sources, relevance); every number traces to the source.
- **Person in charge:** the RM decides whether to act; the product manager owns quality.

**A3. Prep and follow-up assistant** · wave 1 · runs on Salesforce Agentforce or M365 Copilot
- **Job:** before a client meeting, draft a one-page brief. After it, draft the recap, follow-up email and call notes for Salesforce.
- **Inputs:** the Salesforce client record; open insights; the RM's calendar; the Teams meeting recap (recorded only with client consent) or the RM's own notes.
- **Allowed actions:** read the inputs; create drafts for the RM; save an approved call note to Salesforce, tagged "AI-drafted", only after the RM's click.
- **Not allowed:** sending anything to a client; saving to Salesforce without the RM's approval.
- **Outputs:** a brief, a recap, a draft email and draft call notes, all marked as drafts.
- **Stops when:** the drafts are delivered to the RM. If there's no recording or consent, it drafts from the RM's own notes or asks for them.
- **Proof it worked:** the RM approves or edits each draft (logged); share of drafts used with light edits ≥ [X]%.
- **Person in charge:** the RM approves before anything is saved or sent.

**A5. Client Q&A** · wave 3 · runs on Salesforce Agentforce or a Copilot Studio agent in Teams
- **Job:** answer "what should I know before my call with this client?" and similar questions.
- **Inputs:** Salesforce and Snowflake, read-only, only clients the RM is allowed to see.
- **Allowed actions:** read; answer with sources; propose a record update for the RM to click.
- **Not allowed:** answering about clients outside the RM's permissions; giving credit or pricing advice.
- **Outputs:** an answer with its sources, or "I don't have that information."
- **Stops when:** the question is answered, or it is out of scope (it says so and names who can help).
- **Proof it worked:** test-set score meets the quality bar; zero permission breaches in red-team testing.
- **Person in charge:** the RM; the product manager for quality.

A4 (the weekly opportunity digest) was merged into workflow B1 on 2026-10-18: it is a scheduled Monday send with no AI in it, so it is a step, not an agent. A6 (a how-to helper) was removed on 2026-10-17: champions and a Teams channel answer "how do I…?" questions in the pilot. Neither number is reused.

#### Agents the team uses

The team uses the product machine's general agents, specified in full in the
[Agent Library](https://claude.ai/artifact/Cn9nANQoqp2BP7yrmy61zn): for RMs, M20 to M22 in Discover
(interviews, sizing, time use), M23 to M25 in Define (requirements, data contract, risk intake),
M26 in Build (test grading), M27 to M29 in Govern and test (red-teaming, fairness, evidence pack),
M30 in Release and adopt (feedback triage) and M31 to M33 in Measure and iterate (impact,
quality watchdog, improvement scout). Which ones each step uses is in section 4.

### Appendix B: Workflows

Each RM-facing capability as a step-by-step flow. Every RM-facing flow (B1–B8)
has one **decision point** where the RM decides, and everything is logged.
B9 is the release routine behind them. AI sales coaching (wave 3): workflow not
written yet (step 4 of the use case kit, item W3 in the Open Items log).

**B1. Monday opportunity list** (wave 1)
- **Trigger:** every night (signals); every Monday morning (the Monday send).
- **Steps:** 1. A1 scans clients and writes signals. 2. A2 writes an insight for each. 3. Insights appear in the assistant's panel on the Salesforce client record (no record field changes). 4. Every Monday, a scheduled send (Power Automate) messages each RM their top [X] insights in Teams or Outlook, ranked by the agreed score, with links to each client record; it messages only the RM (and, if agreed, their manager), and sends a short "nothing new" note when there's nothing. 5. **Decision point:** the RM accepts, rejects (with a reason) or changes each insight. 6. On accept, the RM creates an opportunity in Salesforce, tagged "AI-sourced." 7. M30 sorts the feedback. 8. Managers review the list in the weekly pipeline meeting, or whatever team meeting they already run (⚠️ to confirm).
- **Logged:** signals, insights, Monday sends, opens, decisions and reasons, opportunities created.
- **Measures:** share of insights acted on; pipeline from AI-sourced opportunities.

**B2. Pre-meeting client brief** (wave 1)
- **Trigger:** a client meeting on the RM's calendar, [X] hours before; or the RM asks.
- **Steps:** 1. A3 pulls the client record, open insights and recent activity. 2. It drafts a one-page brief with sources. 3. The brief reaches the RM in Teams or Outlook. 4. **Decision point:** the RM uses it and rates it with one click.
- **Logged:** briefs created, opened and rated.
- **Measures:** briefs used; prep time saved (RM survey); rating.

**B3. Meeting follow-up: recap and email** (wave 1; first in the backup plan)
- **Trigger:** a client meeting ends.
- **Steps:** 1. M365 Copilot produces the recap (from a recording only with client consent; otherwise from the RM's notes). 2. A3 drafts the follow-up email and action items. 3. **Decision point:** the RM edits and sends it themselves. Nothing is sent automatically.
- **Logged:** drafts created; drafts sent after RM edits.
- **Measures:** time to follow-up; drafts used; time saved.

**B4. Meeting follow-up: call notes into Salesforce** (wave 1; live with the brief and the opportunity list about weeks 4–6)
- **Trigger:** the B3 recap is ready.
- **Steps:** 1. A3 drafts the Salesforce activity note and next steps. 2. **Decision point:** the RM approves or edits. 3. On approval, the note is saved to Salesforce, tagged "AI-drafted."
- **Logged:** drafts, approvals and edits.
- **Measures:** share of meetings logged in Salesforce (the data flywheel); admin time saved.

**B5. Early warning: client may leave** (wave 2)
- **Trigger:** A1 finds a warning signal, such as falling balances or less activity.
- **Steps:** 1. A2 explains the signal with the numbers. 2. An alert appears on the client record and in the next Monday send. 3. **Decision point:** the RM decides whether and how to reach out, and logs the action.
- **Logged:** alerts, RM actions, outcomes.
- **Measures:** clients kept against the comparison group.

**B6. Referral prompts** (wave 2)
- **Trigger:** A1 spots a likely need another team serves, such as treasury management.
- **Steps:** 1. A2 explains the need. 2. **Decision point:** the RM clicks "refer" or dismisses it. 3. On refer, Power Automate creates the referral in Salesforce and notifies the specialist. 4. The specialist accepts it and the referral is tracked to close.
- **Logged:** prompts, referrals, acceptances, outcomes.
- **Measures:** referrals made and won.

**B7. Client Q&A** (wave 3)
- **Trigger:** the RM asks a question in Salesforce or Teams.
- **Steps:** 1. A5 checks the RM's permissions. 2. It answers from permitted data, with sources. 3. **Decision point:** the RM acts; any record update needs their click.
- **Logged:** questions, answers, sources, updates.
- **Measures:** questions answered; answer ratings; zero permission breaches.

**B8. Prospect lookalikes** (wave 2)
- **Trigger:** monthly.
- **Steps:** 1. A1 finds prospects that look like the bank's best clients in the licensed prospect data, using agreed and explainable criteria (wave 2's data contract update adds that data). 2. A2 explains each match. 3. **Decision point:** the RM decides whether to pursue each one.
- **Logged:** prospects shown, pursued and won.
- **Measures:** new clients against the comparison group.
- **Check:** compliance reviews the criteria before launch, because prospect selection can raise fair-lending questions.

**B9. Every release (every week or two)**
- **Trigger:** any change to prompts, rules, data or models.
- **Steps:** 1. M32 re-runs the test set. 2. If the score is below the quality bar, the release stops. 3. If the change is material (Product Framework), it goes back through step 4 before release. 4. Release; M32 watches live quality for [X] days.
- **Logged:** test scores, approvals, release notes.
- **Measures:** quality trend; releases rolled back.

## Part 6: Core use cases and outside research

Working file: `memos/use-case-library.md`.


**The need in one line:** RMs at many commercial banks spend only about 25–30% of their time with clients (McKinsey). Much of the rest goes to admin, weak leads and meeting prep. So the value is in two places: better opportunities, and the time to act on them.

| Core use case | Where the value is | Outside evidence (McKinsey unless noted) | Our AI product (wave) |
|---|---|---|---|
| **Prospecting and next best opportunities** | Finding the clients and prospects most likely to buy | About 30% pipeline growth and 10% higher revenue; one bank saw twice the conversion rate of traditional leads | Monday opportunity list (1); prospect lookalikes (2) |
| **Lead nurturing, including cross-sell** | More qualified leads and referrals between teams | Two to three times more qualified leads; 5% higher conversion (early pilots). Morgan Stanley: more than 100,000 successful AI-matched referrals to advisors (2024, its CFO; [The Daily Upside](https://www.thedailyupside.com/technology/artificial-intelligence/how-morgan-stanleys-ai-helped-close-100k-new-clients-this-year/), Oct 2024) | Referral prompts (2). Contacting prospects on its own: out on purpose |
| **Account intelligence and meeting prep** | Better meetings in less prep time | About 25% less prep time; 10% more time with clients. Bank of America's CTO: AI prep lets a banker cover about 50 clients instead of 15 in some cases (not audited; Reuters 2025, via [TechInformed](https://techinformed.com/?p=37424)) | Pre-meeting client brief (1); client Q&A (3) |
| **Deal scoring and pricing** | Better margins, faster approvals | 10% margin gains; one bank cut deal turnaround from five days to two | Out on purpose: the AI never sets or suggests a price (control K3, chosen to stay clear of fair-lending law) |
| **AI sales coaching** | Better calls; new RMs up to speed sooner | Customer satisfaction up seven points; new bankers up to speed 20% faster | AI sales coaching (3) |
| **Admin off the RM's plate** (our own) | Hours back for clients; better CRM data | Admin ranks first or second of bankers' problems at every stage of a sale (survey of 406 bankers and sales leaders, October 2025); it earns part of the 10–12 hours a week McKinsey expects back per banker, and about 40% better coverage | Meeting follow-up, with call notes into Salesforce (1) |
| **Keep clients** (our own) | Clients kept before they drift away | No outside figure; set from the bank's own retention data | Early warning (2) |

**The headline numbers.** Banks that rework one frontline area end to end see about 3–15% higher revenue per RM and 20–40% lower cost to serve. 53% of bankers cite a shortage of high-quality leads as their biggest barrier. McKinsey's warning: "Banks are moving fastest on the least valuable tools."

**What other banks are doing.**
- **BMO** (commercial banking): a "Next Best Offer" engine ranks leads and offers in the CRM, with the reason shown ([BMO AI](https://ai.bmo.com/?p=569)).
- **Morgan Stanley** (wealth): "Debrief", used with client consent, summarizes meetings, drafts the follow-up email and saves a note into Salesforce ([Morgan Stanley, June 2024](https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch)).
- **Banco do Brasil:** 12,000+ RMs get AI conversation summaries in one workspace ([NiCE case study](https://www.nice.com/resources/banco-do-brasils-bankers-stopped-working-yesterdays-data-and-let-ai-hand-them-todays), vendor, 2026).
- **JPMorgan** (wealth) and **CaixaBank** report AI tools for advisers and bankers; JPMorgan credits its tools with lifting sales in April 2025, without a figure.

The pattern: signals from data, shown inside the CRM, with the reason visible and the banker in control. Results against a comparison group are rare.

**Source:** McKinsey, "Agentic AI is here. Is your bank's frontline team ready?" (Kumar Kanagasabai, Chris Lu, Shital Chheda; [link](https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready)), based on a survey of about 400 US and Canadian bankers; checked against the article's text on 2026-10-10. ⚠️ Publication date not confirmed. Full exhibit data and every RM detail: [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n).


## Part 7: McKinsey's research in full

Working file: `memos/mckinsey-frontline-ai.md`.

The full McKinsey research behind the Use Case Library's relationship manager (RM) section. It summarizes McKinsey's
article "Agentic AI is here. Is your bank's frontline team ready?". How the RM plan answers each use case is in the Use Case Library and RM Detail, Part 3. Checked against the article's text, pasted
in by me on 2026-10-10.

> **Source.** Kumar Kanagasabai, Chris Lu and Shital Chheda (McKinsey):
> https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready
> Based on a survey of about 400 US and Canadian bankers, RMs and sales leaders.
> McKinsey's numbers come from its own client work and early pilots, not
> controlled studies, so treat them as directional. ⚠️ The page I pasted showed no
> publication date, so the date is unconfirmed (an earlier draft said December 2025).

### The headline numbers

| Finding | McKinsey's words |
|---|---|
| Revenue and cost | Banks that rewire one frontline area end to end "enjoy between 3 and 15 percent higher revenues per RM and 20 to 40 percent lower cost to serve" |
| Time with clients | "In many commercial banks, relationship managers spend just 25 to 30 percent of their time in client dialogue" |
| Time freed | "ten to 12 hours a week returned to each banker", improving the coverage ratio (clients per banker) by about 40 percent |
| Top problems | Excessive admin, low-quality leads, and difficult meeting prep. 53 percent cite a shortage of high-quality leads as their biggest barrier |
| Admin at every stage | McKinsey's Exhibit 3, the top three challenges at each stage of the banking sales funnel (% of respondents; Frontline Sales Survey, October 2025, 406 respondents). Prospecting: low-quality leads 37, admin 32, meeting prep 26. Outreach: admin 33, generic outreach 30, meeting prep 28. Early conversation: admin 31, low-quality leads 31, meeting prep 29. Late-stage conversation: admin 35, slow internal approvals 28, meeting prep 25. Negotiation: admin 33, slow approvals 32, hard to prioritize accounts 28. Deal close: admin 37, slow approvals 34, meeting prep 26. So admin ranks first or second at all six stages. Shared by me as a screenshot on 2026-10-10 |
| Where banks go wrong | "Banks are moving fastest on the least valuable tools" |

### The five use cases

| # | Use case | What the AI does | Reported impact (McKinsey) |
|---|---|---|---|
| 1 | **Prospecting** (market maps and next best opportunities) | Combines data sources into ranked lists of high-potential clients, refreshed as markets change | About 30% pipeline growth and 10% higher revenue; one bank saw twice the conversion rate of traditional leads |
| 2 | **Lead nurturing** (including cross-sell) | An agent replies to inquiries, sends tailored content and books meetings, passing only qualified leads to the RM | Two to three times more qualified leads; 5% higher conversion (early pilots) |
| 3 | **Account planning and meeting prep** (account intelligence) | Pulls data from many sources into an account plan or briefing in minutes, with talking points | About 25% less prep time; 10% more time with clients |
| 4 | **Deal structuring and pricing** (dynamic deal scoring) | Recommends pricing and discounts from past deals and client data, and speeds approvals | 10% margin gains; one bank cut deal turnaround from five days to two |
| 5 | **Coaching** (AI sales coaching) | Reviews call transcripts and gives each banker personal guidance | Customer satisfaction up seven points; new bankers up to speed 20% faster |

McKinsey ties these to the stages of a sale: prospecting and deal close
(use case 1), outreach (2), early and late-stage conversations (3, with
coaching in late stage), and negotiation (4).

### McKinsey's five principles for capturing the value

1. Define the business model and the value it should create.
2. Rework a frontline area end to end, not piece by piece, with a repeatable playbook for scaling.
3. Build reusable technology: an orchestration layer for agents, a data foundation (an "ontology" of the bank's workflows, decisions and knowledge), and trust and security.
4. Put governance in place: how much each agent may do on its own, monitoring and audit.
5. Upskill the workforce, as RM roles change.

**Where our framework already does this:** 1 is the value model and the
sponsor's outcome (Discover); 2 is the six-step process and the playbook; 3 is
the agent library, the data contract and the Glossary (our working vocabulary,
which plugs into the bank's ontology); 4 is the Controls Catalog and
"assistive first"; 5 is Release and adopt (training on users' own work and
champions). ⚠️ Role redesign (new roles such as "agent orchestrator") isn't
covered yet.

## Part 8: The prototype: what it shows and how it's built

Working file: `prototypes/rm-assistant/README.md`.

A clickable concept of **The RM Assistant**: one AI assistant for each relationship manager (RM).
It shows the plan's wave 1 capabilities working, with three agents running live on Claude, on
made-up sample data. It's a prototype to show we can build; the real product comes from the six
steps (Discover onward), so every fact about the bank in it is an assumption to confirm.

- **Live page:** https://claude.ai/artifact/RFM2o7cdren3TxesQBsjky (private until shared from its Share menu)
- **The tour as a video:** `rm-assistant-tour-v4.mp4` (version 4, about 2½ minutes, with a voiceover read by Kokoro, an open-source voice; the script is `video/narration.json`). The version 1 video is kept as `rm-assistant-tour-v1.mp4`.
- **Built from:** Prompt 4 in `prompt-library.md`; the product page (`memos/rm-assistant.md`), agents A1 to A3 and
  workflows B1 to B4 in the full plan (`memos/rm-analytics-framework.md`); controls in `playbook/controls.md`.
- **Added for the prototype only:** the outside data feed (the 10-year Treasury yield) and its "Rates context" rule. They
  aren't in the plan's agent specs or data contract; a real build would add them through the data contract (K5) first.

### What's in it

| Screen | Plan reference | What happens |
|---|---|---|
| Today (since version 4) | Ties the wave 1 capabilities together | The RM's day on one screen: four numbers to click, this week's meetings with their briefs, and what's waiting for a decision. |
| Monday opportunity list | Workflow B1, agents A1 and A2 | A1 checks the 12 clients against 5 rules, plus the rates context (code, no AI). A2 (Claude) explains the top 5. The RM accepts, changes or dismisses each one. |
| Pre-meeting client brief | Workflow B2, agent A3 | A3 (Claude) calls four page tools (client record, open insights, recent activity, market data), then writes a one-page brief with a source on every fact. |
| Meeting follow-up | Workflows B3 and B4, agent A3 | A3 (Claude) turns the RM's notes into a recap, a follow-up email, a CRM call note and next steps. Nothing is saved until the RM approves; the RM sends the email. |
| Controls and audit log | K1, K2, K3, K4, K7, K8, K12, K22, K24, K25 | "Try to break it" (guardrails stop credit decisions, prices, auto-send and other RMs' clients in code); A1's rule set; the live audit log. |
| Product manager view | The five kinds of measures | Usage, quality, business impact, adoption, and risk and controls, counted from the session. |
| How it's built | | The agents, the data, and where this sits in the product machine (sub-step 1.6). |
| Early warning (wave 2 preview, version 4) | Workflow B5 | Three rules in code (falling balances, payroll moved out, gone quiet) flag clients who may be drifting away, with a balance chart and the numbers. Never a credit signal. The RM plans a call or dismisses it. |
| Refer to treasury (wave 2 preview, version 4) | Workflow B6 | The Signal finder's treasury rules spot needs the treasury team serves; a drafted hand-off the RM changes, sends or skips, tracked from spotted to accepted (sample: nothing leaves the page). |

The **guided tour** plays on a first visit (under 2 minutes), and anyone can pause, skip or replay it.

### How it works

- **Live AI:** inside claude.ai the page asks Claude through the artifact's `sample` capability, on the
  viewer's own Claude account (the first run asks the viewer's permission). A2 uses the quick model tier;
  A3's brief uses page tools; the follow-up uses the default tier.
- **Without live AI** (outside claude.ai, or if the viewer says no), every screen plays the **recorded run**
  in `src/replay.js`, written by Claude during the build and labeled "Recorded run" on screen. The tour
  always uses recorded runs, so it never spends anyone's usage.
- **Number check (K7 and the accuracy bar):** as soon as an AI draft is finished, and before the RM can use it, every number in it
  is matched against the numeric data the agent was given; anything it can't trace (including amounts written
  in words) is highlighted. Small whole numbers under 10 are left unchecked, so counts like "3 talking points" pass.
- **Guardrails (K8, K4, K1):** checked in code before Claude is asked; Claude's prompt carries the same
  rules as a second line of defence. The code check is pattern matching, so it catches common phrasings, not
  every possible one; `tests/run-tests.js` lists the phrasings it must block and the innocent ones it must allow.
- **Outside data:** the US 10-year Treasury yield (monthly average, Federal Reserve H.15, public domain),
  via the datahub.io copy on GitHub. A published page can't reach outside websites, so
  `scripts/fetch_market.py` saves a dated copy into `src/data/market.js` and the page shows that date.

### Files

| Path | What it is |
|---|---|
| `src/page.html` | The page's markup |
| `src/styles.css` | The house style (the Document Library's tokens), light and dark |
| `src/data/book.js` | The sample RM, 12 clients (plus 2 of another RM's) and the meeting notes |
| `src/data/market.js` | The outside data (generated; don't edit) |
| `src/agents.js` | A1's rules, the guardrails, the number check, the audit log, the page tools and the prompts |
| `src/replay.js` | The recorded runs |
| `src/app.js` | The screens |
| `src/tour.js` | The guided tour |
| `build.py` | Inlines everything into one file, `prototype-v<N>.html` |
| `tests/run-tests.js` | Automated tests of the "done" checklist, with a test double standing in for Claude |
| `tests/record-video.js` | Records the tour as a video, each step timed to its voiceover line |
| `video/narration.json` | The voiceover script, one line per tour step |
| `video/narrate.py` | Reads the script aloud with Kokoro (code MIT, model Apache 2.0), one clip per step |
| `video/make-video.py` | Retimes the recording to real time and lays the voice down in sync |
| `CHANGELOG.md` | What changed in each version |

### How to change it

1. Edit the files in `src/` (or refresh the outside data: `python3 scripts/fetch_market.py`).
2. Build the next version: `python3 build.py 2` writes `prototype-v2.html`. Delivered versions are never
   overwritten, so every step is kept.
3. Test it: `PW=/opt/node-tools/node_modules/playwright node tests/run-tests.js prototype-v2.html`
   (screenshots go to `$SHOTS`).
4. Add a line to `CHANGELOG.md`, publish the new file to the same page link, and save a draft to GitHub.
- **Voice:** `voice/` holds the tour's voice, one MP3 per step (Kokoro, from `video/narration.json`) and their lengths; `build.py` puts them into the page.

_Last updated: 2026-10-18_
