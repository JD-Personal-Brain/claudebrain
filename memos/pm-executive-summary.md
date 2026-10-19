# PM Executive Summary

For the leaders of the credit business · Associated Bank · October 2026

> ⚠️ **A working hypothesis** (first cut, 2026-10-19). Built from outside research and public Associated job postings, not yet from how the bank's portfolio managers (PMs) work today. The first conversations with credit leaders test it.

## The problem
PMs underwrite and monitor the bank's commercial loans (from the bank's job postings), but we expect much of their time goes to gathering financials from many systems, re-typing numbers and writing the routine parts of annual reviews and credit memos. At DBS, the bank estimates credit memos and related work take up to 40% of a relationship manager's time (DBS's estimate). ⚠️ How much of a PM's time they take here is a first question. Time spent assembling a review is time not spent judging the credit or watching for trouble.

The bank has said its first AI work in this business includes portfolio management, aiming at faster loan processing and less manual data work (its June 2026 announcement; ⚠️ exact wording to check).

## The product: The PM Assistant
Each PM gets **their own AI assistant**, inside the tools we expect they already use (Word, Teams and the loan system; ⚠️ to confirm). It gathers the borrower's file, drafts the routine sections of reviews and memos with a source on every number, and later flags borrowers whose signals are weakening. **The PM always writes the judgment, and a named credit officer decides** (no bank we found lets AI make the credit decision). It never sets or suggests a borrower risk rating, never approves or declines credit and never sets a price. [What it is and all its capabilities](https://claude.ai/artifact/BrBLWQzQggQPtqCgLLGf3C).

## What PMs get first (feature wave 1)
| Capability | What the PM gets | Why it matters |
|---|---|---|
| **Borrower file** | Everything about one borrower in one place: financials and their trend, loans, covenants, deposits, payments, the last review and the relationship manager's (RM's) notes, every figure with its source, and a list of what's missing or late | Hours of gathering back on every review; goes live first |
| **Annual review and credit memo drafts** | The routine sections drafted in the bank's template from the borrower file; the borrower risk rating and the recommendation left blank for the PM (wave 1 drafts always leave the recommendation blank; whether a later draft may carry one is the credit policy owner's call, our assumption) | Faster reviews, and faster answers on new requests |

**See it working:** the [PM Assistant Prototype](https://claude.ai/artifact/8vFxUWVwtZbzZs7pL162HE) runs its agents on sample borrowers, with a short tour.

Later waves add early warning flags and a covenant and statement tracker, then credit policy Q&A, a renewal radar and deal screening.

## The value
- **More PM time for judgment:** hours saved on each annual review and credit memo. DBS targets at least 30% less credit assessment time (a target, not yet a result); Moody's says its agents write about 35–40% of each memo at an unnamed tier-one US bank (the vendor's own claim; a share of the text, not of time). Outside figures, not our targets.
- **Faster answers:** fewer days from a complete request to a decision.
- **Earlier sight of trouble (wave 2):** flags acted on, and how early they came.
- Time is proven against similar PMs not yet using it; targets are set from the bank's own numbers. [Outside evidence for each credit core use case](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X#portfolio-managers)

## How fast
A first prototype takes days. We expect approval to set the pace (our assumption, to confirm): drafts inform credit decisions, so we expect them to need a deeper review (we call it the higher-risk path), including the credit policy owner's sign-off. On our first estimates, to confirm, that's the borrower file by about week 7 and the drafts by about week 12. These dates assume the bank's reviews run alongside the build and take weeks, not months; if its model validation takes longer, the drafts move out and the borrower file still goes first (unless it is put on the deeper review too). [The plan, week by week](https://claude.ai/artifact/UKMBCCxBns8YuCJyEo4Zkv)

**What could slow us down:** not known yet. Possible hold-ups include approval to use borrower data and the deeper credit review. If the review runs long, the borrower file still goes first (unless the risk partner puts it on the deeper review too), because it gathers and cites but writes no judgment; if data approval runs long, the prototype keeps running on sample borrowers until it lands.

## What I need, and what I'd confirm
1. A sponsor for the PM work: about an hour a week, plus each go/no-go decision (our estimate).
2. Time with 4–6 PMs and credit analysts, shadowing a real annual review in the first three weeks (our estimate), and a willing pilot group.
3. The credit policy owner, early: what a draft may contain, and their sign-off.
4. Named owners for borrower data and the credit file, and the review and memo templates.

To confirm in the first weeks: how long the bank's AI and model review takes; what usually holds up a new AI tool here; how many reviews and memos PMs write a year and how long each takes; which loan system and spreading tool the bank uses; and whether a later draft may carry a recommendation.

_Last updated: 2026-10-19_
