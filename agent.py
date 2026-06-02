"""
Basic ReAct agent built with LangGraph and Helmholtz Blablador.

Blablador exposes an OpenAI-compatible API — no Anthropic key needed.
Graph structure: START -> agent -> [tools | END]

Get your free API key at: https://sdlaml.pages.jsc.fz-juelich.de/ai/guides/blablador_api_access/
"""

import os
from dotenv import load_dotenv
from typing import Annotated
from langchain_core.messages import HumanMessage, BaseMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from typing_extensions import TypedDict

load_dotenv()


# ── State ─────────────────────────────────────────────────────────────────────

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# ── Tools ─────────────────────────────────────────────────────────────────────

@tool
def calculator(expression: str) -> str:
    """Evaluate a basic math expression. Example: '2 + 2 * 10'"""
    try:
        # Restrict to safe math operations
        allowed = set("0123456789+-*/.() ")
        if not all(c in allowed for c in expression):
            return "Error: only basic arithmetic is supported."
        return str(eval(expression))  # noqa: S307 — restricted input above
    except Exception as e:
        return f"Error: {e}"


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city (stub — returns mock data)."""
    mock_data = {
        "london": "Cloudy, 15°C",
        "new york": "Sunny, 22°C",
        "tokyo": "Rainy, 18°C",
    }
    return mock_data.get(city.lower(), f"No data available for '{city}'.")


tools = [calculator, get_weather]


# ── Model ──────────────────────────────────────────────────────────────────────
# Available model aliases:
#   alias-fast  — Ministral-3-14B   (quick responses)
#   alias-large — Qwen3.5-122B      (best quality)
#   alias-code  — Qwen3.5-35B       (coding tasks)
#   alias-huge  — MiniMax-M2.5      (largest)

BLABLADOR_BASE_URL = "https://api.helmholtz-blablador.fz-juelich.de/v1"

llm = ChatOpenAI(
    model="alias-large",
    base_url=BLABLADOR_BASE_URL,
    api_key=os.getenv("BLABLADOR_API_KEY"),
)
llm_with_tools = llm.bind_tools(tools)


# ── Nodes ─────────────────────────────────────────────────────────────────────

def agent_node(state: AgentState) -> AgentState:
    """Call the LLM and return its response."""
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


# ── Graph ─────────────────────────────────────────────────────────────────────

def build_graph() -> StateGraph:
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)
    graph.add_node("tools", ToolNode(tools))

    graph.add_edge(START, "agent")
    # Route: if the model called a tool → tools node; otherwise → END
    graph.add_conditional_edges("agent", tools_condition)
    graph.add_edge("tools", "agent")  # after tool call, re-enter agent

    return graph.compile()


# ── Entry point ───────────────────────────────────────────────────────────────

def run(user_input: str) -> str:
    app = build_graph()
    result = app.invoke({"messages": [HumanMessage(content=user_input)]})
    return result["messages"][-1].content


if __name__ == "__main__":
    print("LangGraph Agent — type 'quit' to exit\n")
    app = build_graph()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        result = app.invoke({"messages": [HumanMessage(content=user_input)]})
        print(f"Agent: {result['messages'][-1].content}\n")
