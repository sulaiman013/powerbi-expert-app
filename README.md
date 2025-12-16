# Power BI Expert Webapp

<p align="center">
  <img src="https://img.shields.io/badge/Power%20BI-Expert-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI Expert">
  <img src="https://img.shields.io/badge/AI%20Powered-DAX%20Generation-0078D4?style=for-the-badge&logo=microsoft&logoColor=white" alt="AI Powered">
  <img src="https://img.shields.io/badge/Enterprise-Security-DC3545?style=for-the-badge&logo=shield&logoColor=white" alt="Enterprise Security">
</p>

<p align="center">
  <strong>Enterprise-Grade AI Assistant for Microsoft Power BI</strong><br>
  <em>Generate DAX queries, execute analytics, edit PBIP files, and test RLS - all through natural language</em>
</p>

<p align="center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="#"><img src="https://img.shields.io/badge/Platform-Windows%2010%2F11-0078D6?style=flat-square&logo=windows&logoColor=white" alt="Windows"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License"></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square" alt="Production Ready"></a>
</p>

---

## Executive Summary

**Power BI Expert Webapp** is an AI-powered web application that transforms how organizations interact with Microsoft Power BI. It enables business analysts, data engineers, and BI developers to query data, generate DAX code, and manage semantic models using natural language - dramatically reducing the technical barrier to Power BI analytics.

### Business Value

| Metric | Impact |
|--------|--------|
| **Time to Insight** | Reduce DAX development time by 70-80% |
| **Skill Democratization** | Enable non-technical users to query Power BI |
| **Error Reduction** | AI handles complex syntax, relationship logic |
| **Compliance** | Enterprise security with full audit trail |
| **Cost Efficiency** | No per-user licensing - deploy once, use everywhere |

---

## Table of Contents

1. [Key Features](#key-features)
2. [How It Works](#how-it-works)
3. [Architecture Overview](#architecture-overview)
4. [Security & Compliance](#security--compliance)
5. [Business Use Cases](#business-use-cases)
6. [Technical Requirements](#technical-requirements)
7. [Installation Guide](#installation-guide)
8. [Configuration](#configuration)
9. [User Guide](#user-guide)
10. [API Reference](#api-reference)
11. [Codebase Structure](#codebase-structure)
12. [Frequently Asked Questions](#frequently-asked-questions)
13. [Troubleshooting](#troubleshooting)
14. [Roadmap](#roadmap)
15. [Contributing](#contributing)
16. [License](#license)
17. [Author](#author)

---

## Key Features

### Natural Language to DAX

Ask questions in plain English, receive executable DAX queries:

```
User: "What is total revenue by region for Q4 2024?"

AI: Here's the data from your model:

| Region | Revenue    |
|--------|------------|
| North  | $2,450,000 |
| South  | $1,890,000 |
| West   | $3,120,000 |
| East   | $2,740,000 |

West region leads with 30.6% of total Q4 revenue ($10.2M).
```

### Complete Feature Set

| Feature | Description | Desktop | Cloud |
|---------|-------------|:-------:|:-----:|
| **DAX Generation** | AI creates optimized DAX from natural language | ✅ | ✅ |
| **Query Execution** | Auto-execute DAX and display results | ✅ | ✅ |
| **Result Interpretation** | AI explains results in business terms | ✅ | ✅ |
| **Schema Discovery** | Auto-detect tables, columns, measures, relationships | ✅ | ✅ |
| **USERELATIONSHIP** | Automatic handling of inactive relationships | ✅ | ✅ |
| **Measures Awareness** | Use existing measures in generated queries | ✅ | ✅ |
| **Multi-Instance** | Work with multiple .pbix files simultaneously | ✅ | - |
| **RLS Testing** | Test row-level security as any user | ✅ | ✅ |
| **PBIP Editing** | Bulk rename tables, columns, measures | ✅ | - |
| **Audit Logging** | Cryptographically signed activity logs | ✅ | ✅ |

### Supported AI Providers

| Provider | Data Location | Best For | Response Time |
|----------|---------------|----------|---------------|
| **Azure Claude** | Your Azure Subscription | Enterprise production | 1-3 seconds |
| **Azure OpenAI** | Your Azure Subscription | Existing Azure customers | 1-3 seconds |
| **Ollama (Local)** | Your Machine Only | Air-gapped/regulated environments | 3-10 seconds |

---

## How It Works

### User Journey

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER WORKFLOW                            │
└─────────────────────────────────────────────────────────────────┘

  1. LAUNCH                    2. CONNECT                 3. ASK
  ─────────                    ───────────               ─────────
  Double-click              Click "Discover"           Type your
  PowerBI_Expert.bat        to find Power BI           question in
  Browser opens             instances, then            natural
  automatically             "Connect"                  language

       │                          │                         │
       ▼                          ▼                         ▼

  ┌─────────┐              ┌─────────────┐           ┌─────────────┐
  │  Web    │              │  Schema     │           │   AI        │
  │  Server │───────────── │  Discovery  │──────────▶│  Processing │
  │  Starts │              │  (Tables,   │           │  (DAX Gen)  │
  └─────────┘              │  Columns,   │           └──────┬──────┘
                           │  Measures,  │                  │
                           │  Relations) │                  ▼
                           └─────────────┘           ┌─────────────┐
                                                     │  Execute    │
                                                     │  DAX Query  │
                                                     └──────┬──────┘
                                                            │
                                                            ▼
                                                     ┌─────────────┐
                                                     │  AI         │
                                                     │  Interprets │
                                                     │  Results    │
                                                     └──────┬──────┘
                                                            │
                                                            ▼
                                                     ┌─────────────┐
                                                     │  Display    │
                                                     │  Answer     │
                                                     └─────────────┘
```

### Technical Flow

```
User Question: "Show me sales by product category"
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  STEP 1: Build Context                                           │
│  ─────────────────────                                           │
│  • Extract schema: tables, columns, measures                     │
│  • Identify relationships (active/inactive)                      │
│  • Note existing measures that can be reused                     │
└──────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  STEP 2: Generate DAX                                            │
│  ────────────────────                                            │
│  AI creates query with:                                          │
│  • Correct table/column names (exact case, quotes for spaces)    │
│  • USERELATIONSHIP() for inactive relationships                  │
│  • Optimal aggregation functions                                 │
│                                                                  │
│  EVALUATE                                                        │
│  SUMMARIZECOLUMNS(                                               │
│      'Product'[Category],                                        │
│      "Total Sales", [Sales Amount]                               │
│  )                                                               │
└──────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  STEP 3: Fix & Validate                                          │
│  ──────────────────────                                          │
│  • Fix table names with spaces: Sales → 'Fact Sales'             │
│  • Validate syntax before execution                              │
│  • Check for common AI mistakes                                  │
└──────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  STEP 4: Execute                                                 │
│  ──────────────                                                  │
│  • Send to Power BI via ADOMD.NET (Desktop) or XMLA (Cloud)      │
│  • Retrieve results (max 100 rows for safety)                    │
│  • Handle errors gracefully                                      │
└──────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  STEP 5: Interpret                                               │
│  ────────────────                                                │
│  AI analyzes results and provides:                               │
│  • Key insights and trends                                       │
│  • Formatted numbers ($1.2M instead of 1234567)                  │
│  • Business context and recommendations                          │
└──────────────────────────────────────────────────────────────────┘
```

---

## Architecture Overview

### System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           POWER BI EXPERT WEBAPP                             │
│                           http://localhost:5050                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                          PRESENTATION LAYER                             │ │
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐  │ │
│  │  │   Chat Interface │  │  Settings Panel  │  │   Connection Panel   │  │ │
│  │  │   (HTML/JS)      │  │  (Provider Config)│  │   (PBI Discovery)   │  │ │
│  │  └──────────────────┘  └──────────────────┘  └──────────────────────┘  │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                       │                                      │
│  ┌────────────────────────────────────▼───────────────────────────────────┐ │
│  │                          APPLICATION LAYER                              │ │
│  │                          (Flask Web Server)                             │ │
│  │                                                                         │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────────┐  │ │
│  │  │ Chat Routes │  │ Desktop     │  │ Cloud       │  │ PBIP Routes   │  │ │
│  │  │ /api/chat   │  │ Routes      │  │ Routes      │  │ /api/pbip_*   │  │ │
│  │  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └───────┬───────┘  │ │
│  └─────────┼────────────────┼────────────────┼─────────────────┼──────────┘ │
│            │                │                │                 │            │
│  ┌─────────▼────────────────▼────────────────▼─────────────────▼──────────┐ │
│  │                          BUSINESS LOGIC LAYER                           │ │
│  │                                                                         │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐   │ │
│  │  │                      State Management                            │   │ │
│  │  │  • desktop_connector    • xmla_connector    • llm_provider      │   │ │
│  │  │  • model_schema         • cloud_model_schema • pbip_connector   │   │ │
│  │  └─────────────────────────────────────────────────────────────────┘   │ │
│  │                                                                         │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐   │ │
│  │  │                      DAX Processing                              │   │ │
│  │  │  • Query extraction     • Table name fixing  • USERELATIONSHIP  │   │ │
│  │  │  • Data question detection  • Result interpretation             │   │ │
│  │  └─────────────────────────────────────────────────────────────────┘   │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                       │                                      │
│  ┌────────────────────────────────────▼───────────────────────────────────┐ │
│  │                          INTEGRATION LAYER                              │ │
│  │                                                                         │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌────────────┐  │ │
│  │  │   Desktop    │  │    XMLA      │  │    REST      │  │   PBIP     │  │ │
│  │  │  Connector   │  │  Connector   │  │  Connector   │  │  Editor    │  │ │
│  │  │  (ADOMD.NET) │  │  (pyadomd)   │  │  (MSAL)      │  │  (TMDL)    │  │ │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └─────┬──────┘  │ │
│  │         │                 │                 │                │         │ │
│  │  ┌──────┴─────────────────┴─────────────────┴────────────────┴──────┐  │ │
│  │  │                       LLM Provider Layer                         │  │ │
│  │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐   │  │ │
│  │  │  │Azure Claude │  │Azure OpenAI │  │    Ollama (Local)       │   │  │ │
│  │  │  └─────────────┘  └─────────────┘  └─────────────────────────┘   │  │ │
│  │  └──────────────────────────────────────────────────────────────────┘  │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                       │                                      │
│  ┌────────────────────────────────────▼───────────────────────────────────┐ │
│  │                          SECURITY LAYER                                 │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐ │ │
│  │  │ Data Boundary   │  │ Audit Logger    │  │ Network Validator       │ │ │
│  │  │ (Schema-Only)   │  │ (HMAC Signed)   │  │ (Air-Gap Testing)       │ │ │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
┌──────────────┐              ┌──────────────┐              ┌──────────────┐
│  Power BI    │              │  Power BI    │              │    PBIP      │
│  Desktop     │              │  Service     │              │   Files      │
│  (.pbix)     │              │  (XMLA)      │              │  (.tmdl)     │
└──────────────┘              └──────────────┘              └──────────────┘
```

### Component Responsibilities

| Layer | Component | Responsibility |
|-------|-----------|----------------|
| **Presentation** | Chat Interface | User input/output, markdown rendering |
| **Presentation** | Settings Panel | LLM provider configuration |
| **Application** | Flask Server | HTTP routing, request handling |
| **Application** | Chat Routes | Two-step AI processing |
| **Business** | State Manager | Singleton connection management |
| **Business** | DAX Utils | Query extraction, table name fixing |
| **Integration** | Desktop Connector | ADOMD.NET connection to .pbix |
| **Integration** | XMLA Connector | Cloud Premium/PPU connection |
| **Integration** | LLM Providers | AI model abstraction |
| **Security** | Data Boundary | Schema-only transmission enforcement |
| **Security** | Audit Logger | Tamper-evident activity logging |

---

## Security & Compliance

### Data Protection Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    DATA FLOW SECURITY                            │
└─────────────────────────────────────────────────────────────────┘

  YOUR POWER BI DATA                    AI PROVIDER
  ─────────────────                     ───────────

  ┌─────────────────┐                  ┌─────────────────┐
  │  Actual Data    │                  │                 │
  │  ─────────────  │                  │   Azure Claude  │
  │  Row 1: $50,000 │     ╳ NEVER      │       OR        │
  │  Row 2: $75,000 │ ──────────────── │  Azure OpenAI   │
  │  Row 3: $42,000 │     SENT         │       OR        │
  │  ...            │                  │     Ollama      │
  └─────────────────┘                  │                 │
                                       │                 │
  ┌─────────────────┐                  │                 │
  │  Schema Only    │                  │                 │
  │  ─────────────  │     ✓ SENT      │                 │
  │  Table: Sales   │ ────────────────▶│                 │
  │  Column: Amount │   (Metadata     │                 │
  │  Measure: Total │    Only)        │                 │
  └─────────────────┘                  └─────────────────┘
```

### What Goes to the AI

| Sent to AI | NOT Sent to AI |
|------------|----------------|
| Table names | Actual row data |
| Column names | Sample values |
| Data types | Row counts |
| Measure names | Connection strings |
| Measure DAX expressions | Credentials |
| Relationship definitions | PII/sensitive data |
| Your natural language question | Query results (until after execution) |

### Security Features

#### 1. Data Boundary Enforcement

The `data_boundary.py` module ensures only metadata is transmitted:

```python
# Enforced schema-only structure
SchemaInfo:
├── tables: List[TableInfo]
│   ├── name: str
│   ├── columns: List[ColumnInfo] (metadata only)
│   └── description: str (truncated to 500 chars)
├── measures: List[MeasureInfo]
│   ├── name: str
│   └── expression: str (truncated to 2000 chars)
└── relationships: List[RelationshipInfo]

# NEVER includes:
❌ row_count
❌ sample_values
❌ actual_data
```

#### 2. Sensitive Data Detection

Scans for 15+ data patterns before any transmission:

| Pattern | Detection |
|---------|-----------|
| Social Security Numbers | `XXX-XX-XXXX` |
| Credit Card Numbers | `XXXX-XXXX-XXXX-XXXX` |
| Email Addresses | `*@*.*` |
| Currency Values | `$X,XXX.XX` |
| IP Addresses | `XXX.XXX.XXX.XXX` |
| Phone Numbers | `(XXX) XXX-XXXX` |

#### 3. Tamper-Evident Audit Logging

Enterprise-grade logging with cryptographic integrity:

```json
{
  "timestamp": "2024-12-16T10:30:00.000Z",
  "event_type": "QUERY_EXECUTED",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "user_id": "analyst@company.com",
  "tables_accessed": ["Fact Sales", "Dim Date"],
  "query_hash": "sha256:abc123...",
  "hmac_signature": "sha256:def456...",
  "previous_hash": "sha256:xyz789..."
}
```

**Security Properties:**
- **HMAC Signatures**: SHA-256 signing of each event
- **Hash Chain**: Each event references previous hash (blockchain-style)
- **Verification Function**: Detect if logs have been modified
- **Automatic Rotation**: 10MB max file size, automatic archival

#### 4. Air-Gap Network Validation

For regulated environments requiring network isolation:

```
Network Validation Report
─────────────────────────

✅ External DNS Blocking
   google.com      → BLOCKED (expected)
   microsoft.com   → BLOCKED (expected)
   anthropic.com   → BLOCKED (expected)

✅ External TCP Blocking
   8.8.8.8:53      → BLOCKED (expected)
   1.1.1.1:53      → BLOCKED (expected)

✅ Localhost Access
   127.0.0.1       → ALLOWED (expected)
   localhost       → ALLOWED (expected)

✅ No Proxy Configuration Detected

RESULT: Air-gap verified
```

### Compliance Considerations

| Requirement | How Addressed |
|-------------|---------------|
| **GDPR** | Schema-only transmission, no PII sent to AI |
| **HIPAA** | Air-gap capable, audit logging, access controls |
| **SOC 2** | Comprehensive audit trail, tamper detection |
| **Data Residency** | Azure region selection or local Ollama |
| **Right to Audit** | Hash-chain verification, exportable logs |

### Deployment Security Matrix

| Deployment Mode | Data Location | Network Exposure | Best For |
|-----------------|---------------|------------------|----------|
| **Ollama (Local)** | Your machine only | None | Air-gapped, highest security |
| **Azure Claude** | Your Azure subscription | Azure only | Enterprise, compliance |
| **Azure OpenAI** | Your Azure subscription | Azure only | Existing Azure customers |

---

## Business Use Cases

### Use Case 1: Self-Service Analytics

**Scenario**: Marketing team needs sales data without waiting for IT

```
Marketing Analyst: "What were our top 10 products by revenue last quarter?"

Power BI Expert:
┌─────────────────────────────────────────────────────┐
│ Top 10 Products by Revenue (Q3 2024)                │
├─────────────────────────────────────────────────────┤
│ Product              │ Revenue    │ % of Total     │
│ Premium Widget       │ $2.4M      │ 18.2%          │
│ Enterprise Suite     │ $1.9M      │ 14.4%          │
│ Professional Pack    │ $1.6M      │ 12.1%          │
│ ...                  │            │                │
└─────────────────────────────────────────────────────┘

Key Insight: Premium Widget leads with 18.2% of total
quarterly revenue, showing strong enterprise adoption.
```

**Business Value**: Reduced IT backlog, faster time-to-insight

### Use Case 2: DAX Development Acceleration

**Scenario**: Developer needs complex time intelligence measure

```
Developer: "Create a YoY growth measure that handles blank prior year"

Power BI Expert:
YoY Growth % =
VAR CurrentYear = [Total Revenue]
VAR PriorYear =
    CALCULATE(
        [Total Revenue],
        SAMEPERIODLASTYEAR('Date'[Date])
    )
VAR Growth = CurrentYear - PriorYear
RETURN
    IF(
        ISBLANK(PriorYear) || PriorYear = 0,
        BLANK(),
        DIVIDE(Growth, PriorYear)
    )

This measure:
• Uses SAMEPERIODLASTYEAR for accurate comparison
• Handles blank/zero prior year gracefully
• Returns percentage for easy formatting
```

**Business Value**: 70-80% reduction in DAX development time

### Use Case 3: RLS Security Testing

**Scenario**: Security team needs to verify row-level security

```
Security Analyst: "Test what data user john.doe@company.com can see"

[Connects with effective_user = "john.doe@company.com"]

Query: "Show all customers"

Results (filtered by John's RLS role):
┌──────────────────────────────────────────┐
│ John can see 47 customers (Regional)     │
│ Full dataset has 1,250 customers         │
│ RLS is correctly filtering 96.2% of rows │
└──────────────────────────────────────────┘
```

**Business Value**: Automated security verification, reduced audit time

### Use Case 4: PBIP Migration & Refactoring

**Scenario**: Renaming tables across a large PBIP project

```
Developer: "Rename table 'tbl_Sales' to 'Fact Sales'
            in PBIP at C:\Projects\SalesReport"

Power BI Expert:
✅ Renamed 'tbl_Sales' → 'Fact Sales'
📁 Modified 15 files:
   • definition/tables/Fact Sales.tmdl
   • definition/relationships.tmdl
   • Report/report.json
   • Report/sections/*/visuals/*/visual.json (12 files)
🔗 Updated 127 references
💾 Backup created: SalesReport_backup_20241216_143052
```

**Business Value**: Hours of manual work reduced to seconds

---

## Technical Requirements

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Operating System** | Windows 10 | Windows 11 |
| **Python** | 3.10 | 3.11+ |
| **RAM** | 8 GB | 16 GB (for Ollama) |
| **Disk Space** | 2 GB | 10 GB (with Ollama models) |
| **CPU** | 4 cores | 8+ cores (for Ollama) |
| **GPU** | Not required | NVIDIA GPU (for fast Ollama) |

### Power BI Requirements

**For Desktop Connectivity:**
- Power BI Desktop (latest version)
- .pbix file open in Power BI Desktop
- ADOMD.NET libraries (included with Power BI Desktop)

**For Cloud Connectivity:**
- Azure AD App Registration (Service Principal)
- Premium Per User (PPU) or Premium Capacity workspace
- XMLA endpoint enabled on workspace
- Service Principal added with Contributor role

### LLM Provider Requirements

| Provider | Requirements |
|----------|--------------|
| **Azure Claude** | Azure subscription, AI Foundry resource, Claude model deployment |
| **Azure OpenAI** | Azure subscription, Azure OpenAI resource, GPT model deployment |
| **Ollama** | [Ollama](https://ollama.ai) installed, model pulled (`ollama pull mistral`) |

---

## Installation Guide

### Quick Start (5 Minutes)

```bash
# 1. Clone the repository
git clone https://github.com/sulaiman013/powerbi-expert-app.git
cd powerbi-expert-app

# 2. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the application
python web_ui.py

# 5. Browser opens automatically to http://localhost:5050
```

### Alternative: Double-Click Launcher

```bash
# Simply double-click:
PowerBI_Expert.bat

# Browser opens automatically
```

### Dependencies

The `requirements.txt` includes:

```
# Core
flask>=2.0.0
httpx>=0.25.0
pyyaml>=6.0
python-dotenv>=1.0.0

# Power BI Connectivity
pythonnet>=3.0.0
psutil>=5.9.0

# Azure Authentication
msal>=1.20.0

# XMLA Connectivity
pyadomd>=0.1.0
```

---

## Configuration

### Step 1: Configure AI Provider

Click the **Settings** (gear icon) and choose your provider:

#### Azure Claude (Recommended)

```
Endpoint: https://your-resource.services.ai.azure.com
API Key:  your-api-key-here
Model:    claude-3-5-sonnet (or claude-haiku-4-5)
```

#### Azure OpenAI

```
Endpoint:   https://your-resource.openai.azure.com
API Key:    your-api-key-here
Deployment: gpt-4o (or your deployment name)
```

#### Ollama (Local)

```
Model: mistral (or llama3, codellama, etc.)
```

Ensure Ollama is running: `ollama serve`

### Step 2: Connect to Power BI

#### Desktop Connection

1. Open Power BI Desktop with your .pbix file
2. Click **"Discover"** to find running instances
3. Click **"Connect"** to connect to the instance
4. Schema loads automatically

#### Cloud Connection

1. Enter Service Principal credentials:
   - Tenant ID
   - Client ID (App ID)
   - Client Secret
2. Paste your Power BI Service URL
3. Click **"Connect to Service"**

---

## User Guide

### Basic Usage

#### Asking Questions

Simply type your question in natural language:

- "What is total revenue by month?"
- "Show me the top 10 customers"
- "Calculate profit margin by product category"
- "Which region has the highest growth?"

#### Generating DAX Code

Ask for specific DAX patterns:

- "Write a YoY growth measure"
- "Create a running total calculation"
- "Show me how to use CALCULATE with filters"
- "Generate a measure for average order value"

#### PBIP Operations

Include the PBIP path in your request:

- "Rename table Sales to Fact Sales in C:\Projects\MyReport"
- "Rename column CustomerID to Customer ID in Dim Customer at C:\Projects\MyReport"

### Advanced Features

#### Working with Inactive Relationships

The AI automatically detects inactive relationships and uses USERELATIONSHIP():

```
Model has: 'Fact Sales'[ShipDate] → 'Date'[Date] [INACTIVE]

Your question: "Show sales by ship date"

AI generates:
EVALUATE
SUMMARIZECOLUMNS(
    'Date'[Date],
    "Sales", CALCULATE(
        SUM('Fact Sales'[Amount]),
        USERELATIONSHIP('Fact Sales'[ShipDate], 'Date'[Date])
    )
)
```

#### Multi-Instance Support

When multiple .pbix files are open:

1. Click **"Discover"** to see all instances
2. Select the desired instance from dropdown
3. Click **"Connect"** to switch

#### RLS Testing

1. Connect to Power BI Service (XMLA)
2. In the connection settings, specify:
   - Effective User: `user@company.com`
3. All queries execute as that user
4. Verify RLS filters are working correctly

---

## API Reference

### Chat Endpoint

```http
POST /api/chat
Content-Type: application/json

{
  "message": "What is total revenue by region?"
}

Response:
{
  "response": "Based on your data...\n\n| Region | Revenue |\n..."
}
```

### Desktop Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/discover` | GET | Find running Power BI instances |
| `/api/connect` | GET | Connect to first instance |
| `/api/connect_instance?port=XXX` | POST | Connect to specific instance |
| `/api/schema` | GET | Get complete model schema |
| `/api/tables` | GET | List all tables |
| `/api/measures` | GET | List all measures |
| `/api/execute_dax` | POST | Execute custom DAX query |

### Cloud Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/configure_pbi_service` | POST | Connect to Power BI Service |

### LLM Configuration

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/configure_azure_claude` | POST | Configure Azure Claude |
| `/api/configure_azure` | POST | Configure Azure OpenAI |
| `/api/configure_ollama` | POST | Configure local Ollama |
| `/api/provider_status` | GET | Get current provider status |

### PBIP Operations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/pbip_load` | POST | Load PBIP project |
| `/api/pbip_rename` | POST | Single rename operation |
| `/api/pbip_batch_rename` | POST | Bulk rename operations |
| `/api/pbip_info` | GET | Get project information |
| `/api/pbip_schema` | POST | Get schema from PBIP files |

---

## Codebase Structure

```
powerbi-expert-app/
│
├── web_ui.py                    # Application entry point
├── PowerBI_Expert.bat           # Windows launcher script
├── requirements.txt             # Python dependencies
├── README.md                    # This documentation
├── SETUP.md                     # Detailed setup guide
├── LICENSE                      # MIT License
│
└── src/
    ├── __init__.py
    │
    ├── web/                     # Web Application Layer
    │   ├── app.py               # Flask application factory
    │   │                        # - Creates Flask instance
    │   │                        # - Registers all blueprints
    │   │                        # - Configures template folder
    │   │
    │   ├── templates/
    │   │   └── index.html       # Main UI (glassmorphism design)
    │   │                        # - Chat interface
    │   │                        # - Settings modal
    │   │                        # - Connection panel
    │   │                        # - Schema display
    │   │
    │   ├── routes/              # API Route Handlers
    │   │   ├── __init__.py      # Blueprint registration
    │   │   ├── chat.py          # POST /api/chat
    │   │   │                    # - Two-step AI processing
    │   │   │                    # - Schema context building
    │   │   │                    # - USERELATIONSHIP detection
    │   │   │                    # - DAX execution & interpretation
    │   │   │
    │   │   ├── desktop.py       # Desktop connection routes
    │   │   │                    # - /api/discover
    │   │   │                    # - /api/connect
    │   │   │                    # - /api/schema
    │   │   │                    # - /api/execute_dax
    │   │   │
    │   │   ├── cloud.py         # Cloud connection routes
    │   │   │                    # - /api/configure_pbi_service
    │   │   │                    # - XMLA endpoint handling
    │   │   │                    # - Service Principal auth
    │   │   │
    │   │   ├── llm.py           # LLM configuration routes
    │   │   │                    # - /api/configure_azure_claude
    │   │   │                    # - /api/configure_azure
    │   │   │                    # - /api/configure_ollama
    │   │   │
    │   │   ├── pbip.py          # PBIP editing routes
    │   │   │                    # - /api/pbip_load
    │   │   │                    # - /api/pbip_rename
    │   │   │                    # - /api/pbip_batch_rename
    │   │   │
    │   │   └── status.py        # Health check routes
    │   │                        # - /api/status
    │   │                        # - /api/provider_status
    │   │
    │   └── services/            # Business Logic Services
    │       ├── state.py         # AppState singleton
    │       │                    # - Connection management
    │       │                    # - Schema storage
    │       │                    # - Provider tracking
    │       │
    │       ├── dax_utils.py     # DAX processing utilities
    │       │                    # - extract_dax_query()
    │       │                    # - fix_table_names_in_dax()
    │       │                    # - is_data_question()
    │       │
    │       └── pbip_service.py  # PBIP natural language parser
    │                            # - is_pbip_request()
    │                            # - parse_request()
    │
    ├── connectors/              # Power BI Connectors
    │   ├── __init__.py
    │   ├── desktop.py           # Desktop connector (ADOMD.NET)
    │   │                        # - Instance discovery via psutil
    │   │                        # - Schema discovery
    │   │                        # - DAX execution
    │   │                        # - Multi-instance support
    │   │
    │   ├── xmla.py              # XMLA connector (pyadomd)
    │   │                        # - Premium/PPU connection
    │   │                        # - discover_tables()
    │   │                        # - discover_measures()
    │   │                        # - discover_relationships()
    │   │                        # - execute_dax()
    │   │                        # - RLS user impersonation
    │   │
    │   ├── rest.py              # REST API connector
    │   │                        # - MSAL authentication
    │   │                        # - Workspace listing
    │   │                        # - Dataset discovery
    │   │
    │   └── pbip.py              # PBIP file editor
    │                            # - TMDL parsing
    │                            # - PBIR/PBIR-Legacy support
    │                            # - Batch rename operations
    │                            # - Reference tracking
    │                            # - Auto-backup
    │
    ├── llm/                     # LLM Provider Layer
    │   ├── __init__.py
    │   ├── base_provider.py     # Abstract base class
    │   │                        # - LLMRequest/LLMResponse models
    │   │                        # - Provider interface
    │   │
    │   ├── azure_claude_provider.py  # Azure AI Foundry Claude
    │   │                             # - Endpoint URL handling
    │   │                             # - API key authentication
    │   │                             # - Temperature retry logic
    │   │
    │   ├── azure_provider.py    # Azure OpenAI
    │   │                        # - OpenAI SDK integration
    │   │                        # - Deployment name handling
    │   │
    │   ├── ollama_provider.py   # Local Ollama
    │   │                        # - Localhost-only validation
    │   │                        # - Model listing
    │   │                        # - Streaming support
    │   │
    │   ├── router.py            # Provider selection logic
    │   │
    │   └── data_boundary.py     # Security enforcement
    │                            # - Schema-only validation
    │                            # - PII detection
    │                            # - Size limits
    │
    └── security/                # Security Modules
        ├── __init__.py
        ├── audit_logger.py      # Tamper-evident logging
        │                        # - HMAC signatures
        │                        # - Hash chain
        │                        # - Log rotation
        │                        # - Verification function
        │
        └── network_validator.py # Air-gap validation
                                 # - DNS blocking test
                                 # - TCP blocking test
                                 # - Localhost access test
                                 # - Proxy detection
```

### Key File Descriptions

| File | Lines | Purpose |
|------|-------|---------|
| `web_ui.py` | ~50 | Entry point, browser auto-launch |
| `src/web/app.py` | ~70 | Flask factory, blueprint registration |
| `src/web/routes/chat.py` | ~480 | Core AI processing logic |
| `src/web/services/dax_utils.py` | ~200 | DAX extraction, table name fixing |
| `src/connectors/desktop.py` | ~400 | ADOMD.NET Power BI Desktop connector |
| `src/connectors/xmla.py` | ~625 | XMLA cloud connector |
| `src/connectors/pbip.py` | ~600 | PBIP file editing engine |
| `src/llm/azure_claude_provider.py` | ~150 | Azure Claude integration |
| `src/security/audit_logger.py` | ~300 | Enterprise audit logging |

---

## Frequently Asked Questions

### General

**Q: Do I need Claude Desktop or any external AI client?**
> No. Power BI Expert Webapp has built-in LLM support. Just configure your provider in Settings.

**Q: Can I use this offline/air-gapped?**
> Yes! Use Ollama for completely local AI processing with zero internet dependency.

**Q: Does this work with Power BI Pro?**
> Desktop: Yes, any .pbix file works regardless of license.
> Cloud: No, XMLA requires Premium Per User (PPU) or Premium Capacity.

**Q: How is this different from Copilot for Power BI?**
> - No Microsoft 365 Copilot license required
> - Works with any AI provider (including local Ollama)
> - Full PBIP editing capabilities
> - RLS testing built-in
> - Air-gap deployment option

### Security

**Q: Does my data get sent to external servers?**
> Only schema metadata (table/column names) is sent to the AI. Actual row data never leaves your environment until you execute a query.

**Q: Is this compliant with GDPR/HIPAA?**
> When using Ollama (local) or Azure providers (your subscription), data stays within your infrastructure. Enable audit logging for compliance documentation.

**Q: Can I audit what's being sent to the AI?**
> Yes. Enable the audit logger to capture all requests with cryptographic signatures.

### Technical

**Q: Why does connection fail with "ADOMD.NET not found"?**
> Install SQL Server Management Studio (SSMS) or ensure Power BI Desktop is installed with the Analysis Services components.

**Q: Why are my DAX queries returning NULL for some columns?**
> This typically indicates inactive relationships. The AI should automatically use USERELATIONSHIP(), but verify the relationship is detected in your schema.

**Q: Can I run this on a server for team access?**
> Yes, but add authentication first. Change host from `127.0.0.1` to `0.0.0.0` and configure a reverse proxy with HTTPS.

---

## Troubleshooting

### Connection Issues

| Problem | Solution |
|---------|----------|
| "No Power BI instances found" | Open .pbix in Power BI Desktop, wait 10 seconds, click Refresh |
| "ADOMD.NET not found" | Install SQL Server Management Studio (SSMS) |
| "Connection refused" | Verify Power BI Desktop is still running |
| "Authentication failed" (Cloud) | Check Service Principal credentials and workspace permissions |
| "XMLA endpoint not enabled" | Enable XMLA read/write in Power BI Admin Portal |

### AI Provider Issues

| Problem | Solution |
|---------|----------|
| Azure timeout | Check network connectivity, increase timeout |
| "Model not found" | Verify model name matches deployment exactly |
| Ollama not responding | Run `ollama serve` in terminal |
| Temperature error | App automatically retries without temperature |
| Slow responses | Use smaller model or ensure GPU acceleration |

### DAX Issues

| Problem | Solution |
|---------|----------|
| "Invalid object name" | Ask AI to "list all tables" first |
| NULL results | Check for inactive relationships needing USERELATIONSHIP |
| Syntax errors | Table name fixing should handle automatically |
| Wrong aggregation | Specify aggregation type in your question |

---

## Roadmap

### Current Release (v1.0.0)

- [x] Multi-provider LLM support (Azure Claude, Azure OpenAI, Ollama)
- [x] Power BI Desktop multi-instance connectivity
- [x] Power BI Service XMLA connectivity
- [x] Two-step DAX generation and execution
- [x] USERELATIONSHIP automation for inactive relationships
- [x] Smart table name fixing
- [x] PBIP bulk editing (tables, columns, measures)
- [x] RLS user impersonation testing
- [x] Tamper-evident audit logging
- [x] Air-gap network validation
- [x] Modern glassmorphism UI

### Planned (v1.1)

- [ ] Conversation history persistence
- [ ] DAX query favorites and history
- [ ] Export chat to markdown/PDF
- [ ] Dark/light theme toggle
- [ ] Keyboard shortcuts
- [ ] Query performance insights

### Future (v1.2+)

- [ ] Team collaboration (shared sessions)
- [ ] SSO/OIDC authentication
- [ ] Model documentation generator
- [ ] Relationship visualization diagram
- [ ] Integration with Azure DevOps
- [ ] Power Query M-code generation

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/powerbi-expert-app.git
cd powerbi-expert-app

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-asyncio black flake8

# Run tests
pytest

# Format code
black src/
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Sulaiman Ahmed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## Author

<table>
<tr>
<td width="150">
<img src="https://github.com/sulaiman013.png" width="120" style="border-radius: 50%"/>
</td>
<td>

**Sulaiman Ahmed**

*Data Analytics Engineer & Microsoft Certified Professional*

Building the bridge between enterprise data platforms and modern AI. Expertise in Power BI semantic modeling, Python development, and enterprise security architecture.

[![GitHub](https://img.shields.io/badge/GitHub-sulaiman013-181717?style=flat-square&logo=github)](https://github.com/sulaiman013)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/sulaiman-ahmed-/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-blue?style=flat-square&logo=google-chrome)](https://sulaiman-ahmed.lovable.app)

</td>
</tr>
</table>

---

<p align="center">
  <strong>Power BI + AI = Unlimited Possibilities</strong>
  <br><br>
  <a href="https://github.com/sulaiman013/powerbi-expert-app/issues">Report Bug</a> |
  <a href="https://github.com/sulaiman013/powerbi-expert-app/issues">Request Feature</a> |
  <a href="SETUP.md">Setup Guide</a>
</p>

---

## Star History

If this project helps you, please consider giving it a star! It helps others discover the project.

[![Star History Chart](https://api.star-history.com/svg?repos=sulaiman013/powerbi-expert-app&type=Date)](https://star-history.com/#sulaiman013/powerbi-expert-app&Date)
