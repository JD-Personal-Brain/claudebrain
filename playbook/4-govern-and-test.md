# Step 4: Govern and test, the first time

**The question:** is it safe, fair and controlled?
**The gate:** all sign-offs recorded; monitoring plan agreed.
**Governance thread:** formal validation and sign-offs.

This is the formal approval, not the first time risk partners see the
product: they've been involved since 1.0. The product is **frozen** during
this step, so reviewers test what will actually ship. Several reviews can run
at once, so start 4.1, 4.2 and 4.6 on the first day. Fill in the first-time
log (see `README.md`) for every sub-step.

> ⚠️ **How much to trust this.** Written 2026-10-09 from my framework, the RM
> memo and general US banking practice (SR 11-7 model risk guidance, NIST AI
> RMF, fair-lending law), not from Associated Bank's own process. The bank's
> review steps, forms and timings are unknown, so every bank-specific line here
> is a guess ⚠️. Replace them on the first project.

---

## 4.1 Confirm the risk rating and register the product

- **Goal:** the product is formally rated and listed in the bank's inventory of models or AI uses.
- **Why it matters:** the rating sets how deep every other review goes. Unregistered AI is a classic audit finding.
- **Know first:** the early rating from 2.4, and the bank's model or AI inventory and who keeps it. ⚠️
- **First time, step by step:**
  1. Ask the risk partner what the formal submission needs, and by when.
  2. Update the intake with anything that changed since Define.
  3. Register the product in the inventory.
  4. Get the confirmed rating in writing.
- **Output:** the confirmed rating and the inventory entry.
- **Done when:** the rating is confirmed and recorded.
- **Automation watch:**
  - First time: **Me**, with risk.
  - Note: what changed between the early rating and the formal one, and why.
  - Agent: **M25 Risk intake assistant** (agent library) updates the intake from the latest brief. *Draft*.
- **For RM analytics:** expect a lower rating while the product stays assistive and away from credit decisions ⚠️. Risk decides.

---

## 4.2 Review data and privacy

- **Goal:** confirm that the data the AI sees matches what was approved, and that privacy rules are met.
- **Why it matters:** data about individuals, such as business owners and guarantors, is protected by law (for example, GLBA, whose privacy rules cover consumers). Business client data is protected by bank policy and contracts ⚠️. Either way, data use that drifted from the approval is a serious finding.
- **Know first:** the signed data contract (2.3), the data views (3.2), and the privacy team contact. ⚠️
- **First time, step by step:**
  1. List every field the product actually reads, from the live build rather than the plan.
  2. Compare the list with the data contract and explain any difference.
  3. Show how permissions and masking work, with a test as proof.
  4. Walk the privacy team through it and answer their questions in writing.
- **Output:** a data-use statement with proof, and the privacy team's notes.
- **Done when:** privacy has no open questions.
- **Automation watch:**
  - First time: **Draft**.
  - Note: how much of the statement was copied from the data contract.
  - Agent idea: a **data-use checker** (spec M13) that compares the fields actually read with the contract and flags differences. *Auto*, read-only. It runs on each new frozen version, and again monthly after launch.
- **For RM analytics:** each RM sees only clients they're already allowed to see.

---

## 4.3 Gather the testing evidence

- **Goal:** proof of accuracy, how often it makes things up, and how it holds up when someone tries to break it.
- **Why it matters:** this is the core evidence reviewers look at.
- **Know first:** the test results from 3.7, and what evidence format the risk team expects. ⚠️
- **First time, step by step:**
  1. Re-run the full test set on the frozen version.
  2. Report accuracy, made-up answers ("hallucinations"), relevance and permissions against the quality bar.
  3. Red-team it: try to make it reveal other users' data, give a credit decision, or answer off-topic.
  4. Record every failure, its fix and the re-test. Each fix creates a new frozen version: re-run the test set (M26) and the 4.5 control tests on it.
- **Output:** the test report and the red-team report.
- **Done when:** results meet the bar, and every red-team failure is fixed or accepted by risk.
- **Automation watch:**
  - First time: **Draft**, with red-teaming partly **Auto**.
  - Note: which attacks found real problems. Keep them for every future project.
  - Agents: **M26 Test grader** and **M27 Red-team agent** (agent library). Risk reviews every failure.
- **For RM analytics:** "must refuse" cases include another RM's clients and credit decisions.

---

## 4.4 Check fairness

- **Goal:** show that the product treats clients and users fairly across groups.
- **Why it matters:** if outputs touch credit, fair-lending law applies (for example, ECOA). Even without credit, uneven treatment is a reputational risk.
- **Know first:** which groups to compare (client segments, regions), and what compliance wants to see. ⚠️
- **First time, step by step:**
  1. With compliance, agree which groups to compare and what counts as a worrying difference.
  2. Run the comparison on test outputs.
  3. Explain any difference, or fix it.
  4. Get compliance's written view.
- **Output:** a fairness report and compliance's response.
- **Done when:** compliance has no open concerns.
- **Automation watch:**
  - First time: **Draft**.
  - Note: the groups and thresholds compliance chose. Reuse them.
  - Agent: **M28 Fairness monitor** (agent library). *Auto* report; compliance reviews. Its ongoing mode runs it again monthly after launch.
- **For RM analytics:** check that opportunities, especially credit-related ones, are spread fairly across segments and regions.

---

## 4.5 Confirm the controls work

- **Goal:** prove each control from 2.4 and 3.4 works on the frozen version.
- **Why it matters:** reviewers sign off on controls they've seen working, not on promises.
- **Know first:** the controls checklist from 3.4.
- **First time, step by step:**
  1. Re-run every control test on the frozen version.
  2. Show the audit log for a sample of actions.
  3. Show that a user must approve before anything reaches a client or changes a record.
  4. Feed an agent a missing or stale input on purpose, and show that it stops and alerts its owner instead of guessing.
  5. Show that meeting recaps are drafted only where consent is recorded.
  6. Confirm the frozen version reached test through the agreed build, test and live path, that the move to live is approved, and that IT has approved every connection the product uses (the data-sharing rules checked in 2.2).
  7. Update the controls checklist with fresh proof.
- **Output:** the updated controls checklist with proof.
- **Done when:** every control has fresh proof.
- **Automation watch:**
  - First time: **Draft**.
  - Note: which control tests you ran by hand.
  - Agent: the **controls checker** (spec M11) from 3.4. *Auto*, test environment only.
- **For RM analytics:** RM approval before saving call notes or sending follow-ups.

---

## 4.6 Confirm the vendor reviews

- **Goal:** every outside vendor involved has passed the bank's third-party risk review.
- **Why it matters:** an unreviewed vendor can stop a launch at the last minute.
- **Know first:** the vendors in the design (Microsoft, Salesforce, AWS, the model provider), and the vendor risk team. ⚠️ Some may already be approved for other uses.
- **First time, step by step:**
  1. List each vendor and what it does in this product.
  2. Ask vendor risk whether each is already approved **for this use**.
  3. Start any missing reviews on day one, because they can be slow ⚠️.
  4. Record each approval and its date.
- **Output:** the vendor list with approval status.
- **Done when:** every vendor is approved for this use.
- **Automation watch:**
  - First time: **Me**.
  - Note: which vendors were already approved. Keep a list, because the next project will likely reuse them.
  - Agent idea: none needed. A shared **approved vendors list** does the job.
- **For RM analytics:** Salesforce, Microsoft and AWS (with the model provider behind Bedrock).

---

## 4.7 Assemble the evidence pack and get sign-offs

- **Goal:** one pack the reviewers sign, and every sign-off recorded.
- **Why it matters:** a clear pack saves days of back-and-forth, and recorded sign-offs are the audit trail.
- **Know first:** everything from 4.1 to 4.6, and who must sign (risk, compliance, privacy, security). ⚠️
- **First time, step by step:**
  1. Put the outputs of 4.1 to 4.6 into one pack, using the bank's template if there is one ⚠️.
  2. Check every claim in it against its source.
  3. Send it to each signer with a due date.
  4. Track the replies; chase anything late and meet anyone who's stuck.
  5. Record each sign-off, with its date and any conditions.
- **Output:** the signed evidence pack.
- **Done when:** every required signer has signed.
- **Automation watch:**
  - First time: **Draft** for the pack, **Me** for chasing.
  - Note: how long each signer took, and what they asked.
  - Agents: **M29 Evidence pack assembler** (agent library), *Draft*. The **sign-off router** (spec M14) (Power Automate approvals) sends the requests and chases them, *Auto* ⚠️.
- **For RM analytics:** risk, compliance (including fair lending), privacy and security.

---

## 4.8 Agree the monitoring plan

- **Goal:** agree what will be watched after launch, how often, and what triggers action.
- **Why it matters:** approval usually depends on it, and it's what step 6 runs on.
- **Know first:** the measures (2.7) and what risk wants to monitor.
- **First time, step by step:**
  1. List what's watched: quality, guardrail blocks, user overrides, incidents and fairness.
  2. For each one: how often, the alert threshold, who's alerted and what they do.
  3. Write the incident process: who to call, and how to pause the product.
  4. Agree it with risk and operations.
- **Output:** the monitoring plan and the incident process.
- **Done when:** risk and operations have agreed it.
- **Automation watch:**
  - First time: **Draft**.
  - Note: the thresholds chosen. Reuse them next time.
  - Agent idea: a **monitoring plan template**, so the plan is drafted the same way every time. *Draft*. M32 Quality watchdog (agent library) then runs much of the plan in step 6.
- **For RM analytics:** re-test after every change, with alerts on drift.

---

## The Govern and test gate

- **Who decides:** the risk partner and the sponsor.
- **Bring:** the signed evidence pack and the monitoring plan.
- **Go means:** all sign-offs recorded, and the monitoring plan agreed.
- **No-go means:** fix what reviewers found, then re-test only what changed.
- **Record:** the decision and any conditions in the decision log.

---

## Govern and test automation review (do this at the gate)

| Sub-step | Agent | First time | Aim for | Already specified? |
|---|---|---|---|---|
| 4.1 | M25 Risk intake assistant | Me | Draft | Yes, M25 |
| 4.2 | Data-use checker | Draft | Auto | Yes, M13 |
| 4.3 | M26 Test grader, M27 Red-team agent | Draft | Auto | Yes, M26, M27 |
| 4.4 | M28 Fairness monitor | Draft | Auto | Yes, M28 (ongoing mode) |
| 4.5 | Controls checker (from 3.4) | Draft | Auto | Yes, M11 |
| 4.6 | Approved vendors list (not an agent) | Me | Me | — |
| 4.7 | M29 Evidence pack assembler | Draft | Draft | Yes, M29 |
| 4.7 | Sign-off router | Me | Auto ⚠️ | Yes, M14 |
| 4.8 | Monitoring plan template | Draft | Draft | Asset: agent library |

**First time** = how the task is done on the first project. **Aim for** = its kind in `product-framework.md`.

**Never automated:** the sign-offs themselves. Risk partners make every call.

_Last updated: 2026-10-09_
