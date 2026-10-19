# Step 4: Govern and test, the first time

**The question:** is it safe, fair and controlled?
**The gate:** all sign-offs recorded; monitoring plan agreed.
**Governance thread:** formal validation and sign-offs.

This is the formal approval, not the first time risk partners see the
product: they've been involved since 1.0. The product is **frozen** during
this step, so reviewers test what will actually ship. Several reviews can run
at once, so start 4.1, 4.2 and 4.6 on the first day. Fill in the first-time
log (see the Product Playbook's opening page) for every sub-step.

> ⚠️ **How much to trust this.** Written 2026-10-09 from my framework, the RM
> memo and general US banking practice (SR 11-7 model risk guidance, possibly replaced by SR 26-2: item W6
> in the Open Items log; NIST AI RMF; fair-lending law), not from Associated Bank's own process. The bank's
> review steps, forms and timings are unknown, so every bank-specific line here
> is a guess ⚠️. Replace them on the first project.

---

## 4.1 Confirm the risk rating and register the product

- **Goal:** the product is formally rated and listed in the bank's inventory of models or AI uses.
- **Why it matters:** the rating sets how deep every other review goes. Unregistered AI is a classic audit finding.
- **Know first:** the early rating from 2.4, and the bank's model or AI inventory and who keeps it. ⚠️
- **First time, step by step:**
  1. Ask the risk partner what the formal submission needs, and by when.
  2. Update the intake with anything that changed since Define, and confirm whether the product takes the higher-risk path (control K3, set at 2.4).
  3. Register the product in the inventory.
  4. Get the confirmed rating in writing.
- **Output:** the confirmed rating and the inventory entry.
- **Done when:** the rating is confirmed and recorded.
- **Automation watch:**
  - First time: **Me**, with risk.
  - Note: what changed between the early rating and the formal one, and why.
  - Agent: **M25 Risk intake assistant** (agent library) updates the intake from the latest brief. *Draft*.
- **For the RM Assistant:** expect a lower rating while the product stays assistive and away from credit decisions ⚠️. Risk decides.

---

## 4.2 Review data and privacy

- **Goal:** confirm that the data the AI sees matches what was approved, and that privacy rules are met.
- **Why it matters:** data about individuals may be protected by law (for example, GLBA, whose privacy rules cover consumers; ⚠️ whether it reaches business owners' and guarantors' data is for privacy to confirm; bank policy protects it either way). Business client data is protected by bank policy and contracts ⚠️. Either way, data use that drifted from the approval is a serious finding.
- **Know first:** the signed data contract (2.3), the data views (3.2), and the privacy team contact. ⚠️
- **First time, step by step:**
  1. List every field the product actually reads, from the frozen version in test rather than the plan.
  2. Compare the list with the data contract and explain any difference.
  3. Show how permissions and masking work, with a test as proof.
  4. Walk the privacy team through it and answer their questions in writing.
- **Output:** a data-use statement with proof, and the privacy team's notes.
- **Done when:** privacy has no open questions.
- **Automation watch:**
  - First time: **Draft**.
  - Note: how much of the statement was copied from the data contract.
  - Agent: **M13 Data-use checker** (agent library) that compares the fields actually read with the contract and flags differences. *Auto*, read-only. It runs on each new frozen version, and again monthly after launch.
- **For the RM Assistant:** each RM sees only clients they're already allowed to see.

---

## 4.3 Gather the testing evidence

- **Goal:** proof of accuracy, how often it makes things up, and how it holds up when someone tries to break it.
- **Why it matters:** this is the core evidence reviewers look at.
- **Know first:** the test results from 3.7, and what evidence format the risk team expects. ⚠️
- **First time, step by step:**
  1. Re-run the full test set on the frozen version.
  2. Report accuracy, made-up answers ("hallucinations"), relevance and permissions against the quality bar.
  3. Red-team it: try to make it reveal other users' data, give a credit decision or a price, or answer off-topic.
  4. Record every failure, its fix and the re-test. Each fix creates a new frozen version: re-run the test set (M26) and the 4.5 control tests on it, and the fairness check (4.4) if the fix could change who gets what.
- **Output:** the test report and the red-team report.
- **Done when:** results meet the bar, and every red-team failure is fixed or accepted by risk.
- **Automation watch:**
  - First time: **Draft**, with red-teaming partly **Auto**.
  - Note: which attacks found real problems. Keep them for every future project.
  - Agents: **M26 Test grader** and **M27 Red-team agent** (agent library). Risk reviews every failure.
- **For the RM Assistant:** "must refuse" cases include another RM's clients and credit decisions.

---

## 4.4 Check fairness

- **Goal:** show that the product treats clients and users fairly across groups.
- **Why it matters:** if outputs touch credit, fair-lending law applies (for example, ECOA). Even without credit, uneven treatment is a reputational risk.
- **Know first:** which groups to compare (client segments, regions), and what compliance wants to see. ⚠️
- **First time, step by step:**
  1. With compliance, agree which groups to compare and what counts as a worrying difference. On the higher-risk path (control K3) this check is always required.
  2. Run the comparison on test outputs.
  3. Explain any difference, or fix it.
  4. Get compliance's written view.
- **Output:** a fairness report and compliance's response.
- **Done when:** compliance has no open concerns.
- **Automation watch:**
  - First time: **Draft**.
  - Note: the groups and thresholds compliance chose. Reuse them.
  - Agent: **M28 Fairness monitor** (agent library). *Auto* report; compliance reviews. Its ongoing mode runs it again monthly after launch.
- **For the RM Assistant:** check that opportunities are spread fairly across segments and regions. Wave 1 suggests only deposit and treasury gaps; credit-related suggestions arrive only with the portfolio manager work (agreed 2026-10-18).

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
  6. Confirm the frozen version reached test through the agreed build, test and live path, that the move to live has a named approver and an agreed route (the approval itself is recorded in 5.2), and that IT has approved every connection the product uses (the data-sharing rules checked in 2.2).
  7. Show that the guardrails block off-topic answers, harmful content and sensitive data such as account numbers (the settings from 3.4, with the 4.3 red-team results as proof) (K8).
  8. Show that an agent stays read-only: an action the agent isn't allowed to take is refused (K2).
  9. Update the controls checklist with fresh proof.
  10. Draft the monitoring plan (4.8) alongside this check, so it goes into the evidence pack as a draft.
- **Output:** the updated controls checklist with proof.
- **Done when:** every control has fresh proof.
- **Automation watch:**
  - First time: **Draft**.
  - Note: which control tests you ran by hand.
  - Agent: **M11 Controls checker** (agent library) from 3.4. *Auto*, test environment only.
- **For the RM Assistant:** RM approval before saving call notes or sending follow-ups.

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
  - Agent: none needed. A shared **approved vendors list** does the job.
- **For the RM Assistant:** Salesforce and Microsoft; AWS (and the model provider behind Bedrock) only if Bedrock is used.

---

## 4.7 Assemble the evidence pack and get sign-offs

- **Goal:** one pack the reviewers sign, and every sign-off recorded.
- **Why it matters:** a clear pack saves days of back-and-forth, and recorded sign-offs are the audit trail.
- **Know first:** everything from 4.1 to 4.6, the draft monitoring plan (4.8), and who must sign (risk, compliance, privacy, security). ⚠️
- **First time, step by step:**
  1. Put the outputs of 4.1 to 4.6, and the draft monitoring plan (4.8), into one pack, using the bank's template if there is one ⚠️.
  2. Check every claim in it against its source.
  3. Send it to each signer with a due date. On the higher-risk path (control K3), the credit policy owner signs too ⚠️ [name needed]. When the product has early warning rules, credit risk signs the rules ⚠️.
  4. Track the replies; chase anything late and meet anyone who's stuck.
  5. Record each sign-off, with its date and any conditions, and the full user group the approval covers (the planned rollout from 2.8, not only the pilot group).
- **Output:** the signed evidence pack.
- **Done when:** every required signer has signed.
- **Automation watch:**
  - First time: **Draft** for the pack, **Me** for chasing.
  - Note: how long each signer took, and what they asked.
  - Agents: **M29 Evidence pack assembler** (agent library), *Draft*. **M14 Sign-off router** (agent library; Power Automate approvals) sends the requests and chases them, *Auto* ⚠️.
- **For the RM Assistant:** risk, compliance (including fair lending), privacy and security.

---

## 4.8 Agree the monitoring plan

- **Goal:** agree what will be watched after launch, how often, and what triggers action. The plan is drafted alongside 4.5 and goes into the evidence pack (4.7) as a draft; this sub-step finalises it.
- **Why it matters:** approval usually depends on it, and it's what step 6 runs on.
- **Know first:** the measures (2.7) and what risk wants to monitor.
- **First time, step by step:**
  1. List what's watched: quality, guardrail blocks, user overrides, incidents, fairness, data use against the data contract (M13) and data quality on each refresh (M24). Add the **control watch list**: one line per control that no other step watches after launch (K2, K6, K10, K12, K14, K19, K20, K21, K23, K24 and K25 in the Controls Catalog), each with how it's checked; M11 Controls checker re-runs the list monthly (added 2026-10-18).
  2. For each one: how often, the alert threshold, who's alerted and what they do.
  3. Write the incident process: who to call, who may pause the product (the product manager or operations, per the plan) and how. A serious incident is [X], set in the plan with the risk partner.
  4. Agree it with risk and operations.
- **Output:** the monitoring plan and the incident process.
- **Done when:** risk and operations have agreed it.
- **Automation watch:**
  - First time: **Draft**.
  - Note: the thresholds chosen. Reuse them next time.
  - Asset: the **monitoring plan template** (not an agent), so the plan is drafted the same way every time. *Draft*. M32 Quality watchdog (agent library) then runs much of the plan in step 6.
- **For the RM Assistant:** re-test after every change, with alerts on drift.

---

## The Govern and test gate

- **Who decides:** the risk partner and the sponsor, who approve the signed evidence pack in writing; partner sign-offs can't be overruled. A meeting happens only if a criterion is contested or a decider asks for one (see the Product Machine; ⚠️ the bank's approval policy may require a committee meeting).
- **Bring:** the signed evidence pack and the monitoring plan.
- **Go means:** all sign-offs recorded, and the monitoring plan agreed.
- **No-go means:** fix what reviewers found; each fix is a new frozen version, so re-run the test set and the control tests, and send changed evidence back to the signers it affects. Or stop, record why, and retire the AI product.
- **Record:** the date the gate pack was ready, the decision date, the decision, who decided and any conditions, in the decision log.

---

## Govern and test automation review (do this at the gate)

Run the automation check from the Product Machine on every Me and Draft task,
using your first-time logs: cut first (should it exist, delete, simplify, make
it faster), then automate what's left (repeat? stable? safe alone?). Then update this shortlist and the Govern and test
table on the Product Machine page.

| Sub-step | Agent | First time | Aim for | Already specified? |
|---|---|---|---|---|
| 4.1 | M25 Risk intake assistant | Me | Draft | Yes, M25 |
| 4.2 | M13 Data-use checker | Draft | Auto ⚠️ | Yes, M13 |
| 4.2 | None: walking privacy through it stays with a person | Me | Me | — |
| 4.3 | M26 Test grader, M27 Red-team agent | Draft | Auto | Yes, M26, M27 |
| 4.4 | M28 Fairness monitor | Draft | Auto ⚠️ | Yes, M28 (ongoing mode) |
| 4.5 | M11 Controls checker (from 3.4) | Draft | Auto | Yes, M11 |
| 4.6 | None (the approved vendors list, an asset) | Me | Me | — |
| 4.7 | M29 Evidence pack assembler | Draft | Draft | Yes, M29 |
| 4.7 | M14 Sign-off router | Me | Auto ⚠️ | Yes, M14 |
| 4.7 | None: unblocking a stuck sign-off stays with a person | Me | Me | — |
| 4.8 | None (the monitoring plan template, an asset) | Draft | Draft | Asset: agent library |

**First time** = how the task is done on the first project. **Aim for** = its kind on the Product Machine page.

**Never automated:** the sign-offs themselves. Risk partners make every call.

_Last updated: 2026-10-19_
