# Audit: RM analytics framework (v3)

_2026-10-07 · What's missing, what could be better, and how to make it world-class
before sharing it with Associated Bank._

**Status:** all 16 items applied in memo v4 and the design page (2026-10-07). Item 16 is a reminder for me: share from the page's Share menu and read every line first.

## The verdict
The six steps, the agent breakdown and the evidence are solid. What's missing
is mostly what a **hiring panel** looks for: a point of view on value, time,
people and risk. Today the memo explains *how* the work flows. A world-class
version also says *how much it's worth, how fast, who's involved and what
could go wrong*.

## Highest impact (recommend adding all 5)

1. **A one-page executive summary up front.** Readers decide in about 60 seconds. Lead with the outcome, the approach in 3 bullets, the first 90 days and what I'd need from them.
2. **A simple value model.** Show how revenue would be estimated: RMs × opportunities per RM × conversion rate × average revenue per opportunity, minus costs (licenses, build, run). Use placeholders like [X], not invented numbers. This shows commercial thinking and links to "offset the cost."
3. **A 30/60/90-day plan and pilot timeline.** Panels want to know what happens in month one. For example: 30 days to listen and size, 60 to define and design, 90 to have a pilot approved and building. Mark it as an estimate to confirm with the team.
4. **Stakeholders and decision rights.** The job is about aligning business, technology, data, risk, compliance and operations. Add a short "who's involved and who decides" table: business sponsor, RM leaders, data owners, Salesforce and Microsoft platform teams, model risk, compliance, privacy.
5. **Top risks and how I'd handle them.** For example: incomplete CRM data, RMs not trusting insights, governance taking longer than planned, costs growing with usage, and incentives that don't reward acting on insights.

## Strong improvements

6. **Governance runs through every step, not just Step 4.** Calling Step 4 "Govern and test" can suggest risk comes late. Show governance as a thread through all six, with Step 4 as the formal approval gate. Bank risk partners will notice this.
7. **Clear go/no-go gates.** Turn each "Done when" into a measurable gate. For example, "pilot RMs act on at least [X]% of insights" rather than "meets targets."
8. **A platform choice, not just options.** Several agents say "Salesforce Agentforce *or* Copilot Studio." Add the decision criteria (where RMs spend their day, data access, cost, governance fit) and a provisional pick for the pilot, to be confirmed in Discover.
9. **RM incentives.** If compensation doesn't reward acting on insights, adoption stalls. Add it to Discover questions and the risk list.
10. **The "data flywheel."** The time-saving features (auto call notes and CRM logging) also improve CRM data quality, which makes the insights better. Name this loop explicitly; it's a strong strategic point.
11. **Reuse for the next use case.** The data views, test sets, guardrails and agent patterns become a platform for use case #2. Shows "Principal"-level thinking beyond one product.

## Polish before sharing

12. **Rewrite assumptions as hypotheses.** Phrases like "assumed live at the bank" read as internal notes. Use "I'd expect to build on…, to be confirmed in the first weeks."
13. **Tighten fair-lending wording.** Suggesting a credit line is still credit marketing, and fair-lending rules (ECOA) apply to business credit too. Say how insights about credit products get reviewed.
14. **Define the quality bar.** Name the test measures: factual accuracy of numbers, every insight cites its source, relevance as rated by RMs, and the share of insights RMs would act on.
15. **Remove internal notes.** "Draft v3," "verify" flags, and the Claude-specific tool note shouldn't appear in a shared version.
16. **Sharing.** The design page is private. Share it from its **Share** menu, or export it to PDF. Read every line yourself before sending, since it goes out under your name.

---

## Feasibility audit (v4 → v5, 2026-10-07)

Read the whole memo top to bottom and asked: could a bank actually run this?

**Fixed in v5:**
1. **Timeline was too fast.** "Pilot ready for approval by day 90" is unrealistic once data access, platform release cycles and model risk review are included. New estimate: pilot live about month 6, scale decision about month 9, first revenue read about month 12. Shown as a Gantt chart.
2. **First release did too much.** Five RM-facing features at once means more data access, more review and more risk. Now: a quick win (Copilot meeting recaps), then Release 1 (insights, digest, feedback), then Release 2 (prep and follow-up assistant, RM assistant).
3. **Closed revenue can't show up in one quarter.** Commercial deals take months. Added leading vs. lagging measures.
4. ~~No team was named.~~ Added a team section without being asked; removed on 2026-10-08 at my request (lesson L5).
5. **Two AI paths doubled the review work.** Now one AI path for the pilot.
6. **Steps looked strictly one after another.** The plan now overlaps Build and formal review, with the risk partner engaged from week 1.
7. **Data access delays were missing from risks.** Added.

**Still worth knowing:**
- All timings are my estimates, not Associated Bank's actual timelines.
- A small pilot gives directional results; firm numbers need a few quarters.
