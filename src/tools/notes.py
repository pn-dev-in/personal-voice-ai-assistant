from pathlib import Path

NOTES_DIR = Path("user_data/notes")
NOTES_DIR.mkdir(parents=True, exist_ok=True)

def save_note(content: str) -> str:
    note_file = NOTES_DIR / "notes.txt"
    with open(note_file, "a", encoding="utf-8") as f:
        f.write(content + "\n")
    return "Note saved successfully."

def read_notes() -> str:
    note_file = NOTES_DIR / "notes.txt"
    if not note_file.exists():
        return "No notes found."
    return note_file.read_text(encoding="utf-8")
