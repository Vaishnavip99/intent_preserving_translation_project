from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_call(prompt, temperature=0.3, force_json=False):
    messages = []

    if force_json:
        messages.append({
            "role": "system",
            "content": "Return ONLY valid JSON. Do not add any extra text."
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message.content.strip()
