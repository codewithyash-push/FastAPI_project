from pydantic import BaseModel
from typing import Optional

class Note(BaseModel):
    title: str
    content: str

class NoteInDB(Note):
    id: Optional[str] = None