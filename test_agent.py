"""Quick tests for the agent tools and graph wiring."""

import os
import pytest
os.environ.setdefault("BLABLADOR_API_KEY", "test-dummy-key")  # prevent import-time auth error

from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from unittest.mock import patch, MagicMock

from agent import calculator, get_weather, build_graph


# ── Tool unit tests ────────────────────────────────────────────────────────────

def test_calculator_basic():
    assert calculator.invoke({"expression": "2 + 2"}) == "4"

def test_calculator_complex():
    assert calculator.invoke({"expression": "10 * (3 + 2)"}) == "50"

def test_calculator_unsafe():
    result = calculator.invoke({"expression": "__import__('os')"})
    assert "Error" in result

def test_weather_known_city():
    result = get_weather.invoke({"city": "London"})
    assert "15°C" in result

def test_weather_unknown_city():
    result = get_weather.invoke({"city": "Atlantis"})
    assert "No data" in result


# ── Graph smoke test (mocked LLM) ──────────────────────────────────────────────

def test_graph_builds():
    graph = build_graph()
    assert graph is not None


def test_graph_no_tool_call():
    """Graph should return a final answer without tool calls."""
    mock_response = AIMessage(content="Hello! I'm your assistant.")

    with patch("agent.llm_with_tools") as mock_llm:
        mock_llm.invoke.return_value = mock_response
        graph = build_graph()
        result = graph.invoke({"messages": [HumanMessage(content="Hi")]})

    assert result["messages"][-1].content == "Hello! I'm your assistant."
