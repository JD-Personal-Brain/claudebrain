# Use Case Library

Where we think the value of AI is for each group of bankers we serve, and the outside research behind it. One section per group: relationship managers (RMs) and portfolio managers (PMs). Each core use case is one need an AI product can answer.

> ⚠️ **How much to trust the numbers.** They come from consultants, banks and vendors, mostly from their own client work, pilots and claims, not controlled studies. They show where the value is likely to be, not our targets: our targets come from the bank's own data. Check the original source before quoting any number to the bank.

## Relationship managers

**The need in one line:** RMs at many commercial banks spend only about 25–30% of their time with clients (McKinsey). Much of the rest goes to admin, weak leads and meeting prep. So the value is in two places: better opportunities, and the time to act on them.

| Core use case | Where the value is | Outside evidence (McKinsey unless noted) | Our AI product (wave) |
|---|---|---|---|
| **Prospecting and next best opportunities** | Finding the clients and prospects most likely to buy | About 30% pipeline growth and 10% higher revenue; one bank saw twice the conversion rate of traditional leads | Monday opportunity list (1); prospect lookalikes (2) |
| **Lead nurturing, including cross-sell** | More qualified leads and referrals between teams | Two to three times more qualified leads; 5% higher conversion (early pilots). Morgan Stanley: more than 100,000 successful AI-matched referrals to advisors (2024, its CFO; [The Daily Upside](https://www.thedailyupside.com/technology/artificial-intelligence/how-morgan-stanleys-ai-helped-close-100k-new-clients-this-year/), Oct 2024) | Referral prompts (2). Contacting prospects on its own: out on purpose |
| **Account intelligence and meeting prep** | Better meetings in less prep time | About 25% less prep time; 10% more time with clients. Bank of America's CTO: AI prep lets a banker cover about 50 clients instead of 15 in some cases (not audited; Reuters 2025, via [TechInformed](https://techinformed.com/?p=37424)) | Pre-meeting client brief (1); client Q&A (3) |
| **Deal scoring and pricing** | Better margins, faster approvals | 10% margin gains; one bank cut deal turnaround from five days to two | Out on purpose: the AI never sets or suggests a price (control K3, chosen to stay clear of fair-lending law) |
| **AI sales coaching** | Better calls; new RMs up to speed sooner | Customer satisfaction up seven points; new bankers up to speed 20% faster | AI sales coaching (3) |
| **Admin off the RM's plate** (our own) | Hours back for clients; better CRM data | Admin ranks first or second of bankers' problems at every stage of a sale (survey of 406 bankers and sales leaders, October 2025); it earns part of the 10–12 hours a week McKinsey expects back per banker, and about 40% better coverage | Meeting follow-up, with call notes into Salesforce (1) |
| **Keep clients** (our own) | Clients kept before they drift away | No outside figure; set from the bank's own retention data | Early warning (2) |

**The headline numbers.** Banks that rework one frontline area end to end see about 3–15% higher revenue per RM and 20–40% lower cost to serve. 53% of bankers cite a shortage of high-quality leads as their biggest barrier. McKinsey's warning: "Banks are moving fastest on the least valuable tools."

**What other banks are doing.**
- **BMO** (commercial banking): a "Next Best Offer" engine ranks leads and offers in the CRM, with the reason shown ([BMO AI](https://ai.bmo.com/?p=569)).
- **Morgan Stanley** (wealth): "Debrief", used with client consent, summarizes meetings, drafts the follow-up email and saves a note into Salesforce ([Morgan Stanley, June 2024](https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch)).
- **Banco do Brasil:** 12,000+ RMs get AI conversation summaries in one workspace ([NiCE case study](https://www.nice.com/resources/banco-do-brasils-bankers-stopped-working-yesterdays-data-and-let-ai-hand-them-todays), vendor, 2026).
- **JPMorgan** (wealth) and **CaixaBank** report AI tools for advisers and bankers; JPMorgan credits its tools with lifting sales in April 2025, without a figure.

The pattern: signals from data, shown inside the CRM, with the reason visible and the banker in control. Results against a comparison group are rare.

**Source:** McKinsey, "Agentic AI is here. Is your bank's frontline team ready?" (Kumar Kanagasabai, Chris Lu, Shital Chheda; [link](https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready)), based on a survey of about 400 US and Canadian bankers; checked against the article's text on 2026-10-10. ⚠️ Publication date not confirmed. Full exhibit data and every RM detail: [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n).

## Portfolio managers

**The need in one line:** PMs are, by our reading of the bank's job postings, its credit people paired with RMs (⚠️ to confirm). The value is in drafting credit memos and reviews and in monitoring credit quality, with a person always deciding. At DBS, credit memos and related work take up to 40% of its bankers' time (DBS's estimate); ⚠️ how much of a PM's time goes to them here is to confirm.

> ⚠️ **Our own pairing, to test with the credit lead.** Each RM core use case has a credit counterpart; the pairing is ours, and the PM plan uses it (reviewed 2026-10-19). Built from a web scan on 2026-10-13 through search summaries; the primary pages would not open.

| Core use case (credit counterpart) | Where the value is | Outside evidence | Strength | Our AI product (wave) |
|---|---|---|---|---|
| **Credit memo and annual review drafts** (account intelligence) | A review-ready first draft from many systems, with sources | DBS: live for about 1,500 bankers (August 2026), targets at least 30% less time. Moody's: writes about 35–40% of each memo at a tier-one US bank (Moody's investor remarks; bank not named). nCino, S&P and Microsoft all offer it | **Strongest** | Industry background draft (1); Borrower file (1); annual review and credit memo drafts (1) |
| **Early warning on credit quality** (keep clients) | Spotting a weakening borrower early | Nearly 60% of credit risk leaders are pursuing it, more than any other area (McKinsey survey of 24 institutions). Moody's live across 19 countries at a large Asian bank (Moody's earnings call) | **Strong** | Early warning flags (2) |
| **Spreading, document intake and covenant tracking** (admin) | Analyst hours back | Vendors claim 40–60% less analyst time per deal (vendor pages: multimodal.dev, V7 Labs). Evalueserve's covenant module is live at a Middle East commercial bank (vendor case study); nCino also sells these tools | Vendor claims | Covenant and statement tracker (2) |
| **Renewals and line changes** (lead nurturing) | Renewals caught on time; lines matched to results | Part of most memo tools (vendor material) | Thin | Renewal radar (3) |
| **Credit policy Q&A and coaching** (coaching) | Newer analysts up to speed faster | nCino Banking Advisor answers policy questions; American Banker reports AI helps newer bankers most | Thin | Credit policy Q&A (3) |
| **Deal screening** (prospecting) | Checking fit with credit appetite before the RM pitches | Vendor claims only | Thin | Deal screening (3) |
| **Risk rating support** (deal scoring) | Faster, consistent rationale | Little public evidence | Closest to a credit decision | Out on purpose (control K3) |

**What the market shows.** No bank reports letting AI make the credit decision: every example has the AI draft or flag and a person decide. We found no public announcement from a large US bank naming its own AI tool for commercial credit memos (search of 2026-10-13); Moody's reports one unnamed tier-one US bank using its agents.

**Order agreed 2026-10-15:** credit memo and annual review drafts first, early warning second, risk ratings out of the first waves. The full scan, with every source, is in PM Detail, Part 7.

_Last updated: 2026-10-19_
