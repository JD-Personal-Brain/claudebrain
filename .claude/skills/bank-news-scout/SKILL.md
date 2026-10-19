---
name: bank-news-scout
description: Check public sources for new information about Associated Bank, keep only what changes the Bank Business Briefing, draft the edits on a draft branch and end with a summary the user receives by the scheduled task's email and phone notice. Runs on a schedule (a scheduled task starts a fresh session), and also when the user says "run the news scout", "any news on Associated?" or "check for bank updates".
---

# Bank news scout

Keeps the Bank Business Briefing (`memos/bank-business.md`, designed page
https://claude.ai/artifact/7ZVT7LtdqxwAma4UrBgTPX) current, so the user never
works from stale facts. It's the user's own research helper, not one of the product machine's
general agents: its spec is H1 in the agent library (`playbook/agents.md`, "my research helpers"),
and the briefing's section 11 says how it keeps the page current. Keep all three in line.

## The spec

| Field | What it is |
|---|---|
| **Name** | Bank news scout |
| **For** | The user (keeps their own briefing current) |
| **Kind** | Draft: it drafts the edits; the user decides what goes into main |
| **Job** | Find new public facts about Associated Bank that change the briefing, and draft the edits. |
| **Starts when** | Every Monday morning (scheduled task), on October 23, 2026 (the day after Q3 2026 results), or when the user asks |
| **Inputs** | `memos/bank-business.md` (its "As of" date, sections 1 to 9, the sources list in section 10 and section 11); `memos/bank-news-log.md` (what earlier runs already reported); public web pages |
| **Allowed actions** | Search the web and open public pages (if pages won't open because the workspace blocks them, work from search results, say so in the summary and label each item "from search results"); edit `memos/bank-business.md`, rebuild its designed page source and append to `memos/bank-news-log.md` on the session's draft branch; push that branch; end with **one** summary as the final message |
| **Not allowed** | Merge into main or open a pull request; republish the live designed page (that happens after the user's yes); send email with any connector (the summary reaches the user only through the scheduled task's notice); use non-public information; write a number without its period and source; fill a gap from memory |
| **Outputs** | Draft edits on the session's draft branch, one log entry, one summary |
| **Stops when** | The summary is written as the final message. Nothing new → still write a short "nothing new" summary, so the user knows it ran. A page won't open → say so in the summary and leave the gap |
| **Proof it worked** | The notice email in the user's personal inbox; the log entry; the draft branch with its diff (the startup check lists it as unmerged work in the next session) |
| **Person in charge** | The user |
| **Runs on** | A Claude Code scheduled task (fresh cloud session each time), with email and phone notices turned on and no connectors |

**How the summary reaches the user:** the scheduled task's own completion notice (email and phone), sent by claude.ai to the account's email, the user's personal email. Never use the Gmail connector or the work address: the user wants this work kept on their personal email only (decided 2026-10-14).

## 1. Read what we already know
- Open `memos/bank-business.md`: note its "As of" date, the latest quarter it covers and its sources.
- Open `memos/bank-news-log.md`: note the last run's date and what it already reported, so nothing is sent twice.

## 2. Search, in this order
Look for things dated after the last run. Also report anything older that the briefing doesn't mention yet and that changes it (the first build missed some leader news, for example).
1. SEC filings: new 8-K, 10-Q or 10-K (search `site:sec.gov Associated Banc-Corp`).
2. The bank's investor news: earnings releases, presentations, call dates (`investor.associatedbank.com`).
3. The bank's own newsroom and commercial pages.
4. Trade and local press: acquisitions, leaders, new markets, new products, AI announcements, regulatory actions.
5. The earnings call: a transcript if one opens, otherwise a summary, labeled as a summary.

## 3. Keep only what changes the briefing
For each find, ask: **which section of the briefing does it change, and how?** Keep it only if it
- replaces a number (new quarter, new totals, credit figures);
- answers or changes an item in section 9 ("To confirm inside the bank") or a ⚠️ guess;
- changes the strategy, leaders, markets, the American National integration or the bank's AI work (sections 4, 7 and 8);
- adds a risk (section 8).
Drop everything else: stock-price moves, analyst ratings, repeats of known facts and consumer-only news.
Rate each kept item **High** (changes a number or a decision in my plans), **Medium** (changes the picture) or **Low** (worth knowing).

## 4. Draft the edits
- Edit `memos/bank-business.md` in place, following the rules in Prompt 3 of `prompt-library.md`: every number with its period and a source tag, ⚠️ on my own conclusions, [X] where no public number exists, and plain English.
- Add each new source to section 10. Update the "As of" line and "_Last updated_".
- A new quarter's results replace the old figures throughout, so all numbers stay from one period. Say so in the summary.
- Rebuild the page source: `python3 designs/md-page-build.py`. Don't republish the live page.
- Append one entry to `memos/bank-news-log.md`: date, what was searched, each kept item (one line, rating, source) and anything that wouldn't open.
- Save a draft: commit and push to the session's draft branch.

## 5. Check before writing the summary
- Every number in the summary matches its source page.
- Nothing was reported in an earlier log entry.
- The draft branch is pushed and its name is in the summary.

## 6. Write the summary
End the session with one summary as the final message; the scheduled task's notice carries it to the user's personal email and phone.
- **First line:** `Bank news scout: [N] updates for the briefing ([date])`, or `Bank news scout: nothing new ([date])`.
- **Then,** in plain English, highest rating first:
  1. One line: what changed overall and whether anything needs the user's decision.
  2. One block per kept item: the rating, what's new, which briefing section it changes (old → new wording) and the source link.
  3. Pages that wouldn't open.
  4. Next step: "The edits are saved on draft branch `[branch]`. Say 'merge the news scout update' in a Claude session: Claude runs the audit skill (rule R18), shows what will be merged, and merges into main and republishes the page only after your yes."
- Keep it short enough to read in 2 minutes. Never put a guess forward as a fact.
