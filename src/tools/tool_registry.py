from tools.notes import save_note, read_notes

TOOLS = {
    "save_note": {
        "func": save_note,
        "description": "Save a short text note for the user"
    },
    "read_notes": {
        "func": read_notes,
        "description": "Read all saved user notes"
    }
}
