# RM Assistant Plan

How The RM Assistant gets delivered to relationship managers (RMs) · Associated Bank · October 2026

What the product is: [RM Assistant](https://claude.ai/artifact/RBaZS636CtycDwZyDrgum2). The short version for leaders: [RM Executive Summary](https://claude.ai/artifact/LPPq2gt5PSoiB8GzX8ZBE2). Every detail (each step, the agent specs and the workflows) is in [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n), the fourth page in the RM section, for AI to read. The rules every product follows are in the [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ).

## The plan at a glance
The first 13 weeks (about 90 days), as estimates to confirm in the first days. Week 1 starts at kickoff.

```gantt
weeks 13
Kickoff and a working prototype on sample data | 0 | 1 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-1-discover
Gate 1: the sponsor confirms wave 1 | 1 | 1 | gate | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-1-discover
Interviews and sizing with RMs | 0 | 2 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-1-discover
Gate 2: data contract, risk rating, value model | 2 | 2 | gate | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-2-define
Meeting recap and email: tests and sign-offs | 1 | 3 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-the-assistant-s-capabilities-wave-by-wav
**Meeting recap and email live** | 3 | 13 | live | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-5-release-and-adopt
Brief, opportunity list and call notes: built and tested on real data | 1 | 5 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-3-build
Their sign-offs (call notes go back through step 4) | 3 | 5 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-4-govern-and-test-formal-approval-g
**Brief, opportunity list and call notes live** | 5 | 13 | live | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-5-release-and-adopt
Small releases every week or two | 6 | 13 | ongoing | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-6-measure-and-iterate
```

Waves 2 and 3 get dates at gate 2. The first read on closed revenue comes at about month 6. If data access or the AI review runs long, the recap and email still go first and the rest goes live by about week 10.

Each row's "detail" link opens that step in RM Detail, the full plan.

## 1. Wave 1 in about six weeks
Building starts on day one. Weeks are estimates to confirm in the first days.

| When (estimate) | What gets done | Who |
|---|---|---|
| Days 1–5 | Sponsor kickoff; risk partner briefed; data access requested; working prototype on sample data | Product manager |
| Week 1 | **Gate 1:** the sponsor sees the prototype and confirms wave 1 | Sponsor, with the risk partner |
| Weeks 1–2 | Interviews and shadowing with RMs, using the prototype; size the opportunity | Product manager, pilot RMs |
| Week 2 | **Gate 2:** data contract signed, early risk rating, value model, Finance's method for counting results, baseline confirmed, dates proposed for waves 2 and 3 | Sponsor, data owners, risk partner |
| About weeks 2–4 | **Meeting recap and email live** with pilot RMs (in M365 Copilot), after their tests and sign-offs | Sponsor and risk partner |
| About weeks 4–6 | **Client brief, Monday opportunity list and call notes into Salesforce live**, after their tests and sign-offs | Sponsor and risk partner |
| About month 6 | First read on closed revenue against the comparison group | Sponsor, Finance |

After wave 1: small releases every week or two. Wave 2 (early warning, referral prompts, prospect lookalikes) and wave 3 (client Q&A, AI sales coaching) get dates at gate 2, once data access and review times are known.

Detail: [the full project plan, week by week](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate).

## 2. What sets the pace
- **Data access.** The data contract needs the Salesforce and Snowflake data owners' signatures, aimed for week 2. The product manager chases it from day one.
- **The bank's AI review.** The risk partner sees every version as it's built, so sign-off confirms what they already know.
- **Backup plan.** If either runs long, the meeting recap and email go first (they need the least new data and review), and the rest stays ready in the test environment, live by about week 10. The call is made at gate 2.

Detail: [the backup plan and the six conditions for moving fast](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate).

## 3. Who decides
| Role | For the RM project |
|---|---|
| Sponsor | A commercial banking leader [name needed]: the outcome, funding and every gate |
| User leaders | RM leaders and market managers: choose the pilot group, use the assistant in the weekly pipeline meeting, decide with the sponsor whether to scale |
| Pilot RMs | Co-design and test; their feedback steers what gets built |
| Data owners | Salesforce and Snowflake data [names needed]: sign the data contract |
| Risk partner | Rates the product and approves it at step 4; the sponsor can't overrule that approval |
| Sales leadership and HR | Whether acting on the assistant's insights counts in how RMs are measured and paid |

Detail: [who's involved and who decides](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-3-who-s-involved-and-who-decides).

## 4. How we'll prove the value
- **Revenue:** pipeline and wins from the assistant's suggestions, against similar RMs not yet using it. Every AI-sourced opportunity is tagged in Salesforce from day one, and Finance agrees the method before the pilot.
- **Time:** hours saved per week and client-facing time, reported as hours, not turned into revenue.
- **Use:** pilot RMs active each week, and the share of suggestions acted on.
- **Payback:** target [X] months for wave 1. All targets are set from the bank's own numbers at gate 2.

Detail: [the value model](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-2-the-value-model).

## 5. Top risks
| Risk | How I'd handle it |
|---|---|
| Data access or the AI review takes longer | Start both on day one; keep wave 1 internal, assistive and on approved platforms; use the backup plan |
| RMs don't trust the insights | Show the reason and the numbers behind every insight; build it with pilot RMs; managers use it in their routines |
| CRM data is incomplete | Lean on account data in Snowflake first; approved call notes improve CRM data over time |
| Incentives don't reward acting on insights | Agree recognition for AI-sourced wins with sales leadership before launch |
| Client privacy in recorded meetings | Record only with client consent and under the bank's recording policy; notes stay drafts until the RM approves |

Detail: [every risk and how I'd handle it](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-7-top-risks-and-how-i-d-handle-them).

## 6. What I'd confirm in the first weeks
- Which revenue lever matters most now: new clients, growing clients or keeping them?
- Which RM teams would make a good pilot group?
- Who owns the client data in Salesforce and Snowflake?
- How are RMs measured and paid today?
- How long does the AI review take, and is recording client meetings in Teams allowed?
- What team and budget are available for the pilot?

Detail: [the full list of what to confirm](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-9-what-i-d-confirm-in-the-first-weeks).

_Last updated: 2026-10-18_
