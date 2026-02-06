import whisper
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile as wav

SAMPLE_RATE = 16000

print("🔄 Loading Whisper model...")
MODEL = whisper.load_model("base")

def listen(duration: int = 5) -> str:
    print("🎤 Speak now...")
    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype=np.float32
    )
    sd.wait()
    audio = np.squeeze(audio)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, SAMPLE_RATE, audio)
        result = MODEL.transcribe(f.name)
        return result["text"]
