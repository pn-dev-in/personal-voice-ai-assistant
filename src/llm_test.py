import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(user_text: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful, concise assistant."},
            {"role": "user", "content": user_text}
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    user_input = input("Enter text: ")
    reply = ask_llm(user_input)
    print("\n🧠 LLM Response:")
    print(reply)
