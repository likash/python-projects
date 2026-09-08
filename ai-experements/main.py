import os
from dotenv import load_dotenv
from openai import OpenAI

# Завантажуємо змінні з файлу .env
load_dotenv()

print("Початок виконання скрипту...")

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]



prompt = "You're an expert on the Python language Suggest a beginner lesson for Python in the following format: Format: - concepts: - brief explanation of the lesson: - exercise in code with solutions"

response = client.responses.create(model=deployment_name, input=prompt, store=False)


# виведіть відповідь
print(response.output_text)