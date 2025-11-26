import json
import os
from app.models.note import Note

class NoteManager:
    def __init__(self, storage_file="notes.json"):
        self.storage_file = storage_file
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if not os.path.exists(self.storage_file):
            self.notes = []
            return

        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.notes = [Note.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError):
            self.notes = []

    def save_notes(self):
        try:
            data = [note.to_dict() for note in self.notes]
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Erreur lors de la sauvegarde : {e}")

    def add_note(self, title, content):
        new_id = 1
        if self.notes:
            new_id = max(note.id for note in self.notes) + 1
        
        new_note = Note(new_id, title, content)
        self.notes.append(new_note)
        self.save_notes()
        return new_note

    def get_all_notes(self):
        return self.notes

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def update_note(self, note_id, title=None, content=None):
        note = self.get_note_by_id(note_id)
        if note:
            if title is not None:
                note.title = title
            if content is not None:
                note.content = content
            self.save_notes()
            return True
        return False

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            return True
        return False
