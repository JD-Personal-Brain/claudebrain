# Controls catalog

Every governance control the delivery machine uses, in one place. A control is
a safeguard built into a product so the bank can trust it: who must approve,
what the AI may not do, and how we prove it.

> ⚠️ **How much to trust this.** Gathered on 2026-10-09 from my product
> framework, the playbook and the tech stack guide, not from Associated Bank.
> The bank's own control list comes from its risk partner at sub-step 2.4, and
> it replaces this one where they differ. "Tool" lines are guesses.

Each control says where it is **set** (agreed as a requirement), **built**,
**proved** (shown working to reviewers) and **watched** (after launch).

---

### K1. A person decides
- **Group:** People in charge
- **What it is:** the AI drafts or suggests, and a named person approves before anything reaches a client or changes a record.
- **Why it matters:** the bank stays accountable for every client message and every record. This is the control reviewers ask about first.
- **Set in:** 2.4
- **Built in:** 3.1, 3.4
- **Proved in:** 4.5
- **Watched in:** 6.3 (how often users change or reject what the AI wrote)
- **Tool (guess):** approval steps in Salesforce and Power Automate
- **Proof:** a test showing nothing is sent or saved without a click from the user

### K2. Read-only unless approved
- **Group:** People in charge
- **What it is:** every agent only reads by default and has a short list of things it may do.
- **Why it matters:** the more an agent can do, the more review it needs. A short list keeps the risk rating low.
- **Set in:** 2.4
- **Built in:** 3.1
- **Proved in:** 4.5
- **Watched in:** not covered in the playbook yet
- **Tool (guess):** the agent's permissions on each platform
- **Proof:** the agent spec's "allowed" and "not allowed" lists, and a test that a blocked action fails

### K3. No credit decisions or pricing
- **Group:** People in charge
- **What it is:** the intake says plainly what the product does not do, such as credit decisions or pricing. Any insight that suggests a credit product goes to compliance review.
- **Why it matters:** fair-lending rules apply to business credit too, and they set a much higher bar.
- **Set in:** 2.4
- **Built in:** 3.4
- **Proved in:** 4.3
- **Watched in:** 6.3
- **Tool (guess):** guardrail filters
- **Proof:** a red-team test (someone trying to break it on purpose) showing it won't give a credit decision

### K4. Users see only what they're allowed to see
- **Group:** Data
- **What it is:** each user gets answers only from data they could already open. The quality bar allows no failures here.
- **Why it matters:** a leak of one client's data to the wrong banker is the most serious failure the product can have.
- **Set in:** 2.7
- **Built in:** 3.2
- **Proved in:** 3.7, 4.2, 4.3
- **Watched in:** 6.3
- **Tool (guess):** Snowflake access rules and Salesforce sharing rules
- **Proof:** a test where one user tries to see another user's clients and fails

### K5. A data contract
- **Group:** Data
- **What it is:** a written list of the exact fields the product may use, how fresh they must be and the quality checks they must pass, signed by the data owner.
- **Why it matters:** it stops the product quietly using data nobody approved.
- **Set in:** 2.3
- **Built in:** 3.2
- **Proved in:** 4.2
- **Watched in:** 3.2 (checks run on every data refresh)
- **Tool (guess):** Snowflake data checks
- **Proof:** the signed contract, and a comparison of the fields actually read with the fields in the contract

### K6. Sensitive data is hidden or labeled
- **Group:** Data
- **What it is:** sensitive fields are hidden ("masked") and sensitive files carry labels that limit who can open them.
- **Why it matters:** data about individuals, such as business owners and guarantors, is protected by law.
- **Set in:** 2.3, 2.4
- **Built in:** 3.2
- **Proved in:** 4.2
- **Watched in:** 6.3
- **Tool (guess):** Snowflake masking and Microsoft Purview labels
- **Proof:** a test showing a masked field stays hidden from a user without the right access

### K7. Every answer shows its source
- **Group:** Quality
- **What it is:** each number or claim links back to the record or document it came from.
- **Why it matters:** bankers can check the answer, and a made-up answer has nowhere to hide.
- **Set in:** 2.7
- **Built in:** 3.5
- **Proved in:** 3.7, 4.3
- **Watched in:** 6.3
- **Tool (guess):** source links on the Salesforce record
- **Proof:** the share of test answers that show a source, against the quality bar

### K8. Guardrails
- **Group:** Quality
- **What it is:** filters that block off-topic answers, harmful content and sensitive data such as account numbers.
- **Why it matters:** they catch what the instructions alone miss.
- **Set in:** 2.4
- **Built in:** 3.4
- **Proved in:** 4.3, 4.5
- **Watched in:** 6.3 (how often a guardrail blocks an answer)
- **Tool (guess):** Bedrock Guardrails and the Einstein Trust Layer
- **Proof:** the guardrail settings, and red-team results

### K9. A test set and a quality bar
- **Group:** Quality
- **What it is:** real examples with known good answers, run on every version and scored against agreed thresholds.
- **Why it matters:** it turns "it seems good" into evidence, and it catches a change that makes things worse.
- **Set in:** 2.7
- **Built in:** 3.6
- **Proved in:** 3.7, 4.3
- **Watched in:** 6.3
- **Tool (guess):** a test grader agent
- **Proof:** the test report for the version being released

### K10. Red-teaming
- **Group:** Quality
- **What it is:** trying on purpose to make the product reveal other users' data, give a credit decision or answer off-topic.
- **Why it matters:** reviewers want to see how it fails, not only how it works.
- **Set in:** 2.4
- **Built in:** 4.3
- **Proved in:** 4.3
- **Watched in:** 6.3
- **Tool (guess):** a red-team agent, with risk reviewing every failure
- **Proof:** the red-team report, with each failure fixed or accepted by risk

### K11. A fairness check
- **Group:** Quality
- **What it is:** a check that the product treats similar clients alike, reviewed by compliance.
- **Why it matters:** an AI that surfaces opportunities for some kinds of client and not others creates a fair-lending risk.
- **Set in:** 2.4
- **Built in:** 4.4
- **Proved in:** 4.4
- **Watched in:** 6.3 (run again each month after launch)
- **Tool (guess):** a fairness monitor agent
- **Proof:** the fairness report and compliance's response

### K12. An audit log
- **Group:** Records
- **What it is:** every action the AI takes is recorded: what it read, what it wrote and who approved it.
- **Why it matters:** risk and audit teams can reconstruct what happened after the fact.
- **Set in:** 2.4
- **Built in:** 3.4
- **Proved in:** 4.5
- **Watched in:** 4.8 (the monitoring plan says what is checked)
- **Tool (guess):** each platform's own activity log
- **Proof:** the log for a sample of actions

### K13. A risk rating and registration
- **Group:** Approvals
- **What it is:** the product goes through the bank's AI or model risk intake, gets a rating and is registered.
- **Why it matters:** the rating decides how much review is needed and how long approval takes.
- **Set in:** 2.4
- **Built in:** 2.4
- **Proved in:** 4.1
- **Watched in:** not covered in the playbook yet. The RM plan says the risk partner is told before a material change
- **Tool (guess):** the bank's intake form
- **Proof:** the confirmed rating and the registration record

### K14. Vendor reviews
- **Group:** Approvals
- **What it is:** each outside vendor the product relies on is on the bank's approved list for this use.
- **Why it matters:** regulators hold the bank responsible for what its vendors do with its data.
- **Set in:** 2.2
- **Built in:** 4.6
- **Proved in:** 4.6
- **Watched in:** not covered in the playbook yet
- **Tool (guess):** the bank's approved vendors list
- **Proof:** confirmation from vendor risk for each vendor

### K15. Sign-offs
- **Group:** Approvals
- **What it is:** risk, compliance, privacy and security each approve the release. Only a named partner can give a sign-off, and it is never automated.
- **Why it matters:** this is the formal approval. Everything before it is preparation.
- **Set in:** 1.0 (who decides is agreed at kick-off)
- **Built in:** 4.7
- **Proved in:** 4.7
- **Watched in:** 5.1
- **Tool (guess):** Power Automate approvals, or the bank's own system
- **Proof:** each sign-off recorded with a name and a date

### K16. Monitoring and an incident process
- **Group:** After launch
- **What it is:** a plan for what is watched after launch (quality, guardrail blocks, user overrides, incidents and fairness), and a tested way to pause the product and call the right people.
- **Why it matters:** AI quality can slip over time as data, models or instructions change. Approval is not the end of the control work.
- **Set in:** 4.8
- **Built in:** 4.8
- **Proved in:** 5.1
- **Watched in:** 5.6, 6.1, 6.3
- **Tool (guess):** Power BI, and a quality watchdog agent
- **Proof:** the monitoring plan, a dry run of the incident process and the incident log

_Last updated: 2026-10-09_
