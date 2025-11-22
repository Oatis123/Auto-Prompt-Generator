from agents.generator_v2 import start_agent
from agents.prompts.heavy.teachers import *
from agents.generator_v2 import *


print(start_agent(agent=role_persona_agent, request="Напиши небольшой промпт для сортировщика писем", sys_prompt=role_persona_prompt))