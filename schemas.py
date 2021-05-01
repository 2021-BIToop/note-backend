from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserForm(UserBase):
    password: str

class User(UserBase):
    uid: int
    
    class Config:
        orm_mode = True

class TopicForm(BaseModel):
    name: str
    rank: int

class Topic(TopicForm):
    lid: int
    uid: int
    created_time: datetime

    class Config:
        orm_mode = True

class NoteForm(BaseModel):
    content: str
    priority: int
    uid: int
    rid: int

class Note(NoteForm):
    rid: int
    modified_time: datetime

    class Config:
        orm_mode = True