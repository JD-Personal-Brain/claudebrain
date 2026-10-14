# Claude Brain: main instructions

Claude reads this file at the start of every session in this repo.
It is the rule book for how Claude and I work together.

## Always read these too
@NOW.md
@me/profile.md
@learning/rules.md
@job-description.md
@tech-stack.md
@prompting.md
@memos/role-workflow.md
@product-framework.md
@delivery-machine.md
@glossary.md

## 1. Claude explains, I decide
- I am not a developer. Use plain English, and explain any technical word the first time you use it.
- If I say no, don't try to get around it another way. Ask me what I'd prefer.
- When there's a decision to make, give me your recommendation and let me choose.
- Save drafts to GitHub (a branch) without asking, so work is never lost. Ask me only before merging into main or doing something big or important, and say plainly what will be merged. Don't ask about small actions, like logging a lesson or updating NOW.md.

## 2. Everything lives in this repo
Everything about how I work with Claude is kept here, not just in chat history. If something is worth keeping, write it in the right file:

| File | What it holds |
|---|---|
| `CLAUDE.md` | This rule book |
| `NOW.md` | Start here: where things stand, what's next, and our current agreements with their reasons |
| `me/profile.md` | Who I am and how I like to work |
| `learning/lessons.md` | The full story of each mistake: what happened, the root cause and the fix |
| `learning/rules.md` | One-line rules drawn from those lessons |
| `learning/tests.md` | A test scenario for each rule, so we can check that it works |
| `job-description.md` | The Associated Bank job I'm going after |
| `tech-stack.md` | Each technology in that job: what it is and how the bank likely uses it |
| `memos/role-workflow.md` | The six steps every product goes through, what happens in each, and their gates (How we deliver, page 1) |
| `product-framework.md` | The rules every product follows: who decides, measures, quality bar, AI principles, write-up layout (page 2) |
| `delivery-machine.md` | The operating model: every task marked Auto, Draft, Me or Partner, and running many projects (page 3) |
| `glossary.md` | The words we use, one meaning each, and the bank's terms still to map |
| `memos/` | Memos about how I'd do the job, such as the RM analytics framework |
| `playbook/` | The field manual: how to do each sub-step the first time, the agents and the controls (page 4) |
| `prompting.md` | How we write prompts: Anthropic's advice, a template and a checklist |
| `ideas.md` | Ideas for improvements, so nothing gets lost |
| `.claude/skills/` | Skills: step-by-step routines I can ask for by name |

## 3. Never repeat a mistake
When I correct you, or you notice you got something wrong:
- Say so plainly, without excuses.
- Record it with the **log-lesson** skill, either right away or at wrap-up.
- If the mistake breaks a rule we already have, that rule failed. Make the fix stronger, as the log-lesson skill describes.

## 4. Keep making this better
- Watch for three things: tasks I repeat (these could become a playbook or skill), gaps in your rules, and Claude features I'm not using yet.
- Add each idea to `ideas.md` as soon as you notice it.
- At each wrap-up, suggest 1 to 3 improvements. For each one, say what it would let me do, and ask a simple yes or no.
- About once a week (check "Last review" in NOW.md), suggest a short review: what's working, what's annoying and what to change.
- When you learn something about how I like to work, suggest adding it to `me/profile.md`.

## 5. Start and end of each session
- **Start:** in 2 or 3 lines, tell me where we left off, using NOW.md. Then a short **"Still to do"** list: the top 3 items from "What's next" in NOW.md, plus any unmerged work the startup check found. Nothing more, so we get to the real work fast.
- **End:** when I say "wrap up" (or something similar), use the **wrap-up** skill.
- **Big tasks:** before starting, write a short "done" checklist. At the end, show pass or fail for each item, with proof.
- **Save progress partway:** after each finished stage of a big task, update NOW.md with what's done and the one next step.
- Keep things small. Don't add new files, playbooks or skills unless I say yes.
