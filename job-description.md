# Job description: Principal Applied AI Product Manager, Associated Bank

Saved 2026-10-07 from the posting I pasted. Requisition JR106344.
Benefits, equal-opportunity and legal boilerplate left out.

- **Locations:** Minneapolis, Chicago, Omaha, Milwaukee, Green Bay. Remote, hybrid or on-site.
- **Pay range (base):** $103,670 to $177,720 per year.

## The role in one line
Discover, build and deliver AI-enabled products that improve revenue workflows,
banker capacity, operating efficiency and adoption across Corporate and Commercial
Banking. Hands-on: work directly with frontline users and own products from
discovery through governed release and adoption.

## Key accountabilities
- Own assigned AI-enabled products from discovery through governed release, adoption and continuous improvement.
- Work directly with bankers and business stakeholders to find frontline needs and turn them into clear products with defined outcomes, delivery paths, governance requirements and adoption measures.
- Translate business problems into user stories, acceptance criteria, backlog priorities, release scope, success measures, control requirements and delivery tradeoffs.
- Lead complex products with limited oversight: priorities, decisions, dependencies, testing, controls, release readiness and issue resolution across partners.
- Own governed delivery, with risk, controls, data privacy, responsible AI and regulatory expectations built in from the start, engaging risk, compliance, data and technology partners.
- Define and monitor usage, quality, business impact, adoption, and risk and control measures; use the evidence to improve products.
- Configure and deliver practical AI capabilities (agents, retrieval patterns, data flows, workflow automations, system integrations) that fit the tools bankers already use.
- Align business, technology, data, risk, compliance and operations partners around decisions and tradeoffs.

## Required
- Bachelor's in Business, Finance, Data Science, CS, Analytics, Economics or related (or equivalent experience).
- 6+ years in product management, digital product delivery, AI, analytics, data products, workflow automation or related.
- 6+ years leading complex products with limited oversight and measurable outcomes.
- Advanced understanding of product management, AI-enabled workflow transformation, process design, governed AI or data-enabled delivery.
- 3+ years influencing cross-functional stakeholders and driving adoption in a regulated environment.
- 6+ years working with users to define problems, prioritize, manage tradeoffs, build usable solutions and drive adoption.

## Preferred
- Advanced degree, certifications or demonstrated experience in AI, analytics, automation or digital product delivery.
- Familiarity with LLMs, AI agents, AWS Bedrock, Snowflake, Microsoft Fabric, Power Platform, Microsoft 365 Copilot, Salesforce or similar.
- 2+ years in financial services, commercial banking, sales organizations or client-facing work.
- Experience leading adoption, change management or workflow transformation.

## About the bank (from the posting)
Serves more than 120 communities in Wisconsin, Illinois, Minnesota and Missouri.

## Tech stack summary (written by Claude, 2026-10-07)

> ⚠️ Written from Claude's memory (knowledge up to mid-2026). Product names and features change often. Verify on each vendor's site before an interview.

The posting says "familiarity," so the expectation is knowing what each tool can do and when to use it, not coding in it.

### AI building blocks
| Tech | What it is | Why it matters here | Core pieces you'd use |
|---|---|---|---|
| **Large language models (LLMs)** | The AI "brain" that reads and writes text (e.g. Claude, ChatGPT) | Every AI product you'd own uses one | Prompts, spotting made-up answers ("hallucinations"), testing answer quality before release |
| **AI agents** | An LLM that takes steps itself: looks things up, drafts, updates records | The job says "configure and deliver… agents" | What the agent may do, when a human must approve, logging its actions |
| **Retrieval patterns ("RAG")** | The AI looks things up in the bank's own documents before answering | Named in the job; cuts down on made-up answers | Choosing which documents it searches; people only see what they're allowed to |

### Where the AI runs
| Tech | What it is | Why it matters here | Core pieces you'd use |
|---|---|---|---|
| **AWS Bedrock** | Amazon's service for using AI models (Anthropic and others) inside the company's own Amazon cloud | Banks like that data stays in their controlled setup | Knowledge Bases (document lookup), Agents, Guardrails (blocking unsafe answers) |
| **Snowflake** | A cloud "data warehouse": one organized home for company data | Client and deal data likely lives here; AI needs it | Data access rules, hiding sensitive fields, built-in AI features ("Cortex", not certain what's current) |
| **Microsoft Fabric** | Microsoft's all-in-one data and reporting platform, includes Power BI | The job asks you to monitor usage and business impact | Power BI dashboards for adoption and results |

### Where bankers already work
| Tech | What it is | Why it matters here | Core pieces you'd use |
|---|---|---|---|
| **Microsoft 365 Copilot** | The AI assistant inside Outlook, Teams, Word, Excel | Fits "tools bankers already use" | Rollout and adoption, custom agents, respecting who can see which files |
| **Power Platform** | "Low-code" tools (build by clicking, not coding): Power Automate, Power Apps, Copilot Studio | Probably the most hands-on part: "workflow automations" and agents | Power Automate flows, Copilot Studio agents |
| **Salesforce** | A "CRM": where bankers track clients, deals and pipeline | "Revenue workflows" and "banker capacity" likely run through it | Einstein and Agentforce (its AI agents), connecting AI into banker workflows. Unknown which Salesforce products the bank uses |

### Running through all of it: governance
Banks must prove their AI is safe, fair and under control. Risk reviews, privacy checks, testing evidence and audit trails are built in from day one. Regulators call this "model risk management."

**Claude's recommendation:** go deepest on Power Platform, Copilot and Salesforce, where the hands-on work is.

