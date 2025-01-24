import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env')

def generator():
    client = OpenAI(
        base_url="https://api.studio.nebius.ai/v1",
        api_key=os.getenv('N_KEY')
    )

    prompt = """
        create terraform deploy, but please use aws terraform modules for AWS lambda from the docker image with eventbrige trigger
    """
    response = client.chat.completions.create(
        model="Qwen/Qwen2-VL-72B-Instruct",
        messages=[{
            "role":"user",
            "content": [
                {"type": "text",
                 "text": prompt}
            ],
        }],
        max_tokens=700,
    )

    print(f"Response:{response.choices[0].message.content}")

generator()