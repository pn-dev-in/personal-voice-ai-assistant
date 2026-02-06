import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

TASK_PROMPT = """
You are a task interpreter.

Decide if the user wants to:
- save_note
- read_notes
- none

Respond in JSON ONLY.

Format:
{
  "tool": "save_note | read_notes | none",
  "content": "text if needed, else empty"
}
"""

def parse_task(user_text: str) -> dict:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": TASK_PROMPT},
            {"role": "user", "content": user_text}
        ],
        temperature=0
    )

    raw = response.choices[0].message.content.strip()
    return json.loads(raw)
