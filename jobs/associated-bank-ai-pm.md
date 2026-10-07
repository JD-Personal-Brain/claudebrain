# Job: Principal Applied AI Product Manager · Associated Bank

_Saved 2026-10-07 so I never have to paste it again._

## Quick facts
- **Company:** Associated Bank (Corporate and Commercial Banking)
- **Job ID:** JR106344
- **Apply:** https://associatedbank.wd1.myworkdayjobs.com/external_careers/job/Minneapolis-80-8th-43rd-Floor/Principal-Applied-AI-Product-Manager_JR106344/apply
- **Where:** Remote, hybrid or on-site. Offices in Minneapolis, Chicago, Omaha, Milwaukee and Green Bay.
- **Type:** Full time
- **Pay:** $103,670 to $177,720 base per year (as posted)
- **Status:** posted 30+ days ago (as of 2026-10-07)

## The job description (as posted)

Associated Bank is looking for a Principal Applied AI Product Manager to discover, build, and deliver AI-enabled products that improve revenue workflows, banker capacity, operating efficiency, and adoption across Corporate and Commercial Banking. In this hands-on role, you will work directly with frontline users, turn business problems into practical capabilities, and own assigned products from discovery through governed release and adoption.

Associated Bank requires you to directly represent yourself and your own experiences during the recruiting and hiring process. Associated Bank conducts a thorough background check on all new hires.

### Key Accountabilities
- Own assigned AI-enabled products from discovery through governed release, adoption, and continuous improvement.
- Work directly with bankers and business stakeholders to identify frontline needs and convert them into clear products with defined outcomes, delivery paths, governance requirements, and adoption measures.
- Translate complex business problems into user stories, acceptance criteria, backlog priorities, release scope, success measures, control requirements, and delivery tradeoffs.
- Lead complex assigned products with limited oversight, coordinating priorities, decisions, dependencies, testing, controls, release readiness, and issue resolution across cross-functional partners.
- Own governed product delivery, with risk, controls, data privacy, responsible AI, and regulatory expectations built in from the start, while engaging risk, compliance, data, and technology partners for review, guidance, and challenge.
- Define and monitor product usage, quality, business impact, adoption, and risk and control measures, and use the evidence to improve products over time.
- Configure and deliver practical AI capabilities, including agents, retrieval patterns, data flows, workflow automations, and system integrations that fit into the tools and workflows bankers already use.
- Align business, technology, data, risk, compliance, and operations partners around decisions and tradeoffs, while maintaining accountability for product delivery and governance and helping improve team practices.

### Education & Experience: Required
- Bachelor's degree in Business, Finance, Data Science, Computer Science, Analytics, Economics, or a related field; equivalent experience may be considered.
- 6+ years of product management, digital product delivery, AI, analytics, data products, workflow automation, or related experience.
- 6+ years of experience leading complex products, initiatives, or assigned product programs with limited oversight and measurable business outcomes.
- Advanced understanding of product management, AI-enabled workflow transformation, business process design, governed AI delivery, or data-enabled product delivery.
- 3+ years of experience influencing cross-functional stakeholders and driving adoption in a regulated environment while maintaining accountability for product delivery and governance.
- 6+ years of experience working with users and business stakeholders to define problems, prioritize work, manage delivery tradeoffs, build usable solutions, and drive measurable adoption.

### Education & Experience: Preferred
- Advanced degree, relevant certifications, or demonstrated experience in AI, analytics, automation, or digital product delivery.
- Familiarity with large language models, AI agents, AWS Bedrock, Snowflake, Microsoft Fabric, Power Platform, Microsoft 365 Copilot, Salesforce, or related technologies.
- 2+ years of experience in financial services, commercial banking, sales organizations, or client-facing business environments.
- Experience leading product adoption, change management, or workflow transformation initiatives.

### Why You'll Love Working Here (from the posting)
A collaborative team focused on building practical AI solutions that create real business value. You'll work closely with users, see your ideas deployed in production, and grow your expertise in AI, product management, and financial services.

### Benefits (from the posting)
401(k) and pension plans; paid volunteer time; diversity-focused Colleague Resource Groups; professional development; well-being programs, parental leave, employee stock purchase plan, military benefits; personal banking, loan, investment and insurance benefits.

### About the company (from the posting)
Serves 120+ communities in Wisconsin, Illinois, Minnesota and Missouri. Equal opportunity employer, Pay Transparency compliant, participates in E-Verify. Accommodations: leavesandaccommodations@associatedbank.com.

_Left out: the standard legal and compliance text (Bank Secrecy Act, Ethics Hotline, E-Verify poster links)._

---

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

## Next up
- Deep dive into each tech stack, one at a time.
