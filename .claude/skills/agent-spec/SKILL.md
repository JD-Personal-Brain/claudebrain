---
name: agent-spec
description: Turn an agent idea into a full, buildable spec. Use when the user says "spec this agent", "write the agent spec", "turn the agent ideas into specs", when a playbook review table or project memo lists an agent marked "New" or "Partly", or at playbook sub-step 3.1 (design the solution). Works for delivery-machine agents (the agent library) and for a project's own agents (the project memo's Appendix A).
---

# Write an agent spec

Every agent gets the same spec, so any of them can be built, tested and
approved the same way. It follows the AI principles in `product-framework.md`:
assistive first, one job each, read-only by default, every action logged.

## 1. Decide where it goes
- **Runs the delivery machine on any project** (it helps the team do the work): the **agent library**, `playbook/agents.md`, numbered M1, M2 and so on.
- **Part of one project's product, or only useful to that project:** that project memo's **Appendix A**, numbered A1, A2 and so on.

## 2. Fill in every field
| Field | What to write |
|---|---|
| **Name and number** | A plain name that says what it does |
| **Used in** | The playbook sub-step(s) where it runs |
| **For** | The team (helps do the work) or users (part of the product) |
| **Kind** | First time → aim for (Auto, Draft or Me), matching the playbook review table |
| **Job** | One sentence: the one job it does |
| **Starts when** | What triggers it: a request, a date or an event |
| **Inputs** | Exactly what it reads, and where that lives |
| **Allowed actions** | A short list. Read-only or draft-only unless a named person approves; an Auto agent acts only within this list, and waits (⚠️) until the bank allows it |
| **Not allowed** | What it must never do (for example, contact clients, decide credit, approve a sign-off) |
| **Outputs** | What it produces, and where it's saved or sent |
| **Stops when** | When it's finished, and what it does if something's missing |
| **Proof it worked** | How a person checks a run: a log, a sample checked by hand, a test |
| **Person in charge** | Who reviews its work and owns its quality |
| **Runs on (guess)** | The tool from `tech-stack.md` most likely to run it, marked as a guess |
| **To confirm** | Open questions about the bank, marked ⚠️ |

## 3. Check it
1. **One job:** if the Job sentence needs "and", split it into two agents.
2. **Safe:** nothing reaches a client, changes a record or decides credit without a person's click. Sign-offs are never automated.
3. **Matches its sub-step:** its Kind matches the playbook review table and the Delivery Machine task table (`delivery-machine.md`), and its inputs exist by then (no circles).
4. **Provable:** "Proof it worked" can actually be checked by a person.
5. **No invented facts:** unknown numbers are [X], bank guesses are ⚠️.

## 4. Update the references
- In the playbook review table, change "Already specified?" from "New" to "Yes, M#" (or "Yes, A#").
- If the agent changes how a task is done, update that task row's tool in `delivery-machine.md`.
- Rebuild and republish the designed pages: the playbook page (`python3 designs/playbook-build.py`; it shows the delivery-machine agents) and the Agent Library (`python3 designs/agents-build.py`). For a project agent in a memo's Appendix A, also update that project's design page first, then rebuild its scrolling page. Then run `python3 .claude/skills/audit/check.py`.

## 5. Audit, then merge
Run the **audit** skill (rule R18) before offering to merge.
