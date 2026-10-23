# Prompting Handbook: how we write prompts, for any project

A memo for another Claude to read and follow. It packs our whole way of
prompting into one basic framework that any project using Claude can adopt.
Written 2026-10-23 from our Prompting
Guide (`prompting.md`), the write-prompt skill (`.claude/skills/write-prompt/`)
and what we learned building six prompts in our Prompt Library
(`prompt-library.md`).

## 0. How to use this memo
You are Claude, working with a person (called "the human" below) on a project.
This memo tells you four things: how we think about prompting, the structure
every prompt follows, how you and the human build a prompt together, and how a
finished prompt is saved in the project's prompt library so it can be reused
and improved.

- **Follow it whenever** the human asks you to write, fix or save a prompt, or
  asks for something reusable (an email routine, a summary, an analysis, a
  memo), even if they don't say the word "prompt".
- **Adapt the names, not the method.** Where this memo says `prompting.md` or
  `prompt-library.md`, use whatever files the project keeps (section 9 sets
  them up if there are none).
- **The human decides.** You explain, recommend and draft; the human approves.
  If they say no, don't find another way around it: ask what they'd prefer.

## 1. How we think about prompting
A prompt is a briefing for a capable colleague who knows nothing about the task
except what you write down. Everything below follows from that one idea.

**The golden rule** (Anthropic's words, from its prompting guide): "Show your
prompt to a colleague with minimal context on the task and ask them to follow
it. If they'd be confused, Claude will be too."

Five beliefs sit underneath the method:
1. **Clear beats clever.** Say exactly what you want: the length, the format,
   the limits, and what "done" looks like.
2. **Reasons beat rules.** A rule with a "because" is applied sensibly in cases
   the rule didn't foresee; a bare rule is applied blindly.
3. **Structure beats prose.** The same named pieces, in the same order, make
   prompts easy to write, review, compare and improve.
4. **Collaboration beats guessing.** The human holds context you don't have.
   Ask for it, one question at a time, instead of filling gaps with assumptions.
5. **Prompts are assets.** A prompt that worked once is saved, numbered and
   versioned, so the next run starts from the best version, not from memory.

## 2. Anthropic's advice, in plain English
These nine tips are our summary of Anthropic's official prompting guide, last
read on 2026-10-09. Anthropic updates the guide often, so re-check it now and
then:
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

1. **Be clear and direct.** Say exactly what you want: length, format, limits. Number the steps when order matters.
2. **Explain why.** Give the reason behind a rule, and Claude applies it more sensibly.
3. **Show examples.** 3 to 5 good ones that differ from each other.
4. **Use tags to separate parts**, like `<context>` and `<example>`. Any clear names work; keep them consistent.
5. **Give a role.** One sentence, like "You are a product manager at a software company."
6. **Long documents first, the question last.**
7. **Say what to do, not what not to do.** "Write in short paragraphs" beats "don't use bullets."
8. **Ask for extra effort out loud** if you want Claude to go above and beyond.
9. **Big jobs: draft, check, improve.** Write a draft, review it against the goal, then refine.

Anthropic does not publish a fixed list of prompt "pieces". The template in
section 3 is our own checklist, built on this advice. When a saved prompt cites
"tip 4", "tip 6" or "tip 9", it means the numbers above.

## 3. The framework: nine pieces
Use the pieces the task needs. **Goal, Context and Output matter most** and are
in every prompt; add the rest for big, risky or reusable tasks.

```
Role:     You are a ...
Goal:     I want ... Done means ...
Context:  Background, who it's for, and why it matters ...
Inputs:   The document, data or link to use ...
Steps:    1. ... 2. ... 3. ...
Rules:    Do ... Keep it under ... Because ...
Examples: Here's one I like: ...
Output:   Give me ... in this form: ...
Tone:     One main feel, said specifically: "friendly but direct" ...
```

| Piece | What it does | Get it right |
|---|---|---|
| **Role** | Sets the expertise and point of view | One sentence; name the field and the audience ("writing for its finance leaders") |
| **Goal** | Says what the answer is for | Always include "Done means ...": a test the human could apply to the answer |
| **Context** | Background the colleague would need | Who it's for, why it matters, what's already decided, any working assumptions stated as assumptions |
| **Inputs** | The material to work from | Wrap each in its own tag (`<notes>`, `<data>`); if Claude can read files itself, list the paths in tags instead of pasting |
| **Steps** | The order of work | Number them; make the last step "check the draft against the Goal, then improve it" (tip 9) |
| **Rules** | Limits and must-dos | Every rule ends with a reason ("because ..."); say what to do, not what to avoid (tip 7) |
| **Examples** | Shows the target | One short example of a good line or finding; 3 to 5 varied ones for repeated formats |
| **Output** | The exact shape of the answer | Sections in order, length, format (table, list, code block, page) |
| **Tone** | The feel | One main feel, said specifically: "confident but not salesy." Plain "professional" leaves Claude guessing. Skip it when tone doesn't matter |

**Order matters when there's long material.** If the prompt includes notes,
documents or data, put **Inputs first** and **Goal and Output last**, so Claude
reads everything before it sees the request (tip 6). Short prompts can run in
the template's order.

**Patterns we've found worth reusing** (from our six saved prompts):
- **Fill-in blanks:** reusable prompts mark the parts that change in
  `[square brackets]`, so a new run only touches those.
- **Honest placeholders:** use `[X]` for any number nobody knows yet, never an
  invented one, because readers check numbers and one made-up figure spoils
  trust in the rest.
- **Facts vs. assumptions:** tell Claude to mark anything only the client or
  organization knows (its people, data, policies) as "assumption, to confirm",
  with the question to ask.
- **Stages with a stop:** when a prompt would create a new structure or layout,
  split it into Stage 1 (a small sample) and Stage 2 (the full build), and tell
  Claude to stop for the human's yes between them.
- **A "for a different case" line:** under a reusable prompt, one line says
  which pieces to change to point it at a new case and that everything else
  stays.

## 4. The steps for creating a great prompt
Work through these in order. Steps 1 and 3 involve the human; section 5 says how.

1. **Find out what it's for.** You need three answers. Ask only for what the
   conversation hasn't already told you, and ask one question at a time:
   - **Goal:** what should the answer let them do? What does "done" look like?
   - **Inputs:** is there long material (notes, a document, data)? If yes, it
     goes first and the request last.
   - **Reuse:** a one-off, or a prompt they'll run again? Reusable ones get
     `[brackets]` and are offered for the library.
2. **Pick the pieces.** Goal, Context and Output always; Tone when the feel
   matters; Role, Inputs, Steps, Rules and Examples for big, risky or reusable
   prompts.
3. **Draft it with the template.** Fill each piece. Give every rule a reason.
   Wrap pasted material in tags. If you assume something, say so in one line so
   the human can correct it.
4. **Check it against the checklist** (section 6). Fix anything that fails
   before showing it.
5. **Hand it over.** Show the prompt in a code block, so it's easy to copy. Add
   one line on how to use it and one on how to ask for changes if the answer is
   off. If it will be reused, ask whether to save it to the library (yes/no).
6. **Watch for a better home.** If the same setup would be re-typed every
   time, say so once: it may belong in a saved file or a skill instead of a
   prompt.

## 5. Working with the human
Building a prompt is a short collaboration, not a questionnaire. The human
knows the situation; you know how to turn it into a prompt that works.

- **One question at a time, and only what's missing.** Never re-ask something
  the conversation already answers. A long list of questions feels like a form;
  one good question keeps things moving.
- **Explain, recommend, let them choose.** When there's a choice (a one-off or
  reusable prompt, one stage or two), give your recommendation with a one-line
  reason and let the human decide.
- **Show the pieces as you go.** If the human is learning, name the piece you're
  filling ("this is the Context: why it matters") so the framework becomes
  theirs, not only yours.
- **Keep your messages small.** Everything around the prompt stays short:
  about five lines and one question. The prompt itself can be as long as the
  job needs.
- **Don't fill gaps with guesses.** If something is unclear, ask. If you must
  assume to keep moving, say the assumption plainly so it can be corrected.
- **Use plain words.** Explain any technical term the first time you use it.
- **If they say no, stop.** Don't route around a "no"; ask what they'd prefer.

**When the answer is off, ask for changes; don't start over.** Never just say
"try again" or "make it better": that tells Claude nothing. Say what to keep and
what to change, one thing at a time, and teach the human to do the same:
1. **First draft:** use the full template and expect a solid start, not perfection.
2. **Change the direction:** "Keep the structure. Replace the generic points with three real examples."
3. **Polish:** "The intro is too long. Cut it to two sentences."

## 6. The checklist (run it before handing any prompt over)
- [ ] **Newcomer:** would a colleague with no context understand it? (the golden rule)
- [ ] **Done and format:** does it say what "done" looks like, and the output format?
- [ ] **Reasons:** does every rule have a reason?
- [ ] **Tone:** if the feel matters, is the tone specific (one main feel)?
- [ ] **Order:** if there's long material, is it first and the request last?

Show the result to the human in one line, for example:
"Checklist: newcomer ✅ done-and-format ✅ reasons ✅ tone ✅ order ✅".

## 7. Which model to use
Pick the smallest model that does the job well. The human usually chooses the
model when starting a session; at the start of a big or unusual task, say in
one line if a different model would suit it better.
1. **Small, fast jobs** (classifying, tagging, short summaries, bulk cleanup) → the smallest, fastest model.
2. **Everyday work** (drafting, cleanup, quick back-and-forth) → the mid-sized model.
3. **Real reasoning, or a mediocre answer won't do** (memos, plans, designed documents) → the most capable everyday model.
4. **The most capable model fell short on a hard, long-running problem** → the top model, if the plan includes it.

Model names and versions change often, so check the model picker for the
current ones rather than relying on names written here.

## 8. Saving to the prompt library
A prompt worth reusing goes into the project's **prompt library**, one file
(`prompt-library.md`) that holds every saved prompt. Never save without asking:
when a prompt is reusable, ask "Save it in the Prompt Library? (yes/no)".

**The library file has three parts:**
1. **How to use this page:** how to run a prompt (copy it into a new session,
   fill in the `[brackets]`, send it; or ask Claude for it by name), how to
   improve one, and how one gets added.
2. **The index table:** one row per prompt.
3. **One section per prompt**, in number order.

**The index table:**

| # | Prompt | What it gives me | Version |
|---|---|---|---|
| 1 | [short name] | [what the human gets from running it] | 1 ([date]) |

**Each prompt's section follows this layout:**

````
## Prompt [n]: [short name] ([what it's for])
**Version [v]** ([date]). [First run: ... / Say "run the ... prompt".]

[Two to five sentences: what the prompt does, why it's built the way it is,
and which tips it uses, such as "inputs first and the request last (tip 6)".]

```
[the prompt itself, in the nine-piece template]
```

**For a different [case]:** change [which pieces]. Everything else stays.

**What changed:** version 1, written [date]. Version 2 ([date]): [what changed and why].
````

**The rules that keep the library useful:**
- **Numbers never change.** A prompt keeps its number for life, so people and
  other files can refer to it ("Prompt 3").
- **Improving raises the version.** When a prompt is changed, update it in
  place, raise its version, update the index row and add one line to "What
  changed" saying what changed and why. Old wording isn't kept in the library;
  the project's version history (git, if it has one) holds it.
- **One home per prompt.** A prompt lives only in the library. Teaching
  examples (like those in section 10) live in the prompting guide; if one
  becomes worth reusing, move it into the library and remove it from the guide.
- **Save as you go.** Save the library file in the same session the human says
  yes, so an approved prompt never exists only in chat.

## 9. Setting this up in a new project
If the project has no prompting files yet, propose this setup to the human and
build it on their yes:
1. **`prompting.md`:** the prompting guide: sections 1 to 7 of this memo, plus the
   worked examples in section 10, adapted to the project's own work.
2. **`prompt-library.md`:** the library, starting with the "How to use this
   page" part and an empty index table (section 8).
3. **Make Claude read the guide every session:** in Claude Code, add
   `@prompting.md` to the project's `CLAUDE.md`, so every session loads it.
4. **Optional, a write-prompt routine:** in Claude Code, a skill
   (`.claude/skills/write-prompt/SKILL.md`) holding the steps in section 4, so
   the human can say "write a prompt for X" and get this method every time.

Before naming a file, check the project's existing conventions and use those.

## 10. Worked examples
Three teaching examples, from simple to full. Fill the `[brackets]` for your
project.

**Example 1: a basic prompt.** Six pieces; no Inputs or Steps, because there's
no document and no set order.

```
Role:     You are a product manager at [a software company].

Goal:     Write 5 questions I can ask [our customers] to find
          where they lose time each week. Done means I could use
          them in a 20-minute chat tomorrow.

Context:  I'm new to the team. [Customers] are busy and skeptical
          of new tools, so the questions should feel like a
          conversation, not a survey.

Rules:    Use plain, everyday words, because people tune out
          jargon. Keep each question to one sentence.

Example:  A question I like: "Walk me through what you did after
          your last [meeting with a client]."

Output:   A numbered list of 5 questions. Under each, one line on
          what it helps me learn.
```

**Example 2: the full framework.** Eight pieces. The notes come first and the
request (Goal and Output) last (tip 6); tags mark where the notes start and end
(tip 4); step 5 is "draft, check, improve" (tip 9).

```
Inputs:   <notes>
          [paste your interview notes here]
          </notes>

Role:     You are a product manager at [a software company].

Context:  The notes above are from my interview with [a customer]
          about where they lose time. My boss will use the summary
          to decide what we build first, so the problems need to be
          clear and ranked.

Steps:    1. Read the notes and list every time-wasting task
             mentioned.
          2. Group similar tasks together.
          3. Rank the groups by hours lost per week, biggest first.
          4. For the top 3, say whether a tool could realistically
             help.
          5. Check your draft against the Goal, then improve it.

Rules:    Use only what's in the notes, because my boss will act on
          this and made-up details would mislead them. If something
          is unclear, flag it instead of guessing. Use plain words.

Example:  A finding I like: "Status reports: about 3 hours a week
          copying updates into a slide. A tool could draft them
          from the project tracker."

Goal:     Using the notes above, write a 1-page findings summary for
          my boss. Done means they can read it in 2 minutes and see
          the top problems worth solving.

Output:   A heading, then the top 3 problems as short paragraphs,
          then one line: "Open questions to ask next time."
```

**Example 3: meeting notes into a follow-up email.** Ready to reuse. Notes
first, request last (tip 6). `[CHECK: ...]` marks anything unclear, so nothing
made up reaches the recipient.

```
Inputs:   <notes>
          [paste your meeting notes here]
          </notes>

Role:     You are an experienced [account manager] who writes
          clear, warm emails.

Context:  The notes above are from my meeting with [name, company]
          on [date]. The email goes from me to them, so it must be
          accurate and sound like a real person wrote it.

Steps:    1. Pull out what we discussed, what we agreed, and who
             owes what by when.
          2. Write the email.
          3. Check it against the notes and fix anything that
             doesn't match.

Rules:    Use only facts from the notes, because the recipient will
          take anything I send as a commitment. If something is
          unclear (a date, a number, who owns a task), put
          [CHECK: ...] in the email instead of guessing.
          Keep it under 200 words, because busy people skim.
          Use plain, friendly words and no jargon.

Goal:     Using the notes above, write a follow-up email I can send
          after a quick read. Done means the recipient knows exactly
          what happens next and who does it.

Output:   A subject line, then the email: a one-line thank-you,
          a short recap, a "Next steps" list (owner + date for each),
          and a closing line.

Tone:     Warm but businesslike.
```

## Sources
- Anthropic's prompting guide (the two links in section 2), read 2026-10-09; the tips in section 2 are our plain-English summary, not Anthropic's wording, except the golden rule, which is quoted.
- The Tone advice and "ask for changes, don't start over" come from the Claude Mastery course (an online course the human bought), noted 2026-10-09.
- Everything else (the nine-piece template, the steps, the checklist, the library layout and the reuse patterns) is our own method, built and used in this project's Prompting Guide, write-prompt skill and Prompt Library between 2026-10-09 and 2026-10-19.

_Last updated: 2026-10-23_
