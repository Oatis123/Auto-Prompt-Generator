from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

POLZA_AI_API_KEY = os.getenv("POLZA_AI_API_KEY")
BASE_URL = "https://api.polza.ai/api/v1"


student = ChatOpenAI(
    model="google/gemma-3-12b-it",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
    temperature=0.6
)

gemini25_pro = ChatOpenAI(
    model="google/gemini-2.5-pro",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)

claude_sonnet45 = ChatOpenAI(
    model="anthropic/claude-sonnet-4.5",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)

deepseek_r1 = ChatOpenAI(
    model="deepseek/deepseek-r1",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)

grok41_fast = ChatOpenAI(
    model="x-ai/grok-4.1-fast",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)

llama4_Maverick = ChatOpenAI(
    model="meta-llama/llama-4-maverick",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)

gpt_oss_120b = ChatOpenAI(
    model="openai/gpt-oss-120b",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)

gpt51 = ChatOpenAI(
    model="openai/gpt-5.1",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)

gpto4_mini = ChatOpenAI(
    model="openai/o4-mini",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)