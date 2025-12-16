# Power BI MCP Server V3 - Complete Setup Guide

This guide walks you through setting up Power BI MCP Server V3 from scratch. Follow the steps in order for a smooth installation.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Installation](#2-installation)
3. [LLM Provider Setup](#3-llm-provider-setup)
   - [Option A: Azure Claude (Recommended)](#option-a-azure-claude-setup)
   - [Option B: Azure OpenAI](#option-b-azure-openai-setup)
   - [Option C: Ollama (Local)](#option-c-ollama-setup)
4. [Power BI Connection Setup](#4-power-bi-connection-setup)
   - [Power BI Desktop (Local)](#power-bi-desktop-local)
   - [Power BI Service (Cloud)](#power-bi-service-cloud)
5. [Running the Application](#5-running-the-application)
6. [Configuration Reference](#6-configuration-reference)
7. [Verification & Testing](#7-verification--testing)
8. [Common Setup Issues](#8-common-setup-issues)

---

## 1. Prerequisites

Before you begin, ensure you have the following installed:

### Required Software

| Software | Version | Download Link |
|----------|---------|---------------|
| **Python** | 3.10 or higher | [python.org/downloads](https://www.python.org/downloads/) |
| **Power BI Desktop** | Latest | [Microsoft Store](https://aka.ms/pbidesktopstore) or [Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=58494) |
| **Git** | Any recent | [git-scm.com](https://git-scm.com/downloads) |

### Verify Python Installation

Open Command Prompt or PowerShell and run:

```powershell
python --version
```

Expected output: `Python 3.10.x` or higher

If Python is not recognized, you may need to:
1. Reinstall Python with "Add to PATH" checked
2. Or manually add Python to your system PATH

### Verify Git Installation

```powershell
git --version
```

Expected output: `git version 2.x.x`

---

## 2. Installation

### Step 2.1: Clone the Repository

Open PowerShell or Command Prompt and run:

```powershell
# Navigate to your desired location
cd C:\Projects  # or wherever you want to install

# Clone the repository
git clone https://github.com/sulaiman013/powerbi-mcp.git

# Navigate to V3 folder
cd powerbi-mcp\powerbi-mcp-v3
```

### Step 2.2: Create Virtual Environment (Recommended)

Creating a virtual environment keeps dependencies isolated:

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On PowerShell:
.\venv\Scripts\Activate.ps1

# On Command Prompt:
.\venv\Scripts\activate.bat
```

You should see `(venv)` at the beginning of your command prompt.

### Step 2.3: Install Dependencies

```powershell
# Install required packages
pip install -r requirements.txt
```

This installs:
- `flask` - Web framework
- `httpx` - HTTP client for LLM APIs
- `pyadomd` - Power BI Desktop connection
- `pythonnet` - .NET integration
- `msal` - Microsoft authentication
- And other dependencies...

### Step 2.4: Verify Installation

```powershell
# Run the test suite
python test_comprehensive.py
```

Don't worry if some tests fail at this point - they require LLM and Power BI configuration.

---

## 3. LLM Provider Setup

Choose ONE of the following options based on your needs:

| Option | Best For | Requires |
|--------|----------|----------|
| **Azure Claude** | Enterprise, security-focused | Azure subscription |
| **Azure OpenAI** | Organizations with existing Azure OpenAI | Azure subscription |
| **Ollama** | Air-gapped, cost-conscious, local development | Local machine with 8GB+ RAM |

---

### Option A: Azure Claude Setup

Azure Claude is the **recommended option** for enterprise deployments.

#### Step A.1: Create Azure AI Foundry Resource

1. Go to [Azure Portal](https://portal.azure.com)

2. Click **Create a resource**

3. Search for **"Azure AI Foundry"** or **"Azure AI Services"**

4. Click **Create**

5. Fill in the details:
   - **Subscription**: Your Azure subscription
   - **Resource group**: Create new or use existing
   - **Region**: Choose your preferred region (e.g., East US, West Europe)
   - **Name**: A unique name (e.g., `mycompany-ai-foundry`)
   - **Pricing tier**: Standard S0

6. Click **Review + create**, then **Create**

7. Wait for deployment to complete (1-2 minutes)

#### Step A.2: Deploy Claude Model

1. Go to your newly created Azure AI resource

2. Click **Model catalog** or **Deployments**

3. Find **Claude** models (Anthropic):
   - `claude-haiku-4-5` - Fastest, most cost-effective
   - `claude-sonnet-4` - Better for complex queries

4. Click **Deploy**

5. Give the deployment a name (e.g., `claude-haiku-4-5`)

6. Wait for deployment to complete

#### Step A.3: Get Credentials

1. In your Azure AI resource, go to **Keys and Endpoint**

2. Copy:
   - **Endpoint**: `https://your-resource-name.services.ai.azure.com`
   - **Key 1**: Your API key (keep this secret!)

3. Note your **Model name** from Step A.2 (e.g., `claude-haiku-4-5`)

#### Step A.4: Configure in V3

When you run the web UI, click the **Settings** button and enter:

```
Provider: Azure Claude
Endpoint: https://your-resource-name.services.ai.azure.com
API Key: your-api-key-here
Model: claude-haiku-4-5
```

Or configure directly in `web_ui.py`:

```python
# Find these lines and update:
AZURE_CLAUDE_ENDPOINT = "https://your-resource-name.services.ai.azure.com"
AZURE_CLAUDE_API_KEY = "your-api-key-here"
AZURE_CLAUDE_MODEL = "claude-haiku-4-5"
```

---

### Option B: Azure OpenAI Setup

Use this if you already have Azure OpenAI resources.

#### Step B.1: Create Azure OpenAI Resource

1. Go to [Azure Portal](https://portal.azure.com)

2. Click **Create a resource**

3. Search for **"Azure OpenAI"**

4. Click **Create**

5. Fill in the details:
   - **Subscription**: Your Azure subscription
   - **Resource group**: Create new or use existing
   - **Region**: Choose a region with OpenAI availability
   - **Name**: A unique name (e.g., `mycompany-openai`)
   - **Pricing tier**: Standard S0

6. Click **Review + create**, then **Create**

> **Note**: Azure OpenAI requires approval. If you don't have access, apply at [aka.ms/oai/access](https://aka.ms/oai/access)

#### Step B.2: Deploy a Model

1. Go to your Azure OpenAI resource

2. Click **Model deployments** > **Manage Deployments**

3. This opens Azure OpenAI Studio

4. Click **Create new deployment**

5. Select a model:
   - `gpt-4o` - Best performance
   - `gpt-4` - Reliable, proven
   - `gpt-35-turbo` - Faster, cheaper

6. Give it a deployment name (e.g., `gpt-4o`)

7. Click **Create**

#### Step B.3: Get Credentials

1. In your Azure OpenAI resource, go to **Keys and Endpoint**

2. Copy:
   - **Endpoint**: `https://your-resource.openai.azure.com`
   - **Key 1**: Your API key

3. Note your **Deployment name** from Step B.2

#### Step B.4: Configure in V3

In the Settings modal:

```
Provider: Azure OpenAI
Endpoint: https://your-resource.openai.azure.com
API Key: your-api-key-here
Deployment: gpt-4o
```

---

### Option C: Ollama Setup

Ollama runs LLMs entirely on your local machine - no cloud required.

#### Step C.1: Install Ollama

1. Download Ollama from [ollama.ai](https://ollama.ai)

2. Run the installer

3. Verify installation:

```powershell
ollama --version
```

Expected output: `ollama version 0.x.x`

#### Step C.2: Pull a Model

Open a new terminal and run:

```powershell
# Recommended for Power BI (good balance of speed and quality)
ollama pull llama3.2

# Alternative options:
ollama pull mistral        # Fast, capable
ollama pull codellama      # Good for code/DAX
ollama pull llama3.2:3b    # Smaller, faster
```

Model sizes:
- `llama3.2` - ~4GB download
- `mistral` - ~4GB download
- `llama3.2:3b` - ~2GB download

#### Step C.3: Start Ollama Server

Ollama usually starts automatically, but if not:

```powershell
ollama serve
```

Keep this terminal open while using V3.

#### Step C.4: Verify Ollama is Running

```powershell
# List available models
ollama list

# Test a model
ollama run llama3.2 "Hello, what is DAX?"
```

#### Step C.5: Configure in V3

In the Settings modal:

```
Provider: Ollama
Endpoint: http://localhost:11434
Model: llama3.2
```

---

## 4. Power BI Connection Setup

### Power BI Desktop (Local)

This is the easiest option - just open your .pbix file!

#### Step 4.1: Verify ADOMD.NET Installation

Power BI Desktop usually includes the required libraries. If not:

1. Install **SQL Server Management Studio (SSMS)** from [Microsoft](https://docs.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms)

   OR

2. Install the ADOMD.NET client separately

#### Step 4.2: Open Your Power BI File

1. Launch **Power BI Desktop**

2. Open your `.pbix` file

3. Wait for the model to fully load (you should see your visuals)

4. **Important**: Keep Power BI Desktop running while using V3

#### Step 4.3: Verify Connection

When you run the V3 web UI, you should see your Power BI file in the sidebar dropdown.

---

### Power BI Service (Cloud)

For cloud datasets, you need a Service Principal.

#### Step 4.4: Create Azure AD App Registration

1. Go to [Azure Portal](https://portal.azure.com)

2. Navigate to **Azure Active Directory** > **App registrations**

3. Click **New registration**

4. Fill in:
   - **Name**: `PowerBI-MCP-Server` (or your choice)
   - **Supported account types**: Single tenant
   - **Redirect URI**: Leave blank

5. Click **Register**

6. Note the **Application (client) ID** - you'll need this

7. Note the **Directory (tenant) ID** - you'll need this

#### Step 4.5: Create Client Secret

1. In your app registration, go to **Certificates & secrets**

2. Click **New client secret**

3. Add a description: `PowerBI MCP`

4. Choose expiration: 12 months or 24 months

5. Click **Add**

6. **IMMEDIATELY copy the secret value** - it won't be shown again!

#### Step 4.6: Grant API Permissions

1. In your app registration, go to **API permissions**

2. Click **Add a permission**

3. Select **Power BI Service**

4. Select **Delegated permissions**

5. Check:
   - `Dataset.Read.All`
   - `Workspace.Read.All`

6. Click **Add permissions**

7. Click **Grant admin consent** (requires admin rights)

#### Step 4.7: Add Service Principal to Power BI Workspace

1. Go to [Power BI Service](https://app.powerbi.com)

2. Navigate to your workspace

3. Click **Access** (or Manage access)

4. Search for your app registration name (`PowerBI-MCP-Server`)

5. Add it with **Member** or **Admin** role

6. Click **Add**

#### Step 4.8: Enable XMLA Endpoint

1. In Power BI Service, go to your workspace

2. Click **Settings** (gear icon) > **Premium**

3. Under **XMLA Endpoint**, select **Read** or **Read Write**

4. Click **Apply**

> **Note**: XMLA endpoints require Premium Per User (PPU) or Premium Capacity

#### Step 4.9: Configure in V3

In the Settings modal, under "Power BI Service":

```
Tenant ID: your-tenant-id
Client ID: your-client-id
Client Secret: your-client-secret
```

---

## 5. Running the Application

### Step 5.1: Start the Web UI

```powershell
# Make sure you're in the powerbi-mcp-v3 folder
cd C:\Projects\powerbi-mcp\powerbi-mcp-v3

# Activate virtual environment (if using)
.\venv\Scripts\Activate.ps1

# Run the web UI
python web_ui.py
```

You should see:

```
============================================================
  Power BI MCP Server V3 - AI-Powered Assistant
============================================================

  Web UI: http://localhost:5050

  Requirements:
  1. LLM provider configured (Azure Claude/Ollama)
  2. Power BI Desktop with a .pbix file open

  Press Ctrl+C to stop
============================================================
```

### Step 5.2: Open the Web Interface

1. Open your browser

2. Go to: **http://localhost:5050**

3. You should see the modern chat interface

### Step 5.3: Configure Settings

1. Click the **Settings** (gear icon) button in the top-right

2. Select your LLM provider tab (Azure Claude, Azure OpenAI, or Ollama)

3. Enter your credentials

4. Click **Save**

### Step 5.4: Connect to Power BI

1. In the sidebar, you should see your Power BI instance(s)

2. Select one from the dropdown

3. Click **Connect to Selected**

4. You should see "Connected to: [Your Model Name]"

### Step 5.5: Start Chatting!

Try these example queries:

```
"What tables are in my model?"
"List all measures"
"Write a DAX measure for total sales"
"Show me the top 5 customers"
```

---

## 6. Configuration Reference

### Environment Variables (Optional)

You can set these environment variables instead of using the Settings modal:

```powershell
# Azure Claude
$env:AZURE_CLAUDE_ENDPOINT = "https://your-resource.services.ai.azure.com"
$env:AZURE_CLAUDE_API_KEY = "your-key"
$env:AZURE_CLAUDE_MODEL = "claude-haiku-4-5"

# Azure OpenAI
$env:AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com"
$env:AZURE_OPENAI_KEY = "your-key"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o"

# Ollama
$env:OLLAMA_ENDPOINT = "http://localhost:11434"
$env:OLLAMA_MODEL = "llama3.2"

# Power BI Service
$env:POWERBI_TENANT_ID = "your-tenant-id"
$env:POWERBI_CLIENT_ID = "your-client-id"
$env:POWERBI_CLIENT_SECRET = "your-secret"
```

### Web UI Configuration

Edit `web_ui.py` to change defaults:

```python
# Line ~2128: Change port
app.run(host='127.0.0.1', port=5050, debug=False, threaded=True)

# Change to your preferred port:
app.run(host='127.0.0.1', port=8080, debug=False, threaded=True)
```

---

## 7. Verification & Testing

### Run Comprehensive Tests

```powershell
python test_comprehensive.py
```

Expected output:

```
============================================================
  POWER BI MCP SERVER V3 - COMPREHENSIVE TEST SUITE
============================================================

TEST 1: Azure Claude Provider
  [OK] Provider initialization: PASS
  [OK] Health check: PASS
  [OK] Text generation: PASS

TEST 2: Power BI Desktop Discovery
  [OK] Desktop connector available: PASS
  [OK] Discover instances (2 found): PASS

TEST 3: Power BI Desktop Connection
  [OK] Connect to Salesforce BI.pbix: PASS
  [OK] List tables (15 found): PASS
  [OK] Execute DAX query: PASS

... (more tests)

============================================================
  Total: 6/6 tests passed
  STATUS: ALL TESTS PASSED!
============================================================
```

### Manual Verification Checklist

- [ ] Web UI loads at http://localhost:5050
- [ ] Settings modal opens and saves
- [ ] Power BI instances appear in sidebar
- [ ] Can connect to a Power BI instance
- [ ] Schema information loads (tables, measures)
- [ ] Chat responses work
- [ ] DAX queries execute successfully

---

## 8. Common Setup Issues

### Issue: "Python is not recognized"

**Solution**: Reinstall Python with "Add Python to PATH" checked, or manually add Python to your system PATH:

1. Find your Python installation (usually `C:\Users\YourName\AppData\Local\Programs\Python\Python311`)
2. Add it to System Environment Variables > Path

### Issue: "No Power BI instances found"

**Solutions**:
1. Make sure Power BI Desktop is running with a .pbix file open
2. Wait 10-15 seconds after opening Power BI Desktop
3. Click "Refresh Instances" in the sidebar
4. Check if ADOMD.NET is installed (install SSMS if needed)

### Issue: "ADOMD.NET not found"

**Solution**: Install SQL Server Management Studio (SSMS):
1. Download from [Microsoft](https://docs.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms)
2. Install (full or custom installation)
3. Restart your computer
4. Try again

### Issue: "Azure Claude authentication failed"

**Check**:
1. Endpoint format is correct: `https://resource-name.services.ai.azure.com`
   - NOT `https://resource-name.services.ai.azure.com/anthropic/v1/messages`
2. API key is correct and not expired
3. Model name matches your deployment exactly
4. Your Azure AI resource is deployed and running

### Issue: "Ollama not responding"

**Solutions**:
1. Make sure Ollama is running: `ollama serve`
2. Check if the model is pulled: `ollama list`
3. Verify endpoint is `http://localhost:11434`
4. Try restarting Ollama

### Issue: "Power BI Service authentication failed"

**Check**:
1. Tenant ID, Client ID, and Client Secret are correct
2. Service Principal has been added to the workspace
3. API permissions are granted (with admin consent)
4. XMLA endpoint is enabled on the workspace
5. Workspace is Premium Per User or Premium Capacity

### Issue: "pip install fails"

**Solutions**:
1. Upgrade pip: `python -m pip install --upgrade pip`
2. Use virtual environment (recommended)
3. If specific package fails, try installing it separately:
   ```powershell
   pip install pythonnet
   pip install pyadomd
   ```

### Issue: "Port 5050 already in use"

**Solutions**:
1. Find what's using the port:
   ```powershell
   netstat -ano | findstr :5050
   ```
2. Kill the process or change the port in `web_ui.py`

---

## Need More Help?

- Check the [README.md](README.md) for FAQ and troubleshooting
- Open an issue on [GitHub](https://github.com/sulaiman013/powerbi-mcp/issues)
- Enable debug mode in `web_ui.py` for detailed error messages

---

<p align="center">
  <strong>Setup Complete!</strong>
  <br><br>
  You're now ready to chat with your Power BI models using AI.
  <br><br>
  <a href="README.md">Back to README</a>
</p>
