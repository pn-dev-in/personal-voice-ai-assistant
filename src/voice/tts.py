import pyttsx3
import threading

_engine = pyttsx3.init()
_lock = threading.Lock()

_engine.setProperty("rate", 170)
_engine.setProperty("volume", 1.0)

def speak(text: str):
    if not text:
        return

    with _lock:
        _engine.say(text)
        _engine.runAndWait()
