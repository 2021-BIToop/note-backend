from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserForm(UserBase):
    password: str

class User(UserBase):
    user_id: int
    
    class Config:
        orm_mode = True

class TopicForm(BaseModel):
    topic_id: Optional[int] = None
    name: str
    rank: int
    user_id: int

class Topic(TopicForm):
    created_time: datetime

    class Config:
        orm_mode = True

class NoteForm(BaseModel):
    note_id: Optional[int] = None
    content: str
    priority: int
    user_id: int
    topic_id: int

class Note(NoteForm):
    modified_time: datetime

    class Config:
        orm_mode = True