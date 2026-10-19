# Tech stack: Associated Bank, Principal Applied AI Product Manager

The technologies in `job-description.md`: what each one is, how the bank most
likely uses it, and what I need to know to do the job. Update it as I learn how the bank actually works.

> ⚠️ **How much to trust this.** Written on 2026-10-07 from general industry
> knowledge (to mid-2026), not from Associated Bank. Lines marked
> **(guess)** are educated guesses about the bank. Lines marked **(verify)** are
> facts that may have changed: these vendors rename products often. Replace
> guesses with facts as I learn them, and note the source.
>
> **Working assumption (decided 2026-10-07, confirmed 2026-10-09):** every tool
> named in the job description is live at the bank today and available to us.
> Source: confirmed by the bank (2026-10-09). Plan with them as real tools. "(verify)" now
> only flags product details such as names, features and pricing.

## The big picture: how it fits together

```
 Bankers work in ──►  Outlook · Teams · Salesforce (client and deal records)
                              ▲
 AI shows up there via ──►  M365 Copilot · Copilot Studio agents · Salesforce Agentforce
                              ▲
 Workflows and glue ──►  Power Automate · system integrations (APIs)
                              ▲
 AI models run in ──►  AWS Bedrock (and the AI inside Microsoft and Salesforce)
                              ▲
 Data lives in ──►  Snowflake · Microsoft Fabric (reporting via Power BI)
                              ▲
 Wrapped around all of it ──►  Governance: risk, compliance, privacy, responsible AI
```

**The job in one line:** find where bankers lose time or miss revenue, then
pick the right layer above to fix it, without breaking the bank's rules.

**A rule of thumb for choosing (guess):**
- Bankers need help inside email, documents or meetings → **M365 Copilot**.
- The work happens on client or deal records → **Salesforce** (Agentforce).
- It's a repeatable "when X happens, do Y" process → **Power Automate**.
- It needs a custom agent or chat assistant for a team → **Copilot Studio**.
- It needs heavier, custom AI or bank data at scale → **AWS Bedrock + Snowflake**.
- It's about proving usage and impact → **Power BI / Fabric**.

---

## By the six steps (Product Workflow)

The same technologies, sorted by the six steps I'll use in this job.
**Status key:** 🟡 named in the posting; confirmed live by the bank (2026-10-09; see the working assumption above), but product details are unconfirmed ·
🟢 applies to US banks in general (still check for updates).

| Step | What I have | Status |
|---|---|---|
| **Discover** | **Salesforce** pipeline and activity data (where bankers lose time or miss sales). **M365 Copilot / Viva Insights** usage reports (where time goes in email and meetings). **Snowflake / Power BI** for baseline numbers before anything changes. | 🟡 |
| **Define** | **LLM basics**: what AI does well, and its biggest risk, hallucination. The **"pick the layer"** rule of thumb above. **Data checks early**: what's trusted in Snowflake, and which Power Platform connectors IT allows (DLP rules). | 🟡 |
| **Build** | **Where bankers work:** M365 Copilot, Copilot Studio agents, Power Automate, Power Apps, Salesforce Agentforce / Prompt Builder / Flow. **Behind the scenes:** AWS Bedrock (Knowledge Bases, Agents), Snowflake Cortex, retrieval (RAG) with citations, APIs. | 🟡 |
| **Govern and test** | **Rules:** SR 11-7, NIST AI RMF, GLBA, ECOA, third-party risk. **Controls:** Bedrock Guardrails, Einstein Trust Layer, Snowflake masking (Horizon), Microsoft Purview labels. **Testing:** evals, red-teaming, a human approving actions, audit logs. | 🟢 rules · 🟡 tools |
| **Release and adopt** | Publish where bankers already work (Teams, Outlook, Salesforce). Power Platform environments move a tool from test to live. Start "assistive" (AI suggests, a person decides). Copilot licenses are paid per user, so leaders watch usage. | 🟡 |
| **Measure and iterate** | **Power BI / Fabric** dashboards (adoption, hours saved, pipeline impact). **Salesforce** for business results. **Copilot usage dashboard.** Re-run evals after every change; watch guardrail blocks, human overrides and drift. | 🟡 |

**Biggest unknown in every row:** how each tool is set up at the bank (which features, licenses and connections). All of them are live, confirmed by the bank (2026-10-09).

---

## Part 1: Core AI concepts

### Large language models (LLMs)
- **What it is:** the AI "brain" that reads and writes text, such as Claude (Anthropic), GPT (OpenAI), Llama (Meta) and Amazon's Nova models.
- **How the bank likely uses it (guess):** summarizing client meetings and documents, drafting emails and credit memos, answering policy questions, and pulling key facts out of financial statements.
- **What I need to know:**
  - **Prompts:** the instructions given to the model. Good prompts make a big difference.
  - **Hallucination:** the model confidently makes things up. In a bank this is the #1 risk, which is why answers should point back to a source document.
  - **Context window:** how much text the model can read at once.
  - **Evaluation ("evals"):** a set of test questions with known good answers, run before every release to prove quality.
  - **Cost and speed:** bigger models are smarter but slower and more expensive. Pick the smallest one that does the job well.
- **Risk angle:** the bank will likely treat each AI use as a "model" that needs review (see Governance).

### AI agents
- **What it is:** an LLM that can take actions, not just answer. It can look things up, use tools, fill in forms and update records, often in several steps.
- **How the bank likely uses it (guess):** meeting prep ("brief me on this client before my 2pm"), drafting follow-ups after calls, logging activity in Salesforce, and routing requests to the right team.
- **What I need to know:**
  - **Tools/actions:** the specific things an agent is allowed to do. Keep the list short.
  - **Human in the loop:** a person approves before anything goes to a client or changes a record. This is the norm in banking.
  - **Autonomous vs. assistive:** assistive agents suggest and a human acts; autonomous agents act on their own. Expect the bank to start with assistive ones.
  - **Audit trail:** every action logged, so risk and audit teams can review it.
- **Risk angle:** the more an agent can *do*, the more review it needs.

### Retrieval patterns (RAG, "retrieval-augmented generation")
- **What it is:** before answering, the AI searches the bank's own documents and uses what it finds, so answers are based on real sources rather than memory.
- **How the bank likely uses it (guess):** "Ask the policy manual" assistants, product and pricing Q&A for bankers, and searching past deal files.
- **What I need to know:**
  - **Knowledge sources:** which documents the AI can search. Quality in means quality out, so outdated policies give wrong answers.
  - **Citations:** answers should link to the source, so bankers can check them.
  - **Permissions:** a banker should only get answers from documents they're already allowed to see.
  - **Freshness:** how often documents are re-indexed (re-read) when they change.
- **Risk angle:** a leak of confidential data through search results is a major concern.

### Data flows and system integrations
- **What it is:** how data moves between systems. An **API** is a standard doorway that lets one system ask another for data or tell it to do something.
- **How the bank likely uses it (guess):** connecting Salesforce, Snowflake, the loan system and Microsoft 365, so an agent can pull a full client picture.
- **What I need to know:** where each piece of data comes from, who owns it, how fresh it is and whether it may be used for AI. Integrations are usually the slowest part of delivery, so plan for them early.

---

## Part 2: Where the AI and data run

### AWS Bedrock (Amazon Web Services)
- **What it is:** Amazon's service for using AI models from several companies (including Anthropic, Meta, Mistral and Amazon) inside a company's own AWS cloud account.
- **Key parts (verify):**
  - **Knowledge Bases:** ready-made RAG (document search plus answers).
  - **Agents / AgentCore:** tools for building and running AI agents.
  - **Guardrails:** filters that block harmful content, off-topic answers or sensitive data such as account numbers.
  - **Model evaluation:** compare models on your own test questions.
- **How the bank likely uses it (guess):** the "engine room" for custom AI products the off-the-shelf tools can't handle, such as document-heavy work (financial statements, credit files) or AI built into internal apps.
- **Why banks like it:** data stays inside the bank's own cloud setup, and AWS says customer data isn't used to train the models **(verify current terms)**.
- **What I need to know:** which models are approved for use, what Guardrails are required, and cost per use. Engineers build here; the product manager defines the requirements and quality bar.

### Snowflake
- **What it is:** a cloud "data warehouse": one large, organized home for a company's data that many teams can query (ask questions of).
- **Key parts (verify):**
  - **Cortex AI:** AI features built into Snowflake, including AI functions that run on data, **Cortex Search** (RAG over data) and **Cortex Analyst** (ask questions in plain English and get answers from tables).
  - **Governance (Horizon):** access rules, hiding sensitive fields ("masking") and tracking where data came from.
  - **Data sharing:** links with other systems, such as Salesforce, without copying data.
- **How the bank likely uses it (guess):** home for client, account, deal and product data used in analytics. It feeds AI products with facts like "this client's balances and products."
- **What I need to know:** which data is there and trusted ("certified"), who owns it, and what approvals are needed to use it in AI. Also the "data contract" for each product: which fields, how fresh, and which quality checks.

### Microsoft Fabric
- **What it is:** Microsoft's all-in-one data and analytics platform. It combines data storage (**OneLake**), data pipelines, data warehousing and **Power BI** dashboards.
- **How the bank likely uses it (guess):** reporting and dashboards for business leaders, and possibly a second data platform alongside Snowflake. It may copy ("mirror") data from Snowflake **(verify)**.
- **What I need to know:**
  - **Power BI** is the part I'll touch most: dashboards for adoption, usage, time saved and revenue impact.
  - Know which platform holds which data, so I don't promise a feature using data that isn't there.
- **Open question:** why the bank has both Snowflake and Fabric. Ask early.

---

## Part 3: Where bankers already work

### Microsoft 365 Copilot
- **What it is:** the AI assistant inside Outlook, Teams, Word, Excel and PowerPoint. It uses the user's own emails, files, chats and meetings (through "Microsoft Graph") and respects their existing permissions.
- **How the bank likely uses it (guess):** meeting summaries and action items in Teams, drafting client emails, summarizing long email threads, and building first drafts of documents.
- **What I need to know:**
  - **Adoption is the hard part.** Licenses are paid per user (roughly $30 per user per month, Microsoft's announced price at launch, 2023; **verify**), so leaders will ask whether people actually use it.
  - **Oversharing risk:** Copilot shows anything a user *technically* has access to. Messy SharePoint permissions can expose sensitive files. Expect IT to tighten permissions and use **sensitivity labels** (Microsoft Purview) first.
  - **Agents:** custom agents can be added to Copilot, built in Copilot Studio.
- **Measuring it:** Microsoft provides usage reports (Copilot dashboard / Viva Insights, **verify**), plus surveys and time-saved estimates.

### Power Platform (Microsoft)
- **What it is:** "low-code" tools, meaning you build mostly by clicking and configuring:
  - **Power Automate:** workflows ("when X happens, do Y"), including **desktop flows**, which automate clicks in older systems.
  - **Copilot Studio:** builds AI agents and chat assistants, and publishes them to Teams or M365 Copilot. It used to be called Power Virtual Agents.
  - **Power Apps:** simple custom apps and forms.
  - **AI Builder:** pre-built AI, such as pulling data out of documents **(verify, may be folded into other tools)**.
  - **Dataverse:** Power Platform's own data store.
- **How the bank likely uses it (guess):** probably the most hands-on part of this job. Examples: an agent in Teams answering banker questions from policy documents, a flow that drafts a summary when a deal stage changes in Salesforce, or an intake form for credit requests.
- **What I need to know:**
  - **Connectors:** ready-made links to other systems (Salesforce, SharePoint, Outlook). "Premium" connectors cost extra, and IT decides which are allowed.
  - **DLP policies (data loss prevention):** IT rules about which connectors may share data with which. They often block ideas, so check them first.
  - **Environments:** separate spaces for building, testing and live use.
  - **Who builds what:** non-developers ("citizen developers") vs. IT. Know where the line is.
- **Risk angle:** easy to build means easy to build unsafely. Banks usually require reviews before anything goes live.

### Salesforce
- **What it is:** a "CRM" (customer relationship management system) where bankers track clients, contacts, deals ("opportunities"), pipelines and activities.
- **Key parts (verify):**
  - **Sales Cloud / Financial Services Cloud:** the CRM itself. Financial Services Cloud adds banking features such as relationship maps.
  - **Agentforce:** Salesforce's AI agents (successor branding to "Einstein" AI features).
  - **Einstein Trust Layer:** Salesforce's protections when using AI, such as masking sensitive data and not letting AI providers keep the data.
  - **Prompt Builder and Flow:** tools for building AI prompts and automations inside Salesforce.
  - **Data Cloud:** combines client data from many systems. It may have been renamed **(verify)**.
- **How the bank likely uses it (guess):** the center of "revenue workflows": pipeline management, call planning, referrals between bankers and treasury specialists, and activity logging. Which Salesforce products the bank owns is unknown.
- **What I need to know:**
  - **Data quality:** CRM data is often incomplete because bankers skip logging. AI that logs activity *for* them can be a big win.
  - **"Banker capacity"** in the job description probably means freeing bankers from admin, such as call notes, CRM updates and prep, so they spend more time with clients.
  - Agentforce is priced separately **(verify current pricing model)**.

---

## Part 4: Governance (wrapped around everything)

The job says "governed release" again and again. In a bank, *how* you ship
matters as much as *what* you ship.

- **Model risk management:** US bank regulators expect banks to check, test and monitor their models. The key guidance is **SR 11-7** (Federal Reserve, 2011, with the OCC's matching Bulletin 2011-12). Banks increasingly apply it to AI. It may have been replaced by **SR 26-2** (April 2026, reportedly; item W16 in the Open Items log) **(verify)**.
- **Third-party risk:** using Microsoft, AWS, Salesforce or an AI vendor needs vendor risk reviews (US interagency guidance, 2023).
- **Privacy:** customer financial data is protected by law (for example, the **Gramm-Leach-Bliley Act**). Decide early what data an AI may see.
- **Fair lending:** if AI touches credit decisions, fair-lending laws apply (for example, the **Equal Credit Opportunity Act**). That's a much higher bar, so keep early products away from credit decisions.
- **Responsible AI:** fairness, transparency, human oversight and clear accountability. The **NIST AI Risk Management Framework** (2023) is a common reference. The bank probably has its own policy too **(guess)**.

**What a "governed release" likely includes (guess):**
1. An AI product intake and risk rating (low, medium or high).
2. A data review: what data, whose, and is it allowed?
3. Testing evidence: evals, accuracy, bias checks and red-teaming (trying to break it).
4. Controls: human approval steps, guardrails and logging.
5. Sign-offs from risk, compliance, privacy and security.
6. Monitoring after launch: quality, usage, incidents and drift (quality slipping over time).

---

## Part 5: Measuring success

The job asks for usage, quality, business impact, adoption, and risk and
control measures. A starter set:

| Type | Example measures |
|---|---|
| **Adoption** | Weekly active bankers, % of target users, repeat use |
| **Quality** | Accuracy on evals, % of answers with citations, thumbs up/down |
| **Business impact** | Hours saved per banker, more client meetings, faster deal cycle, pipeline growth |
| **Risk and controls** | Incidents, human overrides, guardrail blocks, review findings |

---

## Things to find out at the bank
- Answered: which of these tools are actually live? All of them, confirmed by the bank (2026-10-09).
- Which AI models are approved, and where do they run?
- Why both Snowflake and Fabric, and which holds what?
- Which Salesforce products and licenses does the bank have?
- What does the AI governance process look like, and how long does it take?
- Who builds: my team, IT, or citizen developers?

_Last updated: 2026-10-19_
