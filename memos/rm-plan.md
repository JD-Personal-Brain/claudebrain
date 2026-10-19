# RM Assistant Plan

How The RM Assistant gets delivered to relationship managers (RMs) · Associated Bank · October 2026

[RM Executive Summary](https://claude.ai/artifact/LPPq2gt5PSoiB8GzX8ZBE2) · [The RM Assistant](https://claude.ai/artifact/RBaZS636CtycDwZyDrgum2) · [RM Assistant Prototype](https://claude.ai/artifact/RFM2o7cdren3TxesQBsjky) (see it working) · [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n) (everything in full) · [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ) (the rules every product follows)

## The plan at a glance
The first 13 weeks, as estimates to confirm. Week 1 starts at kickoff; gates (◆) are go/no-go decisions. Each live bar starts once the bank's AI review signs it off (and, where it uses client data, that data is approved), so the bars move with those approvals. Each row links to its detail in RM Detail.

```gantt
weeks 13
Kickoff and a working prototype on sample data | 0 | 1 | build | https://claude.ai/artifact/RFM2o7cdren3TxesQBsjky
Gate 1: target, measure and baseline (from first sizing) agreed | 1 | 1 | gate | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-4-how-the-work-flows
Interviews with RMs, improving the prototype every few days | 0 | 2 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Gate 2: client data approved, risk level rated, business case agreed | 2 | 2 | gate | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-4-how-the-work-flows
Meeting recap and email: set up on sample notes, then tested and signed off after gate 2 | 1 | 3 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
**Meeting recap and email live** | 3 | 13 | live | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Brief, opportunity list and call notes: built and tested on real data, after gate 2 | 2 | 5 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Sign-offs for the brief and list, plus a separate one to save call notes in Salesforce | 3 | 5 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
**Brief, opportunity list and call notes live** | 5 | 13 | live | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Small releases every week or two | 6 | 13 | ongoing | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
```

**Limiting factor (our assumption, to confirm):** how long the bank's AI review takes; every live bar moves with it (section 1).

The recap and email can move first because they're drafted from the RM's own notes, not client account data or meeting recordings (our assumption, to confirm: it needs the least review), and the risk partner reviews each version as it's built. Interviews keep going after gate 1 to refine the target. Waves 2 and 3 get proposed dates at gate 2, once data access and review times are known.

## 1. What could slow us down (to confirm)
Our working assumption is the AI review, then approval to use client data; the real blockers are a first question for the bank.
- **Approval to use client data.** Nothing reaches pilot RMs on real client data until the people responsible for it approve which data the assistant may use.
- **The bank's AI review.** Nothing goes live until risk, compliance, privacy and security sign off; the risk partner sees each version as it's built, so the sign-off has no surprises.
- **Backup plan.** If either runs long, the meeting recap and email go first, and the rest stays ready in the test environment, live by about week 10. The call is made at gate 2.

Detail: [the backup plan and the six conditions for moving fast](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate).

## 2. Who decides
| Role | For the RM project |
|---|---|
| Sponsor | A commercial banking leader [name needed]: the outcome, funding and every gate |
| User leaders | RM leaders and market managers (⚠️ titles to confirm): choose the pilot group, use the assistant in a team meeting they already run, such as a weekly pipeline meeting (⚠️ to confirm), and decide with the sponsor whether to scale |
| Pilot RMs | Co-design and test; their feedback steers what gets built |
| Data owners | The client data, in Salesforce and Snowflake (⚠️ to confirm) [names needed]: sign the data contract (the signed list of client data the assistant may use) |
| Risk partner | Rates the product's risk and approves it before it reaches RMs; the sponsor can't overrule that approval |
| Compliance, privacy and security | Sign off before it reaches RMs |
| Finance | Agrees how results are counted, and joins the sponsor for the quarterly call to invest more, adjust or stop |
| Sales leadership and HR | Whether acting on the assistant's insights counts in how RMs are measured and paid |

Detail: [who's involved and who decides](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-3-who-s-involved-and-who-decides).

## 3. How we'll prove the value
- **Revenue:** pipeline and wins from the assistant's suggestions, against similar RMs not yet using it. Every AI-sourced opportunity is tagged in Salesforce from day one, and Finance agrees the method before the pilot.
- **Time:** hours saved per week and client-facing time, reported as hours, not turned into revenue.
- **Use:** pilot RMs active each week, and the share of suggestions acted on.
- **Payback:** the target is set at gate 2 from the bank's own numbers, as are all the other targets.

Detail: [the value model](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-2-the-value-model).

## 4. Top risks
| Risk | How I'd handle it |
|---|---|
| Data access or the AI review takes longer | Start both on day one; keep wave 1 internal, to drafts and suggestions the RM checks, on platforms we expect the bank has already approved (⚠️ to confirm) (the backup plan is in section 1) |
| RMs don't trust the insights | Show the reason and the numbers behind every insight; build it with pilot RMs; managers use it in their routines |
| Client records (CRM) may be incomplete (⚠️ to confirm) | Lean on account data first; approved call notes improve the records over time |
| Incentives don't reward acting on insights | Agree recognition for AI-sourced wins with sales leadership before launch |
| Client privacy in recorded meetings | Record only with client consent and under any recording policy the bank has (⚠️ to confirm); notes stay drafts until the RM approves |

Detail: [every risk and how I'd handle it](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-7-top-risks-and-how-i-d-handle-them).

_Last updated: 2026-10-19_
