# How We Deliver Audit

**Scope:** the four "How we deliver" pages (Product Workflow, Product Framework, Product Machine, Product Playbook), the Reference pages built from them (Agent Library, Controls Catalog, Steps Catalog, Workflow Maps, Glossary, Tech Stack Guide) and how they line up with the Elon Mode. Relationship manager (RM) and portfolio manager (PM) work was left out on purpose: it's what we build next.

**How:** seven independent reviewers, each attacking one part (the Workflow and Framework, the Product Machine, playbook steps 1 to 3, steps 4 to 6, agents and controls, language and the reference pages), plus one that ran a made-up product ("a Teams assistant that answers bankers' questions about the bank's products") through all 44 sub-steps to find where the machine would stall. Four editors fixed what they found, and a fresh reviewer checked every fix.

## The verdict

- **The structure is sound.** All 44 sub-steps have every field, every agent name and kind matches across files, every gate's wording matches the Product Workflow, and the built pages were all up to date.
- **The pages disagreed on details that matter in real use:** who decides at each gate, what "proof" means at the Build gate, and whether a sponsor could waive the zero-tolerance permissions test. These are fixed.
- **Several things the pages promised had no task behind them**, such as the incident dry run (proof of a legally required control) and the guardrail test in step 4. These are fixed.
- **Six gaps remain that need your decision** before the RM and PM work. They are rules we never wrote, not mistakes, so I haven't invented them. They're listed below with my recommendation.

## What was found and fixed

About 110 findings: 8 Must fix, about 55 Should fix, the rest Minor. All are fixed except those that need your decision (next section).

| Page | What mattered most | Fixed |
|---|---|---|
| Product Workflow | Gate 3 said "every control has proof", but most controls are proved in step 4, so the gate could never pass. Now: "every control is built and passes its control test". Gate 5 said "results hit targets", but revenue takes months. Now: "leading results". | Yes |
| Product Framework | The "who decides" table didn't match the gates. It now names who joins the sponsor at each gate, adds Finance, IT, vendor risk and analytics, and says risk's step 4 approval can't be overruled. It now carries the Elon mode rules (cut first, gates in writing, limiting factor, machine measures) and says what can never be waived. | Yes |
| Product Machine | Missing tasks: incident dry run, compliance agreeing the fairness test, showing the controls to risk, acting on an alert, the incident log, the quarterly summary, recording the machine's measures. Two "Auto" rows hid a person's decision. Claims about where my time goes didn't match the tables. The page now reads every section from the working file, so it can't drift. | Yes |
| Product Playbook, steps 1 to 3 | The sponsor could accept a gap on permissions; the data contract never marked fields as sensitive, but Build masks "sensitive" fields; the baseline could be recorded before the measure was final; vendor reviews started only in step 4 (now in 2.2, because they're slow). | Yes |
| Product Playbook, steps 4 to 6 | Guardrails were never shown working; the monitoring plan came after the sign-offs that depend on it (now drafted alongside 4.5 and in the evidence pack); the step 4 no-go skipped re-testing; the monthly decision required a meeting (now in writing); "stop" had no steps (now it does). | Yes |
| Agent Library | Monitors didn't say what happens when data is missing, so a missing input could read as "all clear". Every agent now stops and alerts, and a monitor never reports a pass on missing data. An Auto agent ticked readiness items itself (now it marks them for me to confirm). | Yes |
| Controls Catalog | The customer privacy law (GLBA) was described as covering business owners and guarantors, which is uncertain; now marked ⚠️ for privacy to confirm. Several controls gained the sub-steps that now build or prove them. 13 of 25 controls still have a stage not covered in the playbook (item W6, unchanged). | Yes |
| Glossary and language | "Risk contact" and "risk partner" named one role; "risk and issue list" had three names; "automation check" meant two things. Each now has one name. New terms: risk and issue list, project file, automation review. | Yes |
| Tech Stack Guide | Heading named the wrong page; the model risk note now cites the OCC's matching guidance and the possible SR 26-2 replacement (item W17). | Yes |
| The checker | It now also catches plural forms of retired words, and fails if an agent's number and name differ between the Product Machine, the playbook and the Agent Library. | Yes |

**Left on purpose:** the RM plan still quotes the old wording of gates 3 and 5. It's out of scope today and gets aligned when we do the RM work.

## Decisions for you: gaps to close before the RM and PM work

Each is a rule the machine needs and doesn't have. My recommendation is in the last column.

| # | Gap | Why it matters for the RM and PM work | Label | My recommendation |
|---|---|---|---|---|
| 1 | **The unit of work.** Nothing says whether a gate is passed per project, per AI product or per feature wave. | The RM plan already runs gates per AI product and per feature wave in parallel; the PM plan will copy whatever we set. | **Needed** | One hierarchy: project (one per user group) → core use case → AI product → feature wave. Gates 1 and 2 per project the first time, then per feature wave (the quick pass); gates 3 and 4 per AI product, gate 5 per feature wave, gate 6 monthly per AI product and quarterly per project. |
| 2 | **Change after launch.** No rule says which changes go back through step 4. | RM pilots release every week or two; without a rule, each fix either breaks the approval or stalls. | **Needed** | A "material change" (new data, a new action, new users, a new or vendor-changed model) goes back through step 4; anything else is re-tested, logged and the risk partner told. ⚠️ The bank's model risk policy has the final word. |
| 3 | **The quick pass.** "A quick pass through Discover and Define" for the next feature wave is never defined. | RM waves 2 and 3 and every credit wave after the first come in this way. | **Needed** | A short checklist: which sub-steps are required (2.3 data contract update, 2.4 intake update, 2.5 stories, 2.7 measures), which reuse earlier work, and that gates 1 and 2 are decided in writing. |
| 4 | **The credit boundary.** Control K3 ("no credit decisions") would block the first PM product, credit memo drafts, which inform credit decisions. | Blocks the PM work as written. | **Needed before PM** | Restate K3 as "AI drafts or flags; a named credit officer decides", and add a higher-risk path in step 4 for products near credit decisions, set at 2.4. |
| 5 | **Products built on documents.** The data contract, data preparation and "simple rules first" assume data fields and rules. | Credit memos, financial statements and RM call notes are documents. | **Needed before PM** | A document variant in 2.3, 3.2 and 3.3: sources, content owner, re-indexing schedule, permissions per document and a check that every answer cites its source. |
| 6 | **From user workflow to AI products.** Discover doesn't start from the user workflow map, and nothing says how a map turns into candidate AI products. | Mapping the RM workflow (item W2) is the next job; its output has no defined way in. | **Needed** | Sub-steps 1.3 and 1.4 start from the user group's workflow map; the map's "where AI fits" list feeds 1.7's choice of target. |
| 7 | **Review depth by risk rating.** A low-risk internal tool goes through the same step 4 as a client-facing one. | Many RM admin products are low-risk; credit products are high-risk. | Optional | A lighter step 4 for low-risk products (fewer sign-offs, same tests), set by the rating in 2.4. Fits Elon mode. |
| 8 | **Four new controls:** hidden instructions in emails and documents (prompt injection), vendor model changes, how long logs are kept, and a periodic access review. | Any product that reads emails or call notes is exposed to the first. | Optional now, needed before the first build | Add them as K26 to K29 with "Comes from" lines. |
| 9 | **A fallback for each ⚠️ Auto task** if the bank says automations can't message people. | Otherwise the machine stalls waiting for that answer at the first project. | Optional | One line per ⚠️ row: what it becomes (usually Draft) if the answer is no. |

**Already planned, with what the audit adds:**
- **W3 templates:** add the outcome note, sizing table, measures sheet, value model, controls checklist, scale recommendation, monthly and quarterly packs, incident log, the sub-step log and a gate approval record.
- **W4 tracker design:** include the limiting factor, the date each gate pack was ready and the decision date (two machine measures depend on them).
- **W5 approvals map:** add credit officers and the credit policy owner when PM work starts.
- **W6 control gaps:** 13 of 25 controls still have a stage not covered.
- **W9 support model:** incident severity, who may pause, rollback and the handover to the long-term owner.

## Proof

- The audit checker: 0 problems after the fixes. It now also checks agent names across files, the gate wording on the Product Workflow page's step cards, and plural forms of retired words.
- The render check: every designed page renders fully, and all 330 jump links land on their sections.
- The nothing-lost check: about 130 sentences changed; all are rewordings from these fixes, except the Framework's "Starting a new project" list, cut on purpose because it repeated sub-step 1.0 (it now points there).
- A fresh second reviewer checked every fix and found about 25 follow-ons, all fixed, including one rule an editor had changed by mistake (which steps are capped when many projects run at once), now put back as I set it.
- 12 pages were republished after checking that none had newer live edits: Product Workflow, Product Framework, Product Machine, Product Playbook, Steps Catalog, Workflow Maps, Agent Library, Controls Catalog, Glossary, Tech Stack Guide, Elon Mode and the Document Library.

_Last updated: 2026-10-15_
