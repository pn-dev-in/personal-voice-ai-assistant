import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

INTENT_PROMPT = """
Classify the user's intent into ONE of the following categories:

- QUERY: Asking for information or explanation
- TASK: Asking to perform a benign task (no execution yet)
- SYSTEM_ACTION: Asking to control system, files, apps, or OS
- REJECT: Dangerous, malicious, illegal, or unclear intent

Respond ONLY with the category name.
"""

def classify_intent(user_text: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": INTENT_PROMPT},
            {"role": "user", "content": user_text}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()
