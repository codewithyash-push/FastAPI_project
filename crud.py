from .database import notes_collection
from .models import NoteInDB

def create_note(note_data: dict):
    result = notes_collection.insert_one(note_data)
    return str(result.inserted_id)

def get_note(note_id: str):
    note = notes_collection.find_one({"_id": note_id})
    if note:
        note["id"] = str(note["_id"])
        return NoteInDB(**note)
    return None

def get_all_notes():
    notes = notes_collection.find()
    return [NoteInDB(**note, id=str(note["_id"])) for note in notes]

def update_note(note_id: str, note_data: dict):
    notes_collection.update_one({"_id": note_id}, {"$set": note_data})

def delete_note(note_id: str):
    notes_collection.delete_one({"_id": note_id})