# Step 2: Define, the first time

**The question:** what exactly do we build first, and how will we know it worked?
**The gate:** brief, data contract and risk rating agreed; value model shows payback within [X] months.
**Governance thread:** risk intake and early rating; data use approved.

Work through 2.1 to 2.8. 2.3 (data) and 2.4 (risk) take the longest because
they wait on other people, so **start both in your first week**, alongside 2.1.
Fill in the first-time log (see the Product Playbook's opening page) for every sub-step.

> ⚠️ **How much to trust this.** Written 2026-10-09 from my framework, the RM
> memo and general practice, not from Associated Bank. Lines marked ⚠️ are
> guesses about how the bank works.

---

## 2.1 Write the problem and the outcome

- **Goal:** one sentence for the problem and one for the measurable outcome.
- **Why it matters:** every later choice (scope, data, tests) is checked against these two sentences. If they're fuzzy, scope creeps.
- **Know first:** the Discover gate pack, especially the chosen target, the baseline and the users' own words.
- **First time, step by step:**
  1. Problem: "[Users] lose / miss [what], because [cause], shown by [evidence from Discover]."
  2. Outcome: "[Measure] moves from [baseline] to [target] by [date] for [pilot group]." Use [X] if the target isn't agreed yet.
  3. Read both aloud to two users and the sponsor. Do they recognize them?
  4. Put them at the top of the one-page product brief.
- **Output:** the first lines of the product brief.
- **Done when:** the sponsor agrees, and a user would say "yes, that's my problem."
- **Automation watch:**
  - First time: **Draft**.
  - Note: how many rewrites it took, and why.
  - Agent: **M23 Requirements drafter** (agent library) drafts both sentences from the Discover findings. You edit, and the sponsor approves.
- **For the RM Assistant:** "RMs miss growth opportunities in their existing book because signals are scattered across systems," with the outcome tied to AI-sourced pipeline.

---

## 2.2 Choose the platform and delivery path

- **Goal:** decide where the product will live and how it gets from test to live.
- **Why it matters:** the platform decides what's possible, what it costs, which approvals apply and how fast you can pilot.
- **Know first:**
  - Where users spend their day (from 1.3 and 1.4).
  - The "pick the layer" rule of thumb in the Tech Stack Guide.
  - Platform team contacts for Salesforce, Microsoft and AWS.
  - IT's data rules (DLP) for Power Platform connectors. ⚠️ Check these early, because they often block ideas.
- **First time, step by step:**
  1. Score the candidate platforms on five criteria: where users work, where the data lives, fit with approvals and controls, cost model, and speed to a pilot.
  2. Meet each platform team for 30 minutes: "Could we do X? What would block us?"
  3. Write the delivery path: build environment → test → live, who moves it, and what approval each move needs.
  4. Check the approved vendors list for the platform and model; if a vendor review is missing, start it now, because it is slow (K14).
  5. Record the choice and the runner-up in the decision log.
- **Output:** the platform decision with its scores, and the delivery path.
- **Done when:** the platform team agrees it's feasible, the decision is logged, and IT has confirmed the planned connections are allowed under its data rules (K20).
- **Automation watch:**
  - First time: **Me**, with platform teams.
  - Note: the questions each platform team asked. They become a standard feasibility checklist.
  - Agent: **M7 Platform fit checker** (agent library) that scores a brief against the five criteria and lists known blockers. *Draft*.
- **For the RM Assistant:** the meeting follow-up's recap and email in M365 Copilot first; insights, the brief and call notes on the Salesforce client record (Agentforce, Prompt Builder), with the Monday list sent through Power Automate (memo section 5; ⚠️ an assumption to confirm in Discover).

---

## 2.3 Define the data contract

- **Goal:** write down exactly which data the product uses, how fresh it must be and how it's checked.
- **Why it matters:** most AI projects slip on data. A signed contract means no feature depends on data you don't have.
- **Know first:**
  - Data owners for each source (Snowflake, Salesforce).
  - Which tables are trusted ("certified") and who may see what. ⚠️ Ask the data team how certification works at the bank.
- **First time, step by step:**
  1. From the Discover target and the 1.6 mock-up screens, list a first set of fields the product needs. Update the list when the user stories (2.5) are done.
  2. For each field: source, owner, refresh rate needed, refresh rate today, quality check, who may see it, and whether it is sensitive (to be masked or labeled).
  3. Check that each field exists and is fresh enough. Mark the gaps.
  4. Agree with the data owner how each gap is fixed or worked around.
  5. Get the data owner's sign-off, in writing.
  6. After 2.5, add any new fields and get the data owner to re-confirm in writing.
  7. **If the product works from documents** (credit memos, financial statements, call notes), write the contract for documents instead of fields: each source (library or folder), its content owner, how often it is re-indexed (re-read by the search, so new or changed documents show up), who may see each document, and the check that every answer cites the document it came from.
- **Output:** the data contract table and a gap list.
- **Done when:** every field is either confirmed or has an agreed fix, and the data owner has signed the final field list (for documents, the content owner has signed the source list).
- **Automation watch:**
  - First time: **Draft**.
  - Note: how long the sign-off took, and which gaps came up. Expect the same gaps on the next project.
  - Agent: **M24 Data contract checker** (agent library). It checks fields, freshness and quality read-only, and the data owner signs off.
- **For the RM Assistant:** balances, product holdings and trends from Snowflake; client records, pipeline and activity from Salesforce ⚠️ (where each lives is still to confirm).

---

## 2.4 Start the risk intake and list the control requirements

- **Goal:** get an early risk rating, and know which controls you must build in.
- **Why it matters:** controls are much cheaper to build in from the start than to bolt on at step 4. An early rating also tells you how long approval will take.
- **Know first:**
  - The bank's AI or model risk intake process and form. ⚠️ Not known yet.
  - Your risk partner from 1.0.
  - The governance basics in the Tech Stack Guide (SR 11-7, possibly replaced by SR 26-2: item PL7 in the Open Items log; privacy; fair lending).
- **First time, step by step:**
  1. Get the intake form and ask the risk partner how long a review usually takes.
  2. Fill it in from the brief so far (2.1) and the Discover gate pack: what the product does, which data (the first field list from 2.3), who uses it, what it can change, and whether anything reaches a client.
  3. Say plainly what it does **not** do, for example "no credit decisions, no pricing" (control K3). If its output informs a credit decision (a credit memo draft, an early-warning flag), mark it for the **higher-risk path** in step 4, and agree with the credit policy owner ⚠️ [name needed] what its drafts may contain (for example, whether a draft may carry a recommendation). The higher-risk path means a fairness check agreed with compliance (4.4), must-refuse cases in the test set (3.6), and a sign-off from the credit policy owner as well (4.7). ⚠️ The bank's model risk policy may add more.
  4. Submit it, then meet the risk partner to walk through it.
  5. Write down the control requirements they give you (human approval, logging, guardrails, permissions, consent for any recorded meeting) and copy them into the backlog as must-haves.
  6. Share the control requirements list with compliance, privacy and security, so nothing in step 4 is a surprise.
- **Output:** the submitted intake, an early rating, and a list of control requirements.
- **Done when:** the risk partner has given an early rating and the control list.
- **Automation watch:**
  - First time: **Draft**. You fill it in; risk rates it.
  - Note: which questions on the form were hard to answer. Next time, answer them earlier in Discover.
  - Agent: **M25 Risk intake assistant** (agent library). It pre-fills the intake and flags likely high-risk areas, and the risk partner sets the rating.
- **For the RM Assistant:** any insight that suggests a credit product goes to compliance review, because fair-lending rules apply to business credit too.

---

## 2.5 Write user stories and acceptance criteria

- **Goal:** turn the problem into small, testable pieces of work.
- **Why it matters:** the stories are what gets built, and their acceptance criteria are how you know each piece is done.
- **Know first:** the brief (2.1), the Discover themes, and the control requirements (2.4).
- **First time, step by step:**
  1. Write each story as "As a [user], I need [what], so that [why]."
  2. Under each, add 2 to 4 acceptance criteria: "Given [situation], when [action], then [result]."
  3. Add control stories once the control list comes back from 2.4, for example "As a risk partner, I need every AI action logged."
  4. Review them with two users and one engineer: are they clear, and are they buildable?
  5. Put them in the backlog tool. ⚠️ Which tool the bank uses isn't known yet.
- **Output:** a backlog of stories with acceptance criteria.
- **Done when:** every story in the first release has criteria that a tester could check.
- **Automation watch:**
  - First time: **Draft**.
  - Note: which story patterns repeat, such as permissions, logging and feedback. These become a story library for every project.
  - Agent: **M23 Requirements drafter** (agent library).
- **For the RM Assistant:** "As an RM, each Monday I need my top [X] client opportunities, with the reason and a suggested next step, so I can plan my calls."

---

## 2.6 Set priorities and record the trade-offs

- **Goal:** rank the backlog and write down why.
- **Why it matters:** partners will ask "why not X?" A recorded trade-off answers that once, instead of in every meeting.
- **Know first:** the stories (2.5), rough effort from engineers, and risk from 2.4.
- **First time, step by step:**
  1. Score each story on value, effort and risk (high, medium or low is enough).
  2. Rank them. Must-have controls go first, whatever their score.
  3. For each hard call, write a decision-log entry: what was chosen, what was given up, who decided and why.
  4. Review the ranking with the sponsor.
- **Output:** a ranked backlog and decision-log entries.
- **Done when:** the sponsor agrees with the top of the list.
- **Automation watch:**
  - First time: **Me**. Trade-offs are judgment calls.
  - Note: which scoring questions actually changed the order.
  - Agent: **M8 Decision log drafter** (agent library) that writes log entries from meeting recaps (M365 Copilot). *Draft*.
- **For the RM Assistant:** the brief, the meeting follow-up (with call notes into Salesforce) and the Monday opportunity list come first.

---

## 2.7 Set the measures, quality bar and value model

- **Goal:** decide how success is measured, how good is good enough, and whether it pays for itself.
- **Why it matters:** this is what the Release and Measure gates will judge against. Set it now, before results come in, so no one moves the goalposts.
- **Know first:**
  - The five kinds of measures and the quality bar in the Product Framework.
  - The baseline and the first value model from 1.7.
  - A Finance contact, to agree how impact is counted.
- **First time, step by step:**
  1. Pick one or two measures for each of the five kinds: usage, quality, business impact, adoption, risk and controls.
  2. Set the quality bar thresholds: accuracy, sources shown, relevance, usefulness, and permissions (zero tolerance). Use [X] until agreed.
  3. Fill in the value model with real numbers where you have them, and [X] where you don't.
  4. Agree with Finance how impact is counted: how wins are tagged, and how the comparison group is used.
  5. Define each measure exactly (source, formula, owner), so the dashboard can be built from it.
  6. If a definition changed from the one recorded in 1.7, or a new business-impact measure was added, record its baseline now (date, source, definition), and point M5 at the final definitions; once 2.8 confirms the pilot and comparison groups, split the baseline by group.
- **Output:** the measures sheet, the quality bar, the value model, and the method Finance agreed.
- **Done when:** the sponsor and Finance agree, and every measure has a source.
- **Automation watch:**
  - First time: **Draft**.
  - Note: which measures you could pull automatically and which needed someone by hand.
  - Agent: **M9 Measures sheet builder** (agent library) that drafts the measures and their sources from the brief and the data contract. *Draft*.
- **For the RM Assistant:** every AI-sourced opportunity is tagged in Salesforce from day one, and Finance agrees the comparison method before the pilot (memo section 2).

---

## 2.8 Scope the first release and the pilot group

- **Goal:** pick the smallest useful version and who tries it first.
- **Why it matters:** a small first release reaches users sooner and teaches you more than a big one.
- **Know first:** the ranked backlog (2.6), the measures (2.7), and user leaders' input on who should pilot.
- **First time, step by step:**
  1. Draw a line in the backlog: above it is release 1.
  2. Test it: "Would a user use this every week, even if it had nothing else?" If not, move the line.
  3. Confirm the final pilot group ([X] users) and the comparison group proposed in 1.7, with user leaders, and the full user group the product is planned to reach (the rollout). Step 4 approves that full group, so user waves inside it (5.7) don't go back through step 4.
  4. Set a target date for release 1, paced by what really blocks you (data access, approvals), not by habit.
  5. Ask the sponsor who should own the product long term, for example someone in a revenue line. Record the name, or "to be decided" with a date to decide by. Until then, the product manager owns it.
  6. Complete the one-page brief: problem, outcome, users (pilot group and planned rollout), platform (2.2), release 1 scope, what's out of scope and the long-term owner.
  7. Build the gate pack: the brief, data contract, risk rating and controls, the backlog with release 1 marked, measures, value model, pilot group and date.
- **Output:** the release 1 scope, the pilot and comparison groups, the planned rollout group, a date, the long-term owner (or a date to decide), the finished brief and the gate pack.
- **Done when:** the gate pack is ready.
- **Automation watch:**
  - First time: **Me** for the scope, **Draft** for the pack.
  - Note: what you copied into the gate pack by hand.
  - Agent: **M6 Gate pack drafter** (agent library) from Discover, reused here. *Draft*.
- **For the RM Assistant:** feature wave 1 = three capabilities: the pre-meeting client brief, the meeting follow-up (recap, email and call notes into Salesforce) and the Monday opportunity list.

---

## The Define gate

- **Who decides:** the sponsor, with the risk partner and the data owner, and on the higher-risk path the credit policy owner (in writing when the gate is clean; a meeting only if a criterion is contested or a decider asks for one; see the Product Machine).
- **Bring:** the gate pack from 2.8.
- **Go means:** brief, data contract and risk rating agreed, and the value model shows payback within [X] months.
- **No-go means:** fix the gap (often data or risk), or narrow the scope.
- **Record:** the date the gate pack was ready, the decision date, the decision, who decided and any conditions, in the decision log.

---

## Define automation review (do this at the gate)

Run the automation check from the Product Machine on every Me and Draft task,
using your first-time logs: cut first (should it exist, delete, simplify, make
it faster), then automate what's left (repeat? stable? safe alone?). Then update this shortlist and the Define
table on the Product Machine page.

| Sub-step | Agent | First time | Aim for | Already specified? |
|---|---|---|---|---|
| 2.1, 2.5 | M23 Requirements drafter | Draft | Draft | Yes, M23 |
| 2.2 | M7 Platform fit checker | Me | Draft | Yes, M7 |
| 2.3 | M24 Data contract checker | Draft | Draft | Yes, M24 |
| 2.4 | M25 Risk intake assistant | Draft | Draft | Yes, M25 |
| 2.5 | None (a story library of reusable stories) | Draft | Draft | Asset: agent library |
| 2.6 | M8 Decision log drafter | Me | Draft | Yes, M8 |
| 2.6, 2.8 | None: priorities and scope stay with a person | Me | Me | — |
| 2.7 | M9 Measures sheet builder | Draft | Draft | Yes, M9 |
| 2.8 | None: recording the long-term owner stays with a person | Me | Me | — |
| 2.8 | M6 Gate pack drafter (shared with Discover) | Draft | Draft | Yes, M6 |

**First time** = how the task is done on the first project. **Aim for** = its kind on the Product Machine page.

_Last updated: 2026-10-19_
