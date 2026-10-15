# Step 5: Release and adopt, the first time

**The question:** will users use it every week?
**The gate:** weekly use and leading results hit targets; no serious incidents; long-term owner confirmed before scaling.
**Governance thread:** live monitoring; incident process.

Adoption comes from changing how teams work, not from a training event. The
core of this step is 5.3: building the product into a routine that managers
already run. Fill in the first-time log (see `README.md`) for every sub-step.

> ⚠️ **How much to trust this.** Written 2026-10-09 from my framework, the RM
> memo and general change-management practice, not from Associated Bank.
> Lines marked ⚠️ are guesses about the bank.

---

## 5.1 Confirm release readiness

- **Goal:** everything around the product is ready before users see it.
- **Why it matters:** a bad first week is hard to recover from. Users decide fast whether a tool is worth their time.
- **Know first:** the sign-offs and conditions from step 4, operations contacts, and the release process for the platform. ⚠️
- **First time, step by step:**
  1. Go through a readiness checklist: sign-offs and conditions met, support contact named, incident process tested, training ready, communications drafted, monitoring switched on (M13 Data-use checker, M24 Data contract checker, M28 Fairness monitor and M32 Quality watchdog).
  2. Build the pilot dashboard from the 2.7 measures sheet, so usage and results are visible from day one.
  3. Do a dry run of the incident process: who is called, and how the product is paused.
  4. Agree the release date with operations and the platform team.
- **Output:** the completed readiness checklist and the pilot dashboard.
- **Done when:** every item is ticked, or has an owner and a date before go-live.
- **Automation watch:**
  - First time: **Draft**.
  - Note: which checklist items were late, and why.
  - Agent: **M15 Readiness tracker** (agent library) that checks off items from the tracker and flags gaps. *Auto*.
- **For RM analytics:** support through operations, and communications sent by RM leaders, not by the project team.

---

## 5.2 Launch the pilot, with a comparison group

- **Goal:** the pilot group is live, and a matching group is not, so results can be compared fairly.
- **Why it matters:** without a comparison group you can't tell the product's effect from a good quarter.
- **Know first:** the pilot and comparison groups (2.8), and the measures (2.7).
- **First time, step by step:**
  1. Move the product from test to live for the pilot group only, with the approval for the move recorded.
  2. Check the first live outputs by hand on day one.
  3. Check that usage and impact data are flowing into the dashboard.
  4. Make sure the comparison group's numbers are tracked the same way.
  5. Set the weekly usage report to send itself to the sponsor and user leaders.
- **Output:** the pilot is live, and data is flowing for both groups.
- **Done when:** the first week's usage shows on the dashboard for both groups, and the weekly report has gone out once.
- **Automation watch:**
  - First time: **Me**, with platform teams.
  - Note: every manual step in the move to live. Those steps are the release checklist for next time.
  - Agent: **M16 Release automation** (agent library) that runs the release checklist in the platform's own deployment tools. *Auto* where the platform supports it ⚠️.
- **For RM analytics:** pilot RMs and their managers, compared with similar RMs not yet using it.

---

## 5.3 Build it into routines (the core of adoption)

- **Goal:** the product becomes part of a meeting or habit that already happens every week.
- **Why it matters:** new tools that arrive without a change in how teams work tend to get little use. A manager's routine makes it stick.
- **Know first:** the team's existing routines (from 1.3), such as weekly pipeline meetings and Monday planning.
- **First time, step by step:**
  1. Pick one existing routine the product fits into.
  2. Agree with the manager how it will be used there, for example "we review the top insights at the start of each pipeline meeting."
  3. Sit in on the first two or three, and note what works and what doesn't.
  4. Adjust the product or the routine.
- **Output:** a routine with the product built in, agreed with managers.
- **Done when:** managers run it without you in the room.
- **Automation watch:**
  - First time: **Me**. This is change management.
  - Note: which routine worked, and how managers phrased it. Reuse that for the next team.
  - Agent: none. This stays with a person. The product's **weekly opportunity digest** (A4 in the RM plan, Appendix A) is part of the product and supports the routine, not an agent that runs it.
- **For RM analytics:** managers run weekly pipeline meetings from the insights.

---

## 5.4 Train users on their own work

- **Goal:** short demos that use each user's own clients or tasks, not made-up examples.
- **Why it matters:** people learn fastest when they see their own work get easier.
- **Know first:** the pilot users and their calendars. Keep demos to 15 to 20 minutes.
- **First time, step by step:**
  1. Prepare a short demo for each user or small group, using their own real work.
  2. Show one task end to end, then have them do one themselves.
  3. Give them a one-page "how to" and say where to ask questions.
  4. Note every question asked; they become the FAQ.
- **Output:** demos done, the one-page guide and the FAQ.
- **Done when:** every pilot user has done one real task themselves.
- **Automation watch:**
  - First time: **Me**.
  - Note: the questions people asked. They feed the onboarding coach.
  - Agent: the product's **onboarding coach** (A6 in the RM plan, Appendix A) answers "how do I…?" in Teams from the guide and the FAQ. *Auto* for answers; the product team keeps the content current.
- **For RM analytics:** demos built on each RM's own clients.

---

## 5.5 Recruit champions and celebrate wins

- **Goal:** respected users show their peers how they use it, and early wins get noticed.
- **Why it matters:** people trust peers more than project teams. Visible wins make the tool worth a try.
- **Know first:** who's respected and well-connected in the pilot group (ask the managers).
- **First time, step by step:**
  1. Ask 2 or 3 respected users to be champions. Give them early access to new AI products and changes and a direct line to you.
  2. Set up a channel (for example in Teams) where champions share tips.
  3. Collect early wins: a deal, an hour saved or a client moment that started with the product.
  4. Ask leaders to recognize those wins in their own meetings.
- **Output:** named champions, a channel and a wins log.
- **Done when:** champions are active and at least one win has been recognized by a leader.
- **Automation watch:**
  - First time: **Me**.
  - Note: which wins got noticed, and where.
  - Agent: **M17 Wins spotter** (agent library) that flags AI-sourced wins from the tagged data for you to check and share. *Draft*.
- **For RM analytics:** credit AI-sourced wins in sales meetings, tagged in Salesforce.

---

## 5.6 Fix fast

- **Goal:** act on feedback every week, and show users that you did.
- **Why it matters:** users keep giving feedback only if they see it acted on.
- **Know first:** where feedback lands (from 3.5) and who can fix what.
- **First time, step by step:**
  1. Read all feedback every week.
  2. Sort it into bugs, quality issues and ideas.
  3. Fix the top items, and add the rest to the backlog.
  4. Tell users what changed ("you said, we did").
  5. Log every incident, its owner and the fix. M30 Feedback triage flags anything that looks like an incident straight to the product manager and operations.
  6. Each fix is a new version: re-run the test set (M26) before it reaches pilot users, and tell the risk partner about any material change (⚠️ what counts as material is still to be agreed).
- **Output:** a weekly fix list, release notes and the incident log.
- **Done when:** this runs every week.
- **Automation watch:**
  - First time: **Me**, reading everything yourself the first few weeks.
  - Note: how feedback splits between bugs, quality and ideas, and how long sorting took.
  - Agent: **M30 Feedback triage** (agent library) sorts and routes it, and you review a weekly sample. Aim for **Auto**.
- **For RM analytics:** feedback logged in Salesforce from the one-click buttons.

---

## 5.7 Scale in user waves

- **Goal:** expand to more users only after a go/no-go check.
- **Why it matters:** scaling something that isn't working spreads the problem.
- **Know first:** the pilot results against the targets from 2.7.
- **First time, step by step:**
  1. Compare pilot results with the targets: weekly use, results, incidents.
  2. Write a one-page scale recommendation: go, wait or change, with the next user wave and its date.
  3. Confirm the long-term owner recorded in 2.8. If it's still to be decided, the sponsor names one now: scaling past the pilot needs a named owner.
  4. Take it to the sponsor (this is the gate).
  5. On a go, repeat 5.1 to 5.6 for the next user wave, reusing everything from this one.
- **Output:** the scale recommendation, the confirmed long-term owner and, on a go, the next user wave plan.
- **Done when:** the sponsor has decided.
- **Automation watch:**
  - First time: **Draft** for the recommendation, **Me** for the decision.
  - Note: what you reused from the first user wave. The more you reuse, the faster later user waves go.
  - Agent: **M6 Gate pack drafter** (agent library), reused. *Draft*.
- **For RM analytics:** expand only after the go/no-go check on the adoption dashboard.

---

## The Release and adopt gate

- **Who decides:** the sponsor and user leaders (in writing when the gate is clean; a meeting only if a criterion is contested or a decider asks for one; see the Product Machine).
- **Bring:** the pilot results and the scale recommendation.
- **Go means:** weekly use and leading results hit the targets, with no serious incidents, and the long-term owner confirmed before scaling.
- **No-go means:** fix the routine, the product or the training, then check again. Or stop, record why, and retire the AI product.
- **Record:** the date the gate pack was ready, the decision date, the decision, who decided and any conditions, in the decision log.

---

## Release and adopt automation review (do this at the gate)

Run the automation check from the Product Machine on every Me and Draft task,
using your first-time logs: cut first (should it exist, delete, simplify, make
it faster), then automate what's left (repeat? stable? safe alone?). Then update this shortlist and the Release and adopt
table in `product-machine.md`.

| Sub-step | Agent | First time | Aim for | Already specified? |
|---|---|---|---|---|
| 5.1 | M15 Readiness tracker | Draft | Auto | Yes, M15 |
| 5.1 | Pilot dashboard (Power BI, not an agent) | Draft | Draft | — |
| 5.2 | M16 Release automation | Me | Auto ⚠️ | Yes, M16 |
| 5.2 | Weekly usage report (Power BI, not an agent) | Me | Auto | — |
| 5.3 | None (stays with a person) | Me | Me | — |
| 5.4 | None: training users stays with a person | Me | Me | — |
| 5.4 | The product's onboarding coach (A6 in the RM plan) | Me | Auto | Yes, RM plan Appendix A |
| 5.5 | None: recruiting champions stays with a person | Me | Me | — |
| 5.5 | M17 Wins spotter | Me | Draft | Yes, M17 |
| 5.6 | M30 Feedback triage | Me | Auto | Yes, M30 |
| 5.6 | None: fixing and telling users what changed stays with a person | Me | Me | — |
| 5.7 | None: confirming the long-term owner stays with a person | Me | Me | — |
| 5.7 | M6 Gate pack drafter (shared) | Draft | Draft | Yes, M6 |

**First time** = how the task is done on the first project. **Aim for** = its kind in `product-machine.md`.

**Stays with a person:** working with managers on routines (5.3) and recruiting champions (5.5).

_Last updated: 2026-10-15_
