from memory.long_term import load_memory
from voice.tts import speak
from brain.llm import ask_llm

def run_daily_briefing():
    memory = load_memory()

    if not memory:
        speak(
            "You don’t have any saved notes yet. "
            "Tell me what you want me to remember, or ask for help with something."
        )
        return

    # Build a concise context for the LLM
    context = "Here are things I know about the user:\n"
    for k, v in memory.items():
        context += f"- {k}: {v}\n"

    prompt = f"""
You are a personal focus assistant.

Using the following context, do THREE things:
1. Briefly summarize what matters today (2–3 sentences max)
2. Suggest ONE clear focus for the next hour
3. Ask ONE simple follow-up question

Keep it calm, short, and practical.

Context:
{context}
"""

    response = ask_llm(prompt)
    speak(response)
