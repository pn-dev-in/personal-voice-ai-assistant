# Privacy-First Voice AI Assistant

A local, privacy-first voice assistant designed for **daily personal use**, not for surveillance, automation hype, or cloud dependency.

This project focuses on **engineering discipline**: safety, intent control, explicit memory, and reliability — rather than flashy demos.

---

## Why this project exists

Most voice assistants today are:
- Always listening
- Cloud-dependent
- Opaque about data usage
- Difficult to reason about safely

This assistant was built with the opposite philosophy:

- **Push-to-talk only** (no background listening)
- **Local execution** wherever possible
- **Explicit intent & safety gates**
- **User-controlled memory**
- **No silent automation**

The goal is not to replace tools, but to **support focused thinking and daily planning**.

---

## Core Capabilities

### 🎙 Voice Interaction
- Push-to-talk activation via keyboard hotkey
- No always-on microphone
- Low-latency speech-to-text

### 🧠 Reasoning Layer
- Natural language understanding via LLM
- Deterministic intent classification
- Calm, concise responses by default

### 🛡 Safety & Intent Control
Every request is classified before action:

- `QUERY` — informational requests
- `TASK` — limited, sandboxed actions
- `SYSTEM_ACTION` — blocked
- `REJECT` — blocked

The LLM **never executes actions directly**.

---

### 🛠 Safe Tool Execution
- Tools are explicitly registered
- Sandboxed file access only
- No shell commands
- No OS-level actions

Current tools:
- Save personal notes
- Read saved notes

---

### 🧠 Memory (Explicit & Ethical)
- No silent data collection
- Memory only written on explicit user request
- Local persistence (JSON)
- User-auditable and removable

Types of memory:
- Long-term factual memory (explicit)
- Session context (temporary)
- No background profiling

---

### 📅 Daily Briefing / Focus Mode
A calm, proactive mode that:
- Summarizes saved context
- Suggests one focus for the next hour
- Asks one clarifying question

No notifications.  
No nagging.  
Triggered only when requested.

---

## Architecture Overview

Speech Input
↓
Speech-to-Text (Whisper)
↓
Mode Detection
├─ Daily Briefing
└─ Normal Interaction
↓
Memory Intent
↓
Safety Gate
↓
Tool Executor or LLM
↓
Text-to-Speech


**Design principles:**
- Single entry point
- Clear separation of concerns
- Deterministic control flow
- Minimal hidden state
---

## Project Structure

voice_ai_agent/
├── src/
│ ├── main.py # Single entry point
│ ├── audio/ # Speech-to-text
│ ├── brain/ # LLM interaction
│ ├── safety/ # Intent & safety logic
│ ├── tools/ # Sandboxed actions
│ ├── memory/ # Explicit memory
│ ├── modes/ # Interaction modes
│ └── voice/ # Text-to-speech
│
├── user_data/ # Local-only user data
├── config.yaml # Runtime configuration
├── requirements.txt
└── README.md

---

## Privacy & Ethics

This assistant:
- Does **not** listen unless explicitly activated
- Does **not** transmit audio recordings
- Does **not** store data without consent
- Runs entirely on the user’s machine

API keys remain local and are never committed.

---

## Status

- Personal, private assistant
- Actively used and iterated
- Not published as a product
- Not intended for mass deployment

This is a **deliberately scoped personal system**, not a startup demo.

---

## Future Work (Optional)

- Performance tuning
- Config-driven behavior
- Optional open-source framework version (without personal data)

---

## Disclaimer

This project is provided for educational and personal use.
No guarantees are made regarding fitness for production or commercial use.

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
2. Create a virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the project root:

GROQ_API_KEY=your_api_key_here
Note: API keys and personal data are never committed to the repository.

5. Run the assistant
python src/main.py
Press Ctrl + Alt + Space to speak

Press ESC to exit

🧠 Why This Project Exists

This assistant was built to reduce friction in daily thinking and productivity by providing a private, voice-first interface to intelligence, instead of repeatedly opening web-based chat applications.

The goal is not autonomy.
The goal is useful presence with human control.

📌 Notes

This project is intended primarily for personal use
Users must supply their own API keys
Personal memory and notes are stored locally and never shared
Future improvements are guided by real usage, not feature bloat
