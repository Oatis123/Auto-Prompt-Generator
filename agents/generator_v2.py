from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.agents import create_agent
from .models.polza_ai import student, gemini25_pro, claude_sonnet45, deepseek_r1, grok41_fast
from .prompts.lite.teacher import prompt as teacher_prompt
from typing import Literal
from threading import Thread
import json


@tool
def test_student_prompt(system_prompt: str, test_queries: list[str]) -> str:
    """
    Performs batch testing of the system prompt on the "Student" (gemini25_flash).

    Accepts a system prompt and a list of test queries.
    Sequentially executes each request to the "Student" with the specified
    system prompt. Collects all responses.

    Args:
        system_prompt: The system prompt to be tested.
        test_queries: A list of string queries to test the prompt.

    Returns:
        A JSON formatted string. This string is a list of dictionaries,
        where each dictionary contains the "test_query" (the sent query)
        and "student_response" (the received response).
    """
    responses_data: list[dict] = [] 
    for query in test_queries:
        response_content = student.invoke(input=[SystemMessage(content=system_prompt), HumanMessage(query)]).content
        responses_data.append({
            "test_query": query,
            "student_response": response_content
        })

    return json.dumps(responses_data, ensure_ascii=False, indent=2)


clarity_structure_agent = create_agent(
    model=claude_sonnet45,
    tools=[test_student_prompt]
)

creativity_originality_agent = create_agent(
    model=gemini25_pro,
    tools=[test_student_prompt]
)

reasoning_master_agent = create_agent(
    model=deepseek_r1,
    tools=[test_student_prompt]
)

role_persona_agent = create_agent(
    model=grok41_fast,
    tools=[test_student_prompt]
)

output_control_constraints_agent = create_agent(
    model=claude_sonnet45,
    tools=[test_student_prompt]
)

safety_alignment_agent = create_agent(
    model=grok41_fast,
    tools=[test_student_prompt]
)

meta_orchestrator_agent = create_agent(
    model=gemini25_pro,
    tools=[test_student_prompt]
)


def start_agent(agent, request: str, sys_prompt: str)->str:



def generate_prompt_parallel(request: str)->str:
    clarity_structure_agent_thred = Thread()
    


def generate_prompt_linear(request: str)->str:
    pass