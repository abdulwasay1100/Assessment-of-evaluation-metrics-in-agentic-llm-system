## Getting Started

### 1. Install uv

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install dependencies

```bash
uv sync
```

> This creates the `.venv` and installs all packages from `uv.lock` automatically.

### 3. Activate the virtual environment

```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 4. Register the Jupyter kernel (first time only)

```bash
python -m ipykernel install --user --name=langgraph-agent
```

### 5. Run the MCP server

Open a terminal and keep it running:

```bash
python mcp_server.py
```

The MCP server exposes the following tools to the agent:

| Tool | Description |
|------|-------------|
| `ask_rdm` | Semantic search over the UFZ RDM guidelines via a Chroma vector database |
| `search_rdm` | Lists all indexed documentation files |
| `calculator` | Evaluate a basic math expression.(server testing tool) |

> The server must stay running in its own terminal while using the notebook.

### 6. Run the evaluation notebook

Open Jupyter notebook:

Open `agent_evals.ipynb` and select the **langgraph-agent** kernel.

run the cells for evaluation.