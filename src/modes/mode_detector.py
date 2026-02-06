def detect_mode(text: str) -> str:
    text = text.lower()

    triggers = [
        "what should i do today",
        "daily briefing",
        "help me plan my day",
        "what should i focus on",
        "give me a summary"
    ]

    for t in triggers:
        if t in text:
            return "daily_briefing"

    return "normal"
