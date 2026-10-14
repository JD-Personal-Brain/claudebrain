# Portfolio manager core use cases: what banks are deploying in commercial credit

As of 2026-10-13. A web scan of what banks are deploying in credit, lined up with the seven core use cases in the RM plan.

> ⚠️ **How much to trust this.** The web search worked, but the primary pages
> would not open from this session (mckinsey.com, federalreserve.gov and
> dbs.com were all blocked). Every fact below comes from search summaries of
> those pages, press coverage or vendor material. Vendor numbers are the
> vendor's own claims, not audited results. Check the original source before
> quoting any number to the bank.

## Summary
- **Credit memos are where banks are furthest along.** DBS rolled an agent that drafts credit memos out to about 1,500 bankers in August 2026, and Moody's says a tier-one US bank uses its agents to write about 35–40% of each memo.
- **Portfolio monitoring (early warning) is where most banks are working.** In McKinsey's survey of credit risk leaders, nearly 60% were pursuing it, more than any other area.
- **Nobody reports letting AI make the credit decision.** Every named example has the AI draft or flag, and a banker or credit officer decides and stays accountable.
- **All six credit processes we parked on 2026-10-09 show up in the market**, and each one lines up with one of the RM plan's seven core use cases (table below).
- **New regulatory guidance to check:** SR 26-2 (April 2026) reportedly replaces SR 11-7, the model risk guidance our files cite. Sources disagree on whether it covers generative AI.

## What banks and vendors have deployed

| Who | What | Status | Evidence quality |
|---|---|---|---|
| **DBS** (Singapore) | Agentic AI tool for relationship managers and credit risk managers. Specialised agents handle more than 70 tasks and pull from annual reports, industry research and internal records to produce a review-ready first draft of a credit memo for large and mid-sized corporate clients. Bankers can ask for more research and revise; they remain responsible for the final memo | Live: announced 19 August 2026, about 1,500 users after a 150-user pilot. DBS estimates credit memos and related work take up to 40% of an RM's time and targets a cut of at least 30% (a target, not a reported result) | Bank announcement, reported by several outlets; bank page itself not opened |
| **A tier-one US bank** (not named) | Moody's agents automate credit memo creation, generating roughly 35–40% of each memo | Deployed, per Moody's Q4 2025 prepared remarks | Vendor's investor remarks; bank not named |
| **A US bank** (not named) | Multi-agent credit memo workflow, reported as 30% faster credit turnaround and 20–60% analyst productivity | Pilot (2025), attributed to McKinsey | **Unconfirmed:** second-hand reports only; McKinsey's page would not open |
| **A top-three Southeast Asian bank** (not named) | Moody's AI early warning solution moved from proof of concept to production across 19 countries | Live, per Moody's earnings call | Vendor's earnings call, via a news summary |
| **A Middle East commercial bank** (not named) | Covenant module added to Evalueserve's spreading platform: the same spread data calculates covenants, and alerts flag breaches | Live | Vendor case study. Vendor reports 70% productivity gains and 99.6% data accuracy (a separate case) |
| **A bank** (not named), via **S&P Global** | Credit memos produced with AI on S&P data | Case study dated 29 May 2026 | Vendor case study |
| **Zions Bancorporation** (US regional) | Chose nCino to digitise commercial loan origination (not described as an AI project) | Selected April 2025 | Press coverage |
| **nCino** (loan platform many US banks use) | Banking Advisor: drafts deal and credit memo narratives, sorts uploaded documents to the right relationship, answers banker questions from uploaded credit policy. Also sells Automated Spreading | Generally available | Vendor press releases |
| **Microsoft** | "Speed credit memo generation" scenario: Copilot Studio agents gather documents, assess the loan and draft the memo from a template; M365 Copilot Chat summarises it for review | Published how-to scenario, not a bank result | Microsoft's own scenario library (search summary) |
| **Salesforce** | Agentforce for Financial Services (launched 21 May 2025): role-based agents in Financial Services Cloud, including a loan officer agent for consumer loans | Generally available; no commercial credit results found | Vendor launch material |

**Not found:** any public announcement from a large US bank (JPMorgan, Wells Fargo, Citi, PNC, U.S. Bank, Fifth Third, Huntington, Citizens, KeyBank, Truist, Regions, BMO) of an AI tool for commercial credit memos, reviews or covenants. Also not found: which loan platform Associated Bank uses. Both are worth asking about inside the bank.

## Industry figures (directional only)
- **Where credit teams are working (McKinsey, "Embracing generative AI in credit risk"; survey of senior credit risk executives at 24 institutions, including nine of the top ten US banks; publication date not confirmed):** portfolio monitoring nearly 60%; credit application processes just over 40%; controls and reporting just over 40%. Respondents see slightly more potential in wholesale (business) credit than retail. Use cases are "mostly narrow, noncustomer-facing."
- **IACPM and McKinsey study (March 2025 deck):** 44 institutions (33 interviewed in Q3 2024, 33 surveyed in December 2024). The use-case percentages are in the deck, which I couldn't open.
- **McKinsey, "The future is agentic: AI's role in the end-to-end corporate credit process" (12 December 2025):** agents can check data quality and consistency and run routine policy checks; the blockers to full automation are system compatibility, data quality and regulation. Deutsche Bank's chief risk officer is reported as calling its agentic work early but already useful (I could not confirm his exact words).
- **Credit memo time:** 20–60% less time, attributed to McKinsey by second-hand sources (unconfirmed). Backbase also cites 20–60% productivity for memo drafting, without saying whether it was measured.
- **Spreading and underwriting time:** vendors claim 40–60% less analyst time per deal and 50–75% shorter time to decision. Vendor claims only.
- **Early warning:** one vendor page claims 12–25% fewer non-performing loans; no primary source given. Treat as unsupported.
- **Budgets:** a 2026 Celent study, commissioned by Zest AI, found 83% of lenders plan to increase generative AI budgets this year.

## Portfolio manager core use cases: each RM core use case and its credit counterpart

The RM plan is organized on seven core use cases. Each has a natural credit
counterpart, often built on the same client data, so an RM AI product and a credit
AI product can share a data contract and agents. ⚠️ The pairing is my own
proposal, not something a source says.

| RM core use case | Credit counterpart (user: portfolio manager or credit analyst) | Parked credit process it covers | What the market shows |
|---|---|---|---|
| **1. Prospecting and next best opportunities** | **Deal screening:** a quick check that a prospect or new request fits the bank's credit appetite before the RM pitches | New (not on our list) | Thin: vendor claims only |
| **2. Lead nurturing, including cross-sell** | **Renewals and line changes:** flag loans coming up for renewal, and clients whose results suggest a bigger or smaller line | Renewals | Vendor material; part of most memo tools |
| **3. Account intelligence and meeting prep** | **Credit memo and annual review first drafts:** one client file pulled together from many systems, drafted in the bank's template, with sources | Credit memos and annual reviews | **Strongest:** DBS live at scale; Moody's at a tier-one US bank; nCino, S&P and Microsoft all offer it |
| **4. Deal scoring and pricing** | **Risk rating support:** AI drafts the rationale and checks it against policy; a person sets the rating | Risk ratings | Little public evidence; it is the closest to a credit decision, so fair-lending rules apply (the same reason pricing is out of the RM plan for now) |
| **5. AI sales coaching** | **Credit policy Q&A and coaching for analysts:** answers from the bank's credit policy, with the page cited | New (not on our list) | nCino Banking Advisor answers policy questions; American Banker reports AI helps newer bankers most |
| **Admin off the RM's plate** | **Spreading, document intake and covenant tracking:** read financial statements into the bank's spread, file documents, test covenants and chase compliance certificates | Spreading financial statements; covenant checks | Vendor case studies (Evalueserve, nCino); widely sold |
| **Keep clients** | **Early warning on credit quality:** signals that a borrower is weakening (late statements, falling deposits, news) | Early warning | McKinsey's most-pursued area (about 60%); Moody's live at a large Asian bank. Shares signals with the RM plan's "Early warning: client may leave" AI product |

**What this shows:** all six parked processes are covered, and two new ones
appear (deal screening, and policy Q&A and coaching). The evidence is strongest
for credit memos and early warning, and weakest for risk ratings and deal
screening.

## Regulatory note: SR 26-2
- **What sources say:** SR 26-2, revised interagency guidance on model risk management, was issued on 17 April 2026 by the Federal Reserve, OCC and FDIC. It reportedly supersedes SR 11-7 (and possibly SR 21-8; sources differ). The Fed's letter reportedly says it is most relevant to banks with over $30 billion in assets. Associated Bank had $51.8 billion at 30 June 2026 (Bank Business Briefing), so it would likely apply.
- **What's unclear:** sources disagree on whether it covers generative and agentic AI. Two (Lumenova, Enzai) say it excludes them; one (Openlayer) says it extends to them. The Fed's own text decides it; I couldn't open it.
- **What it touches in our files:** `tech-stack.md`, `playbook/4-govern-and-test.md`, `playbook/2-define.md` and the RM plan all cite SR 11-7. Not changed yet, because the scope question is open (item W18 in the Open Items log).

## What it means for the credit plan
**The RM structure carries over.** Each RM core use case has a credit
counterpart, so the credit plan can be built on the same seven lines, the same
six steps and the same agents.

**For decision (my recommendation, not yet agreed):**
1. **Start with credit memo and annual review drafts.** It has the strongest evidence, it reuses the RM plan's client brief data, and the person stays the decider.
2. **Put early warning second.** It's where most banks are working, and it shares signals with the RM plan's "Early warning: client may leave" AI product.
3. **Keep risk ratings out of the first waves**, for the same reason pricing is out of the RM plan.

## Sources
Opened through web search summaries on 2026-10-13; the pages themselves were not opened unless noted.
- DBS rollout: [Crowdfund Insider, Aug 2026](https://www.crowdfundinsider.com/2026/08/300467-dbs-rolls-out-agentic-ai-tools-to-1500-bankers-aiming-to-significantly-cut-credit-assessment-time/), [The Asian Banker](https://www.theasianbanker.com/press-releases/dbs-rolls-out-agentic-ai-tool-to-support-corporate-credit-assessment-process), [finews.asia](https://www.finews.asia/finance/45058-dbs-rolls-out-agentic-ai-to-1500-bankers), [DBS newsroom](https://www.dbs.com/newsroom/DBS_scales_agentic_AI_to_transform_way_of_working_for_corporate_bankers_freeing_up_time_for_more_strategic_client_engagements) (would not open)
- Moody's: [Q4 2025 prepared remarks](https://s203.q4cdn.com/694693571/files/doc_financials/2025/q4/4Q25-Prepared-Remarks-vFinal.pdf), [Q2 earnings call highlights](https://www.nasdaq.com/articles/moodys-q2-earnings-call-highlights), [Agentic Solutions](https://www.moodys.com/web/en/us/capabilities/gen-ai/agentic-solutions.html), [CRE early warning launch, Jul 2024](https://fintech.global/2024/07/16/moodys-launches-genai-powered-early-warning-system-for-cre-risk-management/)
- McKinsey: [Embracing generative AI in credit risk](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/embracing-generative-ai-in-credit-risk), [The future is agentic (Dec 2025)](https://www.mckinsey.com/industries/financial-services/our-insights/the-future-is-agentic-ais-role-in-the-end-to-end-corporate-credit-process), [IACPM–McKinsey deck (Mar 2025)](https://iacpm.org/wp-content/uploads/2025/03/IACPM-McKinsey-Gen-AI-Webinar-2025.pdf), [Digital Commerce 360 on McKinsey's agent research](https://www.digitalcommerce360.com/2025/07/28/mckinsey-ai-agents-enterprise-value/amp/)
- nCino: [Banking Advisor (Nasdaq press release)](https://www.nasdaq.com/press-release/ncino-deploying-banking-advisor-generative-ai-solution-drive-new-efficiencies), [Data, AI and analytics](https://www.ncino.com/solutions/data-ai-analytics), [Zions selects nCino](https://www.crowdfundinsider.com/2025/04/238581-intelligent-banking-solutions-provider-ncino-selected-by-zions-bancorporation-to-digitally-transform-loan-orginations/)
- S&P Global: [case study, 29 May 2026](https://www.spglobal.com/market-intelligence/en/news-insights/case-studies/a-bank-uses-ai-backed-by-trusted-data-to-quickly-and-reliably-produce-credit-memos)
- Microsoft: [Speed credit memo generation scenario](https://adoption.microsoft.com/en-us/scenario-library/financial-services/speed-credit-memo-generation/)
- Salesforce: [Agentforce for Financial Services launch](https://smallbiztrends.com/salesforce-agentforce-financial-services-ai-launch/)
- Evalueserve: [covenant monitoring case study](https://www.evalueserve.com/case-study/global-bank-automates-covenant-monitoring-using-ai/)
- Backbase: [AI in commercial banking](https://www.backbase.com/blog/ai-in-commercial-banking)
- Vendor claims on spreading, underwriting and early warning: [multimodal.dev](https://www.multimodal.dev/agentic-workflows/commercial-lending-ai), [V7 Labs](https://www.v7labs.com/blog/ai-commercial-loan-underwriting)
- Lending budgets (Celent for Zest AI): [AI in lending statistics](https://www.sci-tech-today.com/stats/ai-in-lending-statistics/)
- American Banker: [How generative AI gives novice bankers a boost](https://www.americanbanker.com/news/at-banks-generative-ai-helps-novices-not-skilled-workers)
- SR 26-2: [Baker Tilly](https://www.bakertilly.com/insights/updated-interagency-guidance-on-model-risk-management), [Lumenova](https://www.lumenova.ai/blog/sr-26-2-model-risk-management-banking/), [Enzai](https://www.enz.ai/glossary/sr-26-2), [Openlayer](https://www.openlayer.com/blog/post/sr-26-2-mrm-guide-ai-teams), [Fed letter](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) (would not open)

_Last updated: 2026-10-13_
