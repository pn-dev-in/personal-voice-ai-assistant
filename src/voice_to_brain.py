import whisper
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile as wav

from brain.llm import ask_llm
from voice.tts import speak
from safety.intent_classifier import classify_intent
from safety.guard import safety_decision
from tools.task_parser import parse_task
from tools.executor import execute_tool
from memory.memory_intent import parse_memory_intent
from memory.long_term import remember, recall


SAMPLE_RATE = 16000
DURATION = 5  # seconds

print("🔄 Loading Whisper model...")
WHISPER_MODEL = whisper.load_model("base")

def record_audio():
    print("🎤 Speak now...")
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype=np.float32
    )
    sd.wait()
    return np.squeeze(audio)

def speech_to_text(audio):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, SAMPLE_RATE, audio)
        result = WHISPER_MODEL.transcribe(f.name)
        return result["text"]

if __name__ == "__main__":
    audio = record_audio()
    text = speech_to_text(audio)

    print("\n📝 You said:")
    print(text)

    intent = classify_intent(text)
    print(f"\n🧭 Detected intent: {intent}")

    # ---- MEMORY HANDLING (PHASE 7) ----
memory_action = parse_memory_intent(text)

if memory_action["action"] == "remember":
    remember(memory_action["key"], memory_action["value"])
    msg = f"I’ll remember that {memory_action['key']} is {memory_action['value']}."
    print(msg)
    speak(msg)
    exit()

if memory_action["action"] == "recall":
    value = recall(memory_action["key"])
    print(value)
    speak(value)
    exit()


    if not safety_decision(intent):
        warning = "Sorry, I can’t help with that request."
        print("\n⛔ Blocked by safety layer")
        speak(warning)
        exit()

    # ---- TASK HANDLING (PHASE 6) ----
    if intent == "TASK":
        task = parse_task(text)

        result = execute_tool(
            task.get("tool", "none"),
            task.get("content", "")
        )

        print("\n🛠 Tool result:")
        print(result)
        speak(result)
        exit()

    # ---- QUERY HANDLING ----
    response = ask_llm(text)

    print("\n🧠 Assistant response:")
    print(response)

    speak(response)
