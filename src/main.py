import keyboard
import time
import threading

from audio.stt import listen
from brain.llm import ask_llm
from voice.tts import speak
from safety.intent_classifier import classify_intent
from safety.guard import safety_decision
from tools.task_parser import parse_task
from tools.executor import execute_tool
from memory.memory_intent import parse_memory_intent
from memory.long_term import remember, recall
from modes.mode_detector import detect_mode
from modes.daily_briefing import run_daily_briefing


HOTKEY = "ctrl+alt+space"

interaction_lock = threading.Lock()


def handle_interaction():
    # Prevent overlapping interactions
    if not interaction_lock.acquire(blocking=False):
        print("⏳ Assistant busy, ignoring hotkey.")
        return

    try:
        time.sleep(0.3)  # mic warm-up

        text = listen()

        if not text or len(text.strip()) < 3:
            print("⚠️ No clear speech detected.")
            speak("I didn’t catch that. Please try again.")
            return

        print("\n📝 You said:", text)
        
        # ---- MODE DETECTION ----
        mode = detect_mode(text)

        if mode == "daily_briefing":
            run_daily_briefing()
            return

        # ---- MEMORY ----
        mem = parse_memory_intent(text)

        if mem["action"] == "remember":
            remember(mem["key"], mem["value"])
            speak(f"I’ll remember that {mem['key']} is {mem['value']}.")
            return

        if mem["action"] == "recall":
            speak(recall(mem["key"]))
            return

        # ---- INTENT + SAFETY ----
        intent = classify_intent(text)
        print("🧭 Intent:", intent)

        if not safety_decision(intent):
            speak("Sorry, I can’t help with that request.")
            return

        # ---- TASK ----
        if intent == "TASK":
            task = parse_task(text)
            result = execute_tool(
                task.get("tool", "none"),
                task.get("content", "")
            )
            speak(result)
            return

        # ---- QUERY ----
        response = ask_llm(text)
        speak(response)

    finally:
        interaction_lock.release()


def run():
    print(f"🟢 Assistant running. Press [{HOTKEY}] to talk. Press ESC to exit.")

    keyboard.add_hotkey(HOTKEY, handle_interaction, suppress=True)

    try:
        keyboard.wait("esc")
    except KeyboardInterrupt:
        pass

    print("🔴 Assistant stopped.")


if __name__ == "__main__":
    run()
