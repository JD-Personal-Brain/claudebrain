---
name: wrap-up
description: End a work session. Logs lessons, updates NOW.md, suggests improvements, saves to GitHub and opens a pull request. Use when the user says "wrap up", "let's finish" or similar.
---

# Wrap up a session

Keep every message short (see rule R2).

1. **Lessons.** Look back over the session for corrections or mistakes. Log each one with the **log-lesson** skill.
2. **Profile.** If you learned something new about how the user likes to work, add it to `me/profile.md`.
3. **NOW.md.** Update where things stand, what's next and any new agreements (each with its reason). Update the "Last updated" date.
4. **Improvements.** Add new ideas to `ideas.md`. Suggest 1 to 3 of them, each as one line: what it would let the user do, then "(yes/no)". Record each answer as the idea's status.
5. **Weekly review.** If "Last review" in NOW.md is 7 or more days ago, offer a 5-minute review: what's working, what's annoying and what to change. If they agree, do it and update "Last review."
6. **Ask before saving.** Ask once: "Save to GitHub and open a pull request? (y/n)". Only continue if the answer is yes.
7. **Save and open the pull request.** Commit with a clear message and push to the working branch. Open a pull request, or update the existing open one, with a plain-English summary:
   - What changed (3 to 5 bullets, no jargon)
   - Lessons learned
   - What to check
8. **Tell the user how to merge**, step by step: open the link → read the summary → click **Files changed** to look at the details if they want → go back to **Conversation** → click the green **Merge pull request** → click **Confirm merge**.
9. **Required length check (from L2b).** Before sending the final message, count its lines. It must be 5 lines or fewer: the link, one line on what's in it, the merge steps on one line, and anything I must act on. Cut everything else.
