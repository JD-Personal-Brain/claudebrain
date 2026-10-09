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
