# Playbook: the field manual under the product machine

Page 4 of the four "How we deliver" pages. The Product Workflow
shows the steps, the Product Framework
sets the rules, and the Product Machine
marks each task Auto, Draft, Me or Partner. This folder
says **how to do it the first time**, sub-step by sub-step, and what to watch so
the second time can be automated.

**Read it as a designed page:** https://claude.ai/artifact/YPEZ2F4Zp4bYUDmeQPzef4 (built from these files by `designs/playbook-build.py`; edit the .md files here, then rebuild and republish).

Use it while doing the work: open the step's file, work through each sub-step
in order, and fill in its **first-time log** as you go.

## The files
| Step | File | Status |
|---|---|---|
| 1. Discover | `1-discover.md` | In use, reviewed 2026-10-14 |
| 2. Define | `2-define.md` | In use, reviewed 2026-10-14 |
| 3. Build | `3-build.md` | In use, reviewed 2026-10-14 |
| 4. Govern and test | `4-govern-and-test.md` | In use, reviewed 2026-10-14 |
| 5. Release and adopt | `5-release-and-adopt.md` | In use, reviewed 2026-10-14 |
| 6. Measure and iterate | `6-measure-and-iterate.md` | In use, reviewed 2026-10-14 |
| Agent library | `agents.md` | 33 general agents (M1 to M33) plus my research helper H1; a short list closes the playbook page, and the full specs are on the Agent Library page |
| Controls | `controls.md` | 25 controls (K1 to K25); shown on the Controls Catalog page |

## How every sub-step is written
- **Goal:** what this sub-step is for, in one line.
- **Why it matters:** what goes wrong if it's skipped.
- **Know first:** the people, data and bank rules you need before starting.
- **First time, step by step:** the actual work, in order.
- **Output:** what it produces (a document, a number, a decision).
- **Done when:** how to tell it's finished.
- **Automation watch:** what to note while doing it, the agent it could become, the kind to use the first time and the kind to aim for (Auto, Draft or Me).
- **For the RM Assistant:** a short worked example from the first project. Where it cites the "memo" (a section, a step or Appendix A), that means the full RM plan, in RM Detail, Part 5.

## The first-time log (fill in for every sub-step)
This is what makes automation possible later: you can't automate work you
never wrote down.

| Field | What to write |
|---|---|
| Start and finish | The dates the sub-step started and finished |
| Time spent | Hours of real work, roughly |
| What I actually did | The real steps, including the ones not in the playbook |
| Inputs I needed | Data, documents, people |
| Where I waited | Who or what held it up, and for how long |
| What repeated | Anything I did more than once, or will do again next project |
| Wait index | Calendar days from start to finish, divided by hours of real work. A high number means waiting, not working |
| Cut first | Should it exist (and does it come from law, bank policy or our choice)? Delete it? Simplify it? Make it faster? |
| Then automate | For what's left: repeat? Stable? Safe alone? (yes or no each) |
| Agent idea | If all three are yes: what it would do, and Auto or Draft |

On later projects, keep a light version of this log for every sub-step (start and
finish, hours and waits), so the machine's measures can be counted every time.

## Rules that apply to every step
- **No client data in an AI tool the bank hasn't approved**, even for a quick test.
- **Guesses about the bank are marked ⚠️** until confirmed. Replace them with facts as I learn them, and note the source.
- **Numbers we don't have yet are [X].** Never invent them.
- **At the gate,** run the automation check from the Product Machine on every Me and Draft task (cut first, then automate), and update the step's table there.
- **Gates are decided in writing when they're clean:** if every criterion is met, the decider approves the gate pack in writing and the approval goes in the decision log; a meeting happens only when a criterion is contested or a decider asks for one. Partner sign-offs in step 4 don't change, and at the step 4 gate the risk partner and the sponsor approve the signed evidence pack (⚠️ the bank's approval policy may require a committee meeting).
- **Every sub-step is our choice** (ask the product manager to change it) unless the table below says it comes from law, a regulator or bank policy. A sub-step that sets, builds, proves or watches a law or bank-policy control inherits that control's source. Law and bank policy are never deleted by the automation check.

## Where the requirements come from
The sub-steps and gates that rest on law, a regulator or bank policy, including
every sub-step that sets, builds, proves or watches such a control. Everything
else in the playbook is our choice. Each control's own source is on its card in
the Controls Catalog. ⚠️ These are my reading of US rules for banks, to confirm
with the bank's risk partner at sub-step 2.4.

| Sub-step or gate | Comes from | To change it, ask |
|---|---|---|
| 1.0 Kick off the project | Inherits from the controls it sets, builds, proves or watches: K15 bank policy; K23 bank policy | Each control's owner (Controls Catalog) |
| 1.3 Interview and shadow users | Inherits from the controls it sets, builds, proves or watches: K24 law or regulator | Each control's owner (Controls Catalog) |
| 2.2 Choose the platform and delivery path | Inherits from the controls it sets, builds, proves or watches: K18 bank policy; K20 bank policy | Each control's owner (Controls Catalog) |
| 2.3 Data contract | Bank policy on data use ⚠️, resting on customer privacy law (the Gramm-Leach-Bliley Act) | The data owner |
| 2.4 Risk intake | Regulator: the model risk guidance (SR 11-7, with the OCC's matching Bulletin 2011-12, possibly replaced by SR 26-2: item W16 in the Open Items log), through the bank's model risk policy; also inherits K12 bank policy and K24 law or regulator (ask compliance) | Model risk |
| 2.7 Set the measures, quality bar and value model | Inherits from the controls it sets, builds, proves or watches: K4 bank policy; K9 law or regulator | Each control's owner (Controls Catalog) |
| 3.1 Design the solution and choose the AI capabilities | Inherits from the controls it sets, builds, proves or watches: K19 bank policy | Each control's owner (Controls Catalog) |
| 3.2 Prepare trusted data | Inherits from the controls it sets, builds, proves or watches: K4 bank policy; K6 bank policy | Each control's owner (Controls Catalog) |
| 3.3 Build the logic: simple rules first, AI explains | Inherits from the controls it sets, builds, proves or watches: K19 bank policy | Each control's owner (Controls Catalog) |
| 3.4 Build in the controls | Inherits each control's source (Controls Catalog) | Each control's owner |
| 3.6 Build the test set | Inherits from the controls it sets, builds, proves or watches: K9 law or regulator | Each control's owner (Controls Catalog) |
| 3.7 Test against the quality bar | Inherits from the controls it sets, builds, proves or watches: K4 bank policy; K9 law or regulator | Each control's owner (Controls Catalog) |
| 4.1 Risk rating and registration | Regulator: the model risk guidance, through the bank's model inventory | Model risk |
| 4.2 Data and privacy review | Bank policy ⚠️, and customer privacy law (the Gramm-Leach-Bliley Act) where individuals' data is involved | Privacy |
| 4.3 Testing evidence | Regulator: the model risk guidance expects testing; our quality bar sets the thresholds | Model risk |
| 4.4 Fairness check | Law: fair lending (the Equal Credit Opportunity Act) wherever similar clients could be treated differently ⚠️ (my reading for a tool that doesn't decide credit); always required on the higher-risk path (control K3), where drafts inform credit decisions | Compliance |
| 4.5 Confirm the controls work | Regulator and bank policy, through the controls it proves | Each control's owner (Controls Catalog) |
| 4.6 Vendor reviews | Regulator: the US banking regulators' third-party risk guidance (2023); also inherits K19 bank policy | Vendor risk; each control's owner (Controls Catalog) |
| 4.7 Sign-offs | Bank policy: its approval process for AI and models ⚠️; on the higher-risk path (control K3), also the bank's credit policy ⚠️ | Model risk, as owner of the bank's AI and model approval policy ⚠️ [name needed]; the credit policy owner for the higher-risk path |
| 4.8 Monitoring plan | Regulator: the model risk guidance expects ongoing monitoring | Model risk |
| 5.1 Confirm release readiness | Inherits from the controls it sets, builds, proves or watches: K15 bank policy; K16 law or regulator | Each control's owner (Controls Catalog) |
| 5.2 Launch the pilot, with a comparison group | Inherits from the controls it sets, builds, proves or watches: K18 bank policy | Each control's owner (Controls Catalog) |
| 5.6 Fix fast | Inherits from the controls it sets, builds, proves or watches: K16 law or regulator; K17 law or regulator | Each control's owner (Controls Catalog) |
| 6.1 Track the measures on a live dashboard | Inherits from the controls it sets, builds, proves or watches: K16 law or regulator | Each control's owner (Controls Catalog) |
| 6.3 Re-test after every change, and watch for drift | Inherits from the controls it sets, builds, proves or watches: K4 bank policy; K9 law or regulator; K13 law or regulator; K16 law or regulator; K17 law or regulator | Each control's owner (Controls Catalog) |
| Step 4 gate | Regulator and bank policy (the formal approval) | Model risk, as owner of the bank's AI and model approval policy ⚠️ [name needed] |
| The other five gates | Our choice | The product manager |

_Last updated: 2026-10-18_
