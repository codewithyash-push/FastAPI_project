const API_URL = "http://localhost:8000/notes";

// Fetch all notes
async function fetchNotes() {
  const response = await fetch(API_URL);
  const notes = await response.json();
  const notesList = document.getElementById("notes-list");
  notesList.innerHTML = "";
  notes.forEach((note) => {
    const noteElement = document.createElement("div");
    noteElement.className = "note";
    noteElement.innerHTML = `
      <h3>${note.title}</h3>
      <p>${note.content}</p>
      <button onclick="deleteNote('${note.id}')">Delete</button>
    `;
    notesList.appendChild(noteElement);
  });
}

// Create a new note
async function createNote() {
  const title = document.getElementById("title").value;
  const content = document.getElementById("content").value;
  await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title, content }),
  });
  fetchNotes();
  document.getElementById("title").value = "";
  document.getElementById("content").value = "";
}

// Delete a note
async function deleteNote(id) {
  await fetch(`${API_URL}/${id}`, {
    method: "DELETE",
  });
  fetchNotes();
}

// Load notes on page load
fetchNotes();