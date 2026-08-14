from deepeval.test_case import LLMTestCase, ToolCall

TEST_CASES = [
    {
        "id": "TC01",
        "type": "A",
        "question": "Does UFZ require a DMP for DFG-funded projects?",
        "expected_answer": "Yes, UFZ requires a DMP for all DFG-funded projects.",
        "expected_tools": [
            ToolCall(name="search_UFZ_guidelines", input_parameters={})
        ],
        "context": [
            "UFZ requires a Data Management Plan (DMP) for all DFG-funded projects, "
            "as stated in UFZ internal RDM policy."
        ],
    },
]


# --- Builder ---
def build_test_case(tc: dict, result: dict) -> LLMTestCase:
    return LLMTestCase(
        input=tc["question"],
        actual_output=result["actual_output"],
        expected_output=tc["expected_answer"],
        tools_called=result["tools_called"],
        expected_tools=tc["expected_tools"],
        retrieval_context=result["retrieval_context"],  # from the agent run — for Faithfulness, Contextual*
        context=tc["context"],                           # authored ground truth — for Hallucination
    )