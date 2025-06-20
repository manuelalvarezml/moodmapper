# test_openai.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
            model="gpt-3.5-turbo",
            instructions="You analyze song lyrics.",
            input="Analyze: Hello darkness, my old friend...",
            temperature=0.7,
            max_output_tokens=200,
        )

print(response.output[0].content[0].text)
