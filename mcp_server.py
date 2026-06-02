"""
Local Python MCP server — no Node.js or external API keys required.

Tools exposed:
  - get_current_time   : returns current date and time
  - unit_converter     : converts between common units
  - search_web         : mock web search (returns stub results)
  - text_stats         : word / character / sentence count for any text

Run standalone to verify:
    python mcp_server.py
"""

import os
from datetime import datetime
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()  # loads BLABLADOR_API_KEY from .env

base_url= "https://api.blablador.fz-juelich.de/v1"
api_key=os.getenv("BLABLADOR_API_KEY")

embedding=OpenAIEmbeddings(model="alias-embeddings", api_key=api_key, base_url=base_url)
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding)


mcp = FastMCP("local-tools")


# ── Tool 1: current time ───────────────────────────────────────────────────────

@mcp.tool()
def get_current_time() -> str:
    """Return the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ── Tool 2: unit converter ─────────────────────────────────────────────────────

CONVERSIONS: dict[tuple[str, str], float] = {
    # length
    ("km", "miles"): 0.621371,
    ("miles", "km"): 1.60934,
    ("meters", "feet"): 3.28084,
    ("feet", "meters"): 0.3048,
    ("cm", "inches"): 0.393701,
    ("inches", "cm"): 2.54,
    # weight
    ("kg", "lbs"): 2.20462,
    ("lbs", "kg"): 0.453592,
    ("grams", "oz"): 0.035274,
    ("oz", "grams"): 28.3495,
    # temperature handled separately
}


@mcp.tool()
def unit_converter(value: float, from_unit: str, to_unit: str) -> str:
    """
    Convert a value between common units.

    Supported: km↔miles, meters↔feet, cm↔inches, kg↔lbs, grams↔oz,
               celsius↔fahrenheit, celsius↔kelvin.

    Example: unit_converter(100, 'km', 'miles')
    """
    f, t = from_unit.lower().strip(), to_unit.lower().strip()

    # Temperature special cases
    if f == "celsius" and t == "fahrenheit":
        result = (value * 9 / 5) + 32
    elif f == "fahrenheit" and t == "celsius":
        result = (value - 32) * 5 / 9
    elif f == "celsius" and t == "kelvin":
        result = value + 273.15
    elif f == "kelvin" and t == "celsius":
        result = value - 273.15
    elif (f, t) in CONVERSIONS:
        result = value * CONVERSIONS[(f, t)]
    else:
        return (
            f"Unsupported conversion: {from_unit} → {to_unit}. "
            "Supported pairs: km/miles, meters/feet, cm/inches, "
            "kg/lbs, grams/oz, celsius/fahrenheit, celsius/kelvin."
        )

    return f"{value} {from_unit} = {result:.4f} {to_unit}"


# ── Tool 3: mock web search ────────────────────────────────────────────────────

MOCK_RESULTS: dict[str, list[str]] = {
    "langgraph": [
        "LangGraph — Build stateful, multi-actor applications with LLMs (langchain-ai.github.io)",
        "LangGraph Tutorial: Building a ReAct Agent from scratch (towardsdatascience.com)",
        "LangGraph vs LangChain: when to use which (blog.langchain.dev)",
    ],
    "blablador": [
        "Helmholtz Blablador: free LLM API for researchers (fz-juelich.de)",
        "Getting started with Blablador API (sdlaml.pages.jsc.fz-juelich.de)",
        "Using Blablador with LangChain (sdlaml.pages.jsc.fz-juelich.de)",
    ],
    "mcp": [
        "Model Context Protocol — official docs (modelcontextprotocol.io)",
        "MCP: connecting AI models to the world (anthropic.com)",
        "Building MCP servers in Python with FastMCP (github.com)",
    ],
}
DEFAULT_RESULTS = [
    "Result 1: Introduction to the topic (wikipedia.org)",
    "Result 2: Deep dive tutorial (medium.com)",
    "Result 3: Official documentation (docs.example.com)",
]


@mcp.tool()
def search_web(query: str) -> str:
    """
    Search the web for a query and return top results.
    (Stub — returns mock results for demo purposes.)

    Example: search_web('langgraph tutorials')
    """
    query_lower = query.lower()
    for keyword, results in MOCK_RESULTS.items():
        if keyword in query_lower:
            hits = results
            break
    else:
        hits = DEFAULT_RESULTS

    lines = [f"Search results for: '{query}'", ""]
    for i, hit in enumerate(hits, 1):
        lines.append(f"{i}. {hit}")
    return "\n".join(lines)


# ── Tool 4: text statistics ────────────────────────────────────────────────────

@mcp.tool()
def text_stats(text: str) -> str:
    """
    Return word count, character count, and sentence count for the given text.

    Example: text_stats('Hello world. How are you?')
    """
    words = len(text.split())
    chars = len(text)
    chars_no_space = len(text.replace(" ", ""))
    sentences = text.count(".") + text.count("!") + text.count("?")
    paragraphs = len([p for p in text.split("\n\n") if p.strip()])

    return (
        f"Words       : {words}\n"
        f"Characters  : {chars} (without spaces: {chars_no_space})\n"
        f"Sentences   : {sentences}\n"
        f"Paragraphs  : {paragraphs}"
    )

@mcp.tool()
def calculator(expression: str) -> str:
    """Evaluate a basic math expression. Example: '2 + 2 * 10'"""
    try:
        allowed = set("0123456789+-*/.() ")
        if not all(c in allowed for c in expression):
            return "Error: only basic arithmetic is supported."
        return str(eval(expression))  # noqa: S307 — restricted input above
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a city (stub — returns mock data)."""
    mock_data = {
        "london": "Cloudy, 15°C",
        "new york": "Sunny, 22°C",
        "tokyo": "Rainy, 18°C",
    }
    return mock_data.get(city.lower(), f"No data available for '{city}'.")

@mcp.tool()
def ask_rdm(question: str) -> str:
    """
    Retrieve relevant content from UFZ RDM guidelines to answer a question.
    Use this for any question about data management, storage,
    archiving, publishing, SOPs, RDM tools and more.

    Args:
        question: the question to answer
    """
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    docs = retriever.invoke(question)
    return "\n\n".join(d.page_content for d in docs)


@mcp.tool()
def search_rdm(query: str) -> list[dict]:
    """
    Search RDM docs and return chunks with their sources.
    Use this when you need to know where information comes from.

    Args:
        query: topic to search for
    """
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    docs = retriever.invoke(query)
    return [
        {"content": d.page_content, "source": d.metadata.get("source", "")}
        for d in docs
    ]


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Run as SSE MCP server — client connects via http://localhost:8000/sse
    mcp.run(transport="sse")