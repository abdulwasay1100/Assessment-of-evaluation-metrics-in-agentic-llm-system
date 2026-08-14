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

# Load both collections from the same chroma_db
ufz_store = Chroma(
    collection_name="ufz_guidelines",
    persist_directory="./chroma_db",
    embedding_function=embedding,
)

funding_store = Chroma(
    collection_name="funding_guidelines",
    persist_directory="./chroma_db",
    embedding_function=embedding,
)


mcp = FastMCP("local-tools")


# ── Tool 1: current time ───────────────────────────────────────────────────────

# @mcp.tool()
# def get_current_time() -> str:
#     """Return the current date and time."""
#     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# @mcp.tool()
# def search_web(query: str) -> str:
#     """
#     Search the web for a query and return top results.
#     (Stub — returns mock results for demo purposes.)

#     Example: search_web('langgraph tutorials')
#     """
#     query_lower = query.lower()
#     for keyword, results in MOCK_RESULTS.items():
#         if keyword in query_lower:
#             hits = results
#             break
#     else:
#         hits = DEFAULT_RESULTS

#     lines = [f"Search results for: '{query}'", ""]
#     for i, hit in enumerate(hits, 1):
#         lines.append(f"{i}. {hit}")
#     return "\n".join(lines)


# # ── Tool 4: text statistics ────────────────────────────────────────────────────

# @mcp.tool()
# def text_stats(text: str) -> str:
#     """
#     Return word count, character count, and sentence count for the given text.

#     Example: text_stats('Hello world. How are you?')
#     """
#     words = len(text.split())
#     chars = len(text)
#     chars_no_space = len(text.replace(" ", ""))
#     sentences = text.count(".") + text.count("!") + text.count("?")
#     paragraphs = len([p for p in text.split("\n\n") if p.strip()])

#     return (
#         f"Words       : {words}\n"
#         f"Characters  : {chars} (without spaces: {chars_no_space})\n"
#         f"Sentences   : {sentences}\n"
#         f"Paragraphs  : {paragraphs}"
#     )

# @mcp.tool()
# def calculator(expression: str) -> str:
#     """Evaluate a basic math expression. Example: '2 + 2 * 10'"""
#     try:
#         allowed = set("0123456789+-*/.() ")
#         if not all(c in allowed for c in expression):
#             return "Error: only basic arithmetic is supported."
#         return str(eval(expression))  # noqa: S307 — restricted input above
#     except Exception as e:
#         return f"Error: {e}"

@mcp.tool()
def search_UFZ_guidelines(question: str) -> str:
    """
    Retrieve relevant content from UFZ RDM guidelines to answer a question.
    Use this for any question about UFZ internal data management requirements:
    storage, archiving, publishing, metadata standards, SOPs, RDM tools and more.

    Args:
        question: the question to answer
    """
    docs = ufz_store.similarity_search(question, k=5)
    return "\n\n".join(d.page_content for d in docs)


@mcp.tool()
def search_funding_guidelines(question: str, agency: str = None) -> str:
    """
    Retrieve relevant content from external funding agency DMP requirements.
    Use this when the question concerns funder-mandated data management requirements.

    Args:
        question: the question to answer
        agency: optional filter — one of 'FNR', 'Uni_Siegen', 'EU_Horizon'
    """
    filter = {"source": agency} if agency else None
    docs = funding_store.similarity_search(question, k=5, filter=filter)
    return "\n\n".join(d.page_content for d in docs)

# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Run as SSE MCP server — client connects via http://localhost:8000/sse
    mcp.run(transport="sse")