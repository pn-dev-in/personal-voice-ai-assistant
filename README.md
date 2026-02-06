# 🎙️ Personal Voice-First AI Assistant

A **local, privacy-first, voice-driven AI assistant** designed for personal daily use.
This project focuses on **usability, safety, and control**, not automation hype.

Unlike cloud chatbots, this assistant:
- Runs locally on your machine
- Uses push-to-talk (no always-on listening)
- Stores memory only with explicit consent
- Executes tasks through a safe, sandboxed tool system

---

## ✨ Features

- 🎤 Push-to-talk voice interaction (hands-free, privacy-safe)
- 🧠 LLM-based reasoning (Groq API)
- 🔊 Voice responses (Text-to-Speech)
- 🧭 Intent classification & safety guardrails
- 🗂️ Explicit long-term memory (user-controlled)
- 🛠️ Safe task execution (notes, reminders, etc.)
- 🧩 Modular, extensible architecture

---

## 🏗️ Architecture Overview

- **Voice Input** – User speaks via push-to-talk
- **Speech-to-Text (Whisper)** – Converts audio to text
- **Intent & Safety Layer** – Classifies intent and applies guardrails
- **LLM Reasoning (Groq)** – Generates intelligent responses
- **Tool / Memory Layer** – Executes safe tasks or retrieves memory
- **Text-to-Speech** – Speaks the final response


---

## 🔐 Privacy & Safety Principles

- No always-on microphone
- No silent memory storage
- No OS-level command execution
- No user data sent anywhere except the LLM API
- All sensitive data stored locally

This assistant is designed to be **trustworthy by default**.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add environment variables

Create a .env file:

GROQ_API_KEY=your_api_key_here

5. Run the assistant
python src/main.py


Press Ctrl + Alt + Space to speak.
Press ESC to exit.

🧠 Why This Project Exists

This assistant was built to reduce friction in daily thinking and tasks by acting as a personal AI mediator, rather than repeatedly opening web-based chat interfaces.

The goal is not autonomy — the goal is useful presence with human control.

📌 Notes

This project is intended for personal use

API keys and personal data are not included

Future improvements are guided by real usage, not feature bloat

