# Prompting: how we write prompts

Claude loads this every session. Whenever Claude writes a prompt for me, or
helps me write one, it follows this page.

> ⚠️ **Source.** Based on Anthropic's official prompting guide, read on
> 2026-10-09. Anthropic updates it often, so re-check it at a weekly review now and then:
> - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
> - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
>
> Anthropic does not publish a fixed list of prompt "pieces". The template
> below is our own checklist, built on their advice.

## The golden rule (Anthropic's words)
> "Show your prompt to a colleague with minimal context on the task and ask
> them to follow it. If they'd be confused, Claude will be too."

## Anthropic's advice, in plain English
1. **Be clear and direct.** Say exactly what you want: length, format, limits. Number the steps when order matters.
2. **Explain why.** Give the reason behind a rule, and Claude applies it more sensibly.
3. **Show examples.** 3 to 5 good ones that differ from each other.
4. **Use tags to separate parts**, like `<context>` and `<example>`. Any clear names work; keep them consistent.
5. **Give a role.** One sentence, like "You are a product manager at a bank."
6. **Long documents first, the question last.**
7. **Say what to do, not what not to do.** "Write in short paragraphs" beats "don't use bullets."
8. **Ask for extra effort out loud** if you want Claude to go above and beyond.
9. **Big jobs: draft, check, improve.** Write a draft, review it against the goal, then refine.

## Fill-in-the-blanks template
Use the pieces you need. **Goal, Context and Output** matter most; add the rest for big or risky tasks.

**Long material (notes, documents, data)?** Put **Inputs first** and **Goal and Output last**, so Claude reads everything before it sees the request (tip 6). See Example 2.

```
Role:     You are a ...
Goal:     I want ... Done means ...
Context:  Background, who it's for, and why it matters ...
Inputs:   The document, data or link to use ...
Steps:    1. ... 2. ... 3. ...
Rules:    Do ... Keep it under ... Because ...
Examples: Here's one I like: ...
Output:   Give me ... in this form: ...
```

## Example 1: a basic prompt
Uses 6 pieces. No Inputs or Steps, because there's no document and no set order.

```
Role:     You are a product manager at a commercial bank.

Goal:     Write 5 questions I can ask commercial bankers to find
          where they lose time each week. Done means I could use
          them in a 20-minute chat tomorrow.

Context:  I'm new to the team. Bankers are busy and skeptical of
          new tools, so the questions should feel like a
          conversation, not a survey.

Rules:    Use plain, everyday words, because bankers will tune out
          jargon. Keep each question to one sentence.

Example:  A question I like: "Walk me through what you did after
          your last client meeting."

Output:   A numbered list of 5 questions. Under each, one line on
          what it helps me learn.
```

## Example 2: the full framework
Uses all 8 pieces. The notes come **first** and the request (Goal and Output)
comes **last**, so Claude reads the material before it sees what to do (tip 6).
The `<notes>` tags mark where the notes start and end (tip 4). Step 5 is
"draft, check, improve" (tip 9).

```
Inputs:   <notes>
          [paste your interview notes here]
          </notes>

Role:     You are a product manager at a commercial bank.

Context:  The notes above are from my interview with a commercial
          banker about where they lose time. My boss will use the
          summary to decide which AI tool we build first, so the
          problems need to be clear and ranked.

Steps:    1. Read the notes and list every time-wasting task
             mentioned.
          2. Group similar tasks together.
          3. Rank the groups by hours lost per week, biggest first.
          4. For the top 3, say whether AI could realistically help.
          5. Check your draft against the Goal, then improve it.

Rules:    Use only what's in the notes, because my boss will act on
          this and made-up details would mislead them. If something
          is unclear, flag it instead of guessing. Use plain words.

Example:  A finding I like: "Call notes: about 3 hours a week
          typing up meetings into Salesforce. AI could draft them
          from the meeting recording."

Goal:     Using the notes above, write a 1-page findings summary for
          my boss. Done means they can read it in 2 minutes and see
          the top problems worth solving.

Output:   A heading, then the top 3 problems as short paragraphs,
          then one line: "Open questions to ask next time."
```

## Our house style (from my profile and rules)
Add these to prompts written for me, when they fit:
- Plain English; explain any technical word.
- Ask me one question at a time.
- Say clearly what's a guess and what I should verify.

## Before using a prompt, check
- [ ] Would a newcomer understand it? (golden rule)
- [ ] Does it say what "done" looks like, and the output format?
- [ ] Does each rule have a reason?

_Last updated: 2026-10-09_
