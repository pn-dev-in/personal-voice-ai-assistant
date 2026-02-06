import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PROMPT = """
Decide if the user wants to:
- remember: store a personal fact
- recall: retrieve a stored fact
- none

Respond in JSON only.

Format:
{
  "action": "remember | recall | none",
  "key": "",
  "value": ""
}
"""

def parse_memory_intent(user_text: str) -> dict:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": user_text}
        ],
        temperature=0
    )

    raw = response.choices[0].message.content.strip()
    return json.loads(raw)
