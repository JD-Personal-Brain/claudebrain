# PM Assistant Plan

How The PM Assistant gets delivered to portfolio managers (PMs) · Associated Bank · October 2026

[PM Executive Summary](https://claude.ai/artifact/Cvw3mkUohNFLwVr4H2wURd) · [The PM Assistant](https://claude.ai/artifact/BrBLWQzQggQPtqCgLLGf3C) · [PM Assistant Prototype](https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE) (see it working) · [PM Detail](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg) (everything in full) · [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ) (the rules every product follows)

## The plan at a glance
The first 13 weeks from kickoff, as estimates to confirm. Gates (◆) are go/no-go decisions; each capability goes live once its data is approved and the review signs it off. **Limiting factor (our assumption, to confirm):** how long the bank's AI review takes. Each row links to its detail.

```gantt
weeks 13
Kickoff and a working prototype on sample borrowers | 0 | 1 | build | https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE
Gate 1: target, measure and provisional baseline agreed | 1 | 1 | gate | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-4-how-the-work-flows
Shadowing PMs through real reviews, giving the final baseline | 0 | 3 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Industry background draft: built and tested on public sources | 0 | 5 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Borrower file and drafts built on sample borrowers | 0 | 4 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Gate 2: borrower data approved, higher-risk path set, business case agreed | 4 | 4 | gate | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-4-how-the-work-flows
Industry background draft: sign-offs, then **live in week [X]** (set at gate 2, once the AI review's length is known) | 4 | 13 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Borrower file: tested on real data, sign-offs, then **live in week [X]** (set at gate 2) | 4 | 13 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Review and memo drafts: tested on real past reviews | 4 | 9 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Higher-risk review and sign-offs, including the credit policy owner | 9 | 11 | build | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Gates 3 and 4 for the drafts: quality bar met, sign-offs recorded | 11 | 11 | gate | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
**Review and memo drafts live** | 11 | 13 | live | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
Small releases every week or two, once a capability is live | 11 | 13 | ongoing | https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate
```

The industry background draft goes first because it uses no borrower data, so it's built on public sources from week 1. The borrower file goes ahead of the drafts because it writes no judgment; the drafts inform credit decisions and take the deeper review we call the higher-risk path (our assumption; ⚠️ the risk partner decides). Feature waves 2 and 3 get dates once that review is signed (about week 11).

## 1. What could slow us down (to confirm)
Our working assumption, to confirm with the bank:
- **Approval to use borrower data and credit files.** Nothing reaches pilot PMs on real data until the people responsible for it approve which data the assistant may use.
- **The deeper review for credit drafts.** Nothing goes live until risk, compliance, privacy, security and the credit policy owner sign off. To keep that short, they review each version as it's built.
- **Backup plan** (decided at gate 2). A slow review of the industry background draft is no worse than today: the outside firm keeps writing the section. Slow data approval: the prototype keeps running on sample borrowers and the dates are reset at gate 2. If the risk partner puts the industry background draft or the borrower file on the higher-risk path, it goes live with the drafts at about week 12. A slow review of the drafts: the borrower file stays live, the version under review is kept unchanged, and improvements ship after sign-off.

Detail: [the backup plan and how we move fast](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate).

## 2. Who decides
| Role | For the PM project |
|---|---|
| Sponsor | A credit or commercial banking leader [name needed]: the outcome, funding and every gate |
| User leaders | PM team leaders and credit managers: choose the pilot group, use the early warning flags in a portfolio review they already run (⚠️ to confirm), and decide with the sponsor whether to scale |
| Pilot PMs and analysts | Co-design and test, and grade the drafts; their feedback steers what gets built |
| Credit policy owner | What a draft may contain, and a sign-off before drafts reach PMs [name needed] |
| Credit officer | Whoever holds approval authority for that credit under the bank's authority list (it may be the PM; ⚠️ to confirm); named on every draft |
| Data owners | Borrower data and credit files (⚠️ which systems is to confirm) [names needed]: sign the data contract (the signed list of borrower data the assistant may use), with the credit file's content owner signing the list of documents |
| Risk partner | Rates the product's risk and approves it before it reaches PMs; the sponsor can't overrule that approval |
| Compliance, privacy and security | Sign off before it reaches PMs; compliance runs the fairness check |
| Owner of the outside firm's contract | Vendor management or procurement (⚠️ to confirm): whether and when the contract for industry sections changes; vendor risk approves any licensed industry source |
| Finance | Agrees how hours saved are valued, and joins the sponsor for the quarterly call to invest more, adjust or stop |

Detail: [who's involved and who decides](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-3-who-s-involved-and-who-decides).

## 3. How we'll prove the value
- **Outside cost:** the outside fees for industry sections we could replace (counted once the contract changes; its terms are to confirm), and how many days sooner the section is ready.
- **Time:** hours per annual review and credit memo, against similar PMs not yet using it, by a method Finance agrees before the pilot.
- **Speed:** days from a complete request to a decision, judged once enough requests have gone through.
- **Quality:** every number in a draft matches its source; the share of sections PMs keep with light edits.
- **Use:** pilot PMs using it each week.
- **Payback:** the target is set at gate 2 from the bank's own numbers, as are all the other targets. Loan losses avoided are tracked, not counted, until Finance and credit risk agree a method.

Detail: [the value model](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-2-the-value-model).

## 4. Top risks
| Risk | How I'd handle it |
|---|---|
| A wrong number in a credit draft, or PMs don't trust the drafts | Every number traced to its source and checked before the PM sees it; zero tolerance in testing; built with pilot PMs on their own past reviews |
| The AI drifts into the credit decision, or loan review or examiners question AI-drafted text in the credit file | It never writes the borrower risk rating or the recommendation; tests that it refuses; every draft stamped AI-drafted and approved by the named PM, with the credit officer named and sources kept; brief loan review early |
| Approval to use borrower data takes longer | Request it on day one; keep the prototype running on sample borrowers |
| The deeper review takes longer | Brief the credit policy owner in week one; the borrower file goes ahead of the drafts (section 1) |
| Documents are scanned, messy or in many systems (⚠️ to confirm) | Start with documents already in a standard form; the file lists what's missing instead of guessing |
| Copyright and license terms of the industry sources | Only sources on an approved list, each license checked by vendor risk; nothing copied beyond what a license allows; every statement cited and dated |

Detail: [every risk and how I'd handle it](https://claude.ai/artifact/KZ4PEbhCPAj6uWKXmJMCeg#part-5-the-full-delivery-plan-with-every-7-top-risks-and-how-i-d-handle-them).

_Last updated: 2026-10-19_
