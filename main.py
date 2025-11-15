from agents.generator_v1 import generate_prompt


prompt_request = input("Request for prompt: ")

print(f"Final prompt: {generate_prompt(request=prompt_request)}")