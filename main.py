from fastapi import FastAPI, HTTPException
from .models import Note, NoteInDB
from .crud import create_note, get_note, get_all_notes, update_note, delete_note
from bson import ObjectId

app = FastAPI()

@app.post("/notes/", response_model=NoteInDB)
async def create_note_endpoint(note: Note):
    note_id = create_note(note.dict())
    return {**note.dict(), "id": note_id}

@app.get("/notes/{note_id}", response_model=NoteInDB)
async def read_note(note_id: str):
    note = get_note(note_id)
    if note:
        return note
    raise HTTPException(status_code=404, detail="Note not found")

@app.get("/notes/", response_model=list[NoteInDB])
async def read_all_notes():
    return get_all_notes()

@app.put("/notes/{note_id}", response_model=NoteInDB)
async def update_note_endpoint(note_id: str, note: Note):
    update_note(note_id, note.dict())
    updated_note = get_note(note_id)
    if updated_note:
        return updated_note
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/{note_id}")
async def delete_note_endpoint(note_id: str):
    delete_note(note_id)
    return {"message": "Note deleted"}