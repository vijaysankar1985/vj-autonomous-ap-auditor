# vj-autonomous-ap-auditor
AI-powered invoice auditing system | AP domain + LangChain + AWS Bedrock | 6-month build log

# Autonomous AP Invoice Auditor

> AI-powered system that autonomously extracts, validates, and flags 
> anomalies in Non-PO invoices using LangChain, LangGraph, and AWS Bedrock.

**Domain:** Accounts Payable + HRIS | **Stack:** Python · LangChain · 
LangGraph · ChromaDB · FastAPI · Docker · AWS (S3, Lambda, Bedrock, Textract)

---

## Business Problem

Enterprise AP teams manually review thousands of Non-PO invoices monthly.
Human review misses duplicate invoices, vendor overcharges, and PO-bypass 
fraud. This system automates extraction, cross-validation, and anomaly 
flagging — reducing manual review load by an estimated 60–70%.

---

## Architecture (evolving)
Month 1: PDF → PyMuPDF → Chunks → ChromaDB → RAG Query → JSON Output
Month 2: + LangGraph Agent → Tool Calling → RAGAS Evaluation → FastAPI
Month 3: + S3 → Lambda → Textract → Bedrock → DynamoDB → SNS
Month 4: + AWS ML Cert · Portfolio Polish · Market Entry
---

## Build Log

| Month | Week | Status | Milestone |
|-------|------|--------|-----------|
| 1 | W1 | 🔄 In Progress | SQL + vectors + Python foundation |
| 1 | W2 | ⬜ Not started | PDF parsing + ChromaDB embeddings |
| 1 | W3 | ⬜ Not started | Full RAG pipeline on AP data |
| 1 | W4 | ⬜ Not started | Metadata filters + CLI tool |
| 2 | W5 | ⬜ Not started | LangGraph 3-node agent |
| 2 | W6 | ⬜ Not started | Tool calling + human-in-loop |
| 2 | W7 | ⬜ Not started | RAGAS evaluation + golden dataset |
| 2 | W8 | ⬜ Not started | FastAPI + Docker |
| 3 | W9 | ⬜ Not started | AWS S3 + Lambda + Textract |
| 3 | W10 | ⬜ Not started | AWS Bedrock integration |
| 3 | W11 | ⬜ Not started | Cost model + security hardening |
| 3 | W12 | ⬜ Not started | Full system + CloudWatch dashboard |

---

## Performance (updated weekly)

| Metric | Value |
|--------|-------|
| Extraction accuracy | TBD |
| RAGAS faithfulness score | TBD |
| Cost per 100 invoices | TBD |
| Avg latency per invoice | TBD |

---

## Repository Structure
vj-autonomous-ap-auditor/
├── src/
│   ├── month1-rag-foundation/   # PDF parsing, embeddings, RAG
│   ├── month2-agents/           # LangGraph, tool calling, FastAPI
│   ├── month3-aws/              # Lambda, Bedrock, DynamoDB
│   └── month4-portfolio/        # Final polished system
├── docs/
│   ├── daily-logs/              # Day-by-day progress notes
│   ├── concepts/                # Concept explainers I wrote
│   ├── architecture/            # ADRs and architecture diagrams
│   └── extra-reads/             # Annotated external resources
├── data/
│   └── sample-invoices/         # Anonymised test data
├── evaluations/                 # RAGAS results, golden datasets
├── prompts/                     # Testing prompts
└── README.md

---

## Author

Vijay | AP + HRIS Domain Expert → AI Solutions Architect  
Built over 6 months · 45 min/day · Started May 2026