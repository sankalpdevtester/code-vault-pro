"""Pydantic schemas"""

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SnippetCreate(BaseModel):
    title: str
    description: str
    code: str
    language: str
    tags: List[str] = []

class SnippetResponse(SnippetCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: List[str] = []

class NoteResponse(NoteCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class ProjectCreate(BaseModel):
    name: str
    description: str
    tech_stack: List[str]
    github_url: Optional[str] = None
    demo_url: Optional[str] = None
    status: str

class ProjectResponse(ProjectCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
