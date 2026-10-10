# Step 3: Build, the first time

**The question:** what's the smallest version users will use and trust?
**The gate:** it meets the quality bar in testing, and every control has proof.
**Governance thread:** controls built in; test set created.

Build runs in short cycles: build a piece, test it, show users, repeat.
Start the test set (3.6) on day one, not at the end. Fill in the first-time
log (see `README.md`) for every sub-step.

> ⚠️ **How much to trust this.** Written 2026-10-09 from my framework, the RM
> memo and general practice, not from Associated Bank. In this step platform
> teams or engineers do much of the building; the PM sets requirements, checks
> quality and makes the calls. Lines marked ⚠️ are guesses about the bank.

---

## 3.1 Design the solution and choose the AI capabilities

- **Goal:** agree how the pieces fit: which agents, data flows, automations and integrations.
- **Why it matters:** a one-page design stops each team building its own idea of the product.
- **Know first:**
  - The release 1 scope, data contract and control requirements from Define.
  - The AI principles in `product-framework.md`: assistive first, one job each, built where the work happens.
- **First time, step by step:**
  1. Draw the flow on one page: data in → logic → AI writing → where the user sees it → feedback back in.
  2. For each AI piece, write an agent spec: mission, inputs, allowed actions, outputs, stop condition, proof it worked, person in charge (memo Appendix A is the pattern).
  3. Keep every agent read-only unless a user clicks to approve an action.
  4. Give each agent a stop rule: if its inputs are missing, stale or fail a check, it stops and alerts its owner instead of guessing.
  5. Review the design with the platform team and the risk partner.
- **Output:** a one-page design and an agent spec for each agent.
- **Done when:** the platform team and the risk partner have agreed the design.
- **Automation watch:**
  - First time: **Me**, with platform teams.
  - Note: which spec fields were hard to fill in. That tells you what to ask earlier.
  - Agent idea: an **agent spec drafter** (spec M10) that turns a user story into a first spec. *Draft*.
- **For RM analytics:** A1 Signal finder → A2 Insight writer → Salesforce record and the A4 Weekly opportunity digest. A3 handles prep and follow-up (memo Appendix A).

---

## 3.2 Prepare trusted data

- **Goal:** clean, permission-checked data views that the product reads from.
- **Why it matters:** AI quality can't beat data quality. Wrong numbers in front of users kill trust fast.
- **Know first:** the data contract (2.3), the data engineer assigned, and the bank's masking and access rules (Snowflake Horizon). ⚠️
- **First time, step by step:**
  1. With the data engineer, build a view for each source in the contract.
  2. Add the quality checks from the contract, such as no blanks and a refresh within [X] hours.
  3. Apply the permission rule: each user only sees data they're already allowed to see.
  4. Spot-check 20 records by hand against the source system.
- **Output:** the data views, with checks and permissions.
- **Done when:** the spot-check matches and the checks run every refresh.
- **Automation watch:**
  - First time: **Me**, with the data engineer.
  - Note: which checks failed in the first week.
  - Agent: the quality checks become **Auto** once they run on every refresh. M24 Data contract checker (agent library) watches them: its ongoing mode runs on every data refresh.
- **For RM analytics:** signal views for balance trends, product gaps and activity.

---

## 3.3 Build the logic: simple rules first, AI explains

- **Goal:** produce the core output (an insight, a draft or an answer) in a way people can explain.
- **Why it matters:** in a bank, "the AI said so" isn't a reason. Simple, visible rules are easier to trust, test and approve.
- **Know first:** the stories and acceptance criteria (2.5), and which AI model is approved and where it runs. ⚠️
- **First time, step by step:**
  1. Write the business rules in plain words with users, for example "flag clients whose balances fell [X]% in 90 days."
  2. Have them built as rules or scores, not as AI.
  3. Use AI only to explain each result in plain English and suggest a next step, citing the numbers.
  4. Write the prompts using `prompting.md`, and keep every version.
  5. Check 10 to 20 outputs by hand with a user after every change.
- **Output:** working rules and prompts, with every version kept.
- **Done when:** users agree the outputs are right and useful on real examples.
- **Automation watch:**
  - First time: **Draft**. AI drafts prompts; you and users check.
  - Note: which prompt changes fixed which problems. Keep a prompt change log.
  - Agent: none new. The checking becomes **M26 Test grader** (3.7).
- **For RM analytics:** A1 finds signals with explainable rules; A2 writes the reason and talking points.

---

## 3.4 Build in the controls

- **Goal:** the control requirements from 2.4 are built, not just promised.
- **Why it matters:** step 4 checks the controls. If they're built now, approval is a confirmation, not a rebuild.
- **Know first:** the control list (2.4), and the platform's built-in protections (Bedrock Guardrails, Einstein Trust Layer, Purview labels). ⚠️ Check what the bank has turned on.
- **First time, step by step:**
  1. For each control requirement, name the feature that meets it and who builds it.
  2. Human approval: nothing reaches a client or changes a record without a user's click.
  3. Guardrails: block sensitive data and off-topic answers.
  4. Logging: every AI action recorded, with who, what and when.
  5. Recordings: meeting recaps come only from recordings made with consent under the bank's recording policy; otherwise the AI works from the user's own notes.
  6. Test each control on purpose, for example by trying to see another user's clients.
- **Output:** a controls checklist with proof for each one (a screenshot or a test result).
- **Done when:** every control has proof.
- **Automation watch:**
  - First time: **Me**, with platform teams.
  - Note: which controls the platform gave you for free, and which needed building. Next project, choose platforms with that in mind.
  - Agent idea: a **controls checker** (spec M11) that re-runs the control tests on every release. *Auto*, test environment only.
- **For RM analytics:** RMs approve before anything is saved or sent; each RM sees only their permitted clients.

---

## 3.5 Deliver it where users work, with sources and feedback

- **Goal:** the output appears inside tools users already use, shows its source and takes one-click feedback.
- **Why it matters:** a new place to go is a new habit to form, and most new tools lose that fight. Sources build trust; feedback steers the backlog.
- **Know first:** the platform (2.2) and the design (3.1).
- **First time, step by step:**
  1. Place the output where users already look, such as the client record or a weekly message.
  2. Make every output link to the numbers or documents behind it.
  3. Add one-click feedback (accept, reject, change), with a short reason when rejecting.
  4. Show it to 3 to 5 users each cycle, and fix what confuses them.
- **Output:** the product working in the test environment.
- **Done when:** users can use it without help, and feedback is being saved.
- **Automation watch:**
  - First time: **Me**, with platform teams.
  - Note: the feedback options users actually used.
  - Agent: the feedback saved here feeds **M30 Feedback triage** in step 5.
- **For RM analytics:** insights on the Salesforce client record, plus the Monday digest in Teams or Outlook.

---

## 3.6 Build the test set

- **Goal:** a set of real examples with known good answers, used to test every version.
- **Why it matters:** without a test set, "it's better" is an opinion. With one, it's a score, and it's the core evidence in step 4.
- **Know first:** the quality bar (2.7), and 3 to 5 experienced users willing to grade answers.
- **First time, step by step:**
  1. Collect [X] real examples covering normal, tricky and edge cases. ⚠️ A common start is about 50 to 100.
  2. Have experienced users write or approve the good answer for each one.
  3. Add "must refuse" cases, such as another user's client or a credit decision.
  4. Store it with a version number, and never change old versions.
- **Output:** the test set, versioned.
- **Done when:** it covers every story in release 1 and the main risks.
- **Automation watch:**
  - First time: **Draft**. AI suggests cases; users approve the answers.
  - Note: how long grading took per example.
  - Agent idea: a **test case generator** (spec M12) that suggests new cases from feedback and failures. *Draft*.
- **For RM analytics:** real client examples graded by experienced RMs.

---

## 3.7 Test against the quality bar

- **Goal:** prove the build meets the bar set in Define.
- **Why it matters:** this is the gate. It's also the first run of what becomes automatic re-testing in step 6.
- **Know first:** the test set (3.6) and the quality bar thresholds (2.7).
- **First time, step by step:**
  1. Run the test set against the current version.
  2. Score it on each part of the quality bar. Permissions must be 100%.
  3. List the failures, fix the biggest ones and re-run.
  4. Have experienced users grade a sample of outputs, to check the scoring.
  5. Build the gate pack: the design, the controls checklist, test results and user feedback.
- **Output:** a test report and the gate pack.
- **Done when:** every threshold is met, or the sponsor accepts a documented gap.
- **Automation watch:**
  - First time: **Draft**.
  - Note: how long a full test run took by hand. That's the time the agent saves on every later change.
  - Agent: **M26 Test grader** (agent library). It scores every version; users grade a sample. Aim for **Auto** on every new version.
  - Agent idea: the **gate pack drafter** (spec M6) from Discover, reused for the Build gate pack. *Draft*.
- **For RM analytics:** accuracy (numbers match the source), relevance and usefulness rated by RMs.

---

## The Build gate

- **Who decides:** the sponsor, with the product manager.
- **Bring:** the gate pack from 3.7.
- **Go means:** it meets the quality bar in testing, and every control has proof.
- **No-go means:** another build cycle on the failures, or a smaller scope.
- **Record:** the decision in the decision log.

---

## Build automation review (do this at the gate)

| Sub-step | Agent | First time | Aim for | Already specified? |
|---|---|---|---|---|
| 3.1 | Agent spec drafter | Me | Draft | Yes, M10 |
| 3.2 | Data quality checks (M24 in an ongoing mode) | Me | Auto | Yes, M24 (ongoing mode) |
| 3.3 | None new (M26 checks the outputs) | Draft | Draft | — |
| 3.4 | Controls checker | Me | Auto (test only) | Yes, M11 |
| 3.5 | None (its feedback feeds M30 in step 5) | Me | Me | — |
| 3.6 | Test case generator | Draft | Draft | Yes, M12 |
| 3.7 | M26 Test grader | Draft | Auto | Yes, M26 |
| 3.7 | Gate pack drafter | Draft | Draft | Yes, M6 |

**First time** = how the task is done on the first project. **Aim for** = its kind in `product-framework.md`.

_Last updated: 2026-10-09_
