from backend.services.llm import llm

print("Sending request...")

response = llm.invoke("Say hello")

print(response)