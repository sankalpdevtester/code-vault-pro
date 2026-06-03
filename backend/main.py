"""
Code Vault Pro - Developer Workspace Platform
FastAPI backend
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db, Base
from models import CodeSnippet, TechnicalNote, Project
from schemas import (
    SnippetCreate, SnippetResponse,
    NoteCreate, NoteResponse,
    ProjectCreate, ProjectResponse
)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Code Vault Pro API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Code Snippets
@app.get("/api/snippets", response_model=List[SnippetResponse])
def get_snippets(db: Session = Depends(get_db)):
    return db.query(CodeSnippet).all()

@app.post("/api/snippets", response_model=SnippetResponse)
def create_snippet(snippet: SnippetCreate, db: Session = Depends(get_db)):
    db_snippet = CodeSnippet(**snippet.dict())
    db.add(db_snippet)
    db.commit()
    db.refresh(db_snippet)
    return db_snippet

@app.get("/api/snippets/{snippet_id}", response_model=SnippetResponse)
def get_snippet(snippet_id: int, db: Session = Depends(get_db)):
    snippet = db.query(CodeSnippet).filter(CodeSnippet.id == snippet_id).first()
    if not snippet:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet

@app.delete("/api/snippets/{snippet_id}")
def delete_snippet(snippet_id: int, db: Session = Depends(get_db)):
    snippet = db.query(CodeSnippet).filter(CodeSnippet.id == snippet_id).first()
    if not snippet:
        raise HTTPException(status_code=404, detail="Snippet not found")
    db.delete(snippet)
    db.commit()
    return {"message": "Snippet deleted"}

# Technical Notes
@app.get("/api/notes", response_model=List[NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    return db.query(TechnicalNote).all()

@app.post("/api/notes", response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = TechnicalNote(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# Projects
@app.get("/api/projects", response_model=List[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

@app.post("/api/projects", response_model=ProjectResponse)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.get("/")
def root():
    return {"name": "Code Vault Pro API", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
