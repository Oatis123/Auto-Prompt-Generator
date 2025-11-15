from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

POLZA_AI_API_KEY = os.getenv("POLZA_AI_API_KEY")
BASE_URL = "https://api.polza.ai/api/v1"


deepseek_r1 = ChatOpenAI(
    model="deepseek/deepseek-r1",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)

grok4_fast = ChatOpenAI(
    model="x-ai/grok-4-fast",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)

gemini25_flash = ChatOpenAI(
    model="google/gemini-2.5-flash",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
    temperature=0.6
)

llama4_Maverick = ChatOpenAI(
    model="meta-llama/llama-4-maverick",
    api_key=POLZA_AI_API_KEY,
    base_url=BASE_URL,
)