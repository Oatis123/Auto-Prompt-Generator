from langchain_core.tools import tool
from ..models.polza_ai import gemini25_flash
from langchain_core.messages import HumanMessage, SystemMessage


def test_student_prompt(system_prompt: str, test_queries: list[str])->str:
    responses: list[str] = []
    for query in test_queries:
        responses.append(f"Response to query \" {query}\": {gemini25_flash.invoke(input=query)}")

    return "\n".join(responses)