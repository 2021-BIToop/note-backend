from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    topics = relationship('Topic', back_populates='topic_owner')
    notes = relationship('Note', back_populates='note_owner')

class Topic(Base):
    __tablename__ = "topics"

    topic_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    rank = Column(Integer)
    created_time = Column(DateTime)
    
    user_id = Column(Integer, ForeignKey('users.user_id'))
    topic_owner = relationship('User', back_populates='topics')

    notes = relationship('Note', back_populates='kind')

class Note(Base):
    __tablename__ = "notes"

    note_id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    priority = Column(Integer)
    modified_time = Column(DateTime)
    
    user_id = Column(Integer, ForeignKey('users.user_id'))
    note_owner = relationship('User', back_populates='notes')

    topic_id = Column(Integer, ForeignKey('topics.topic_id'))
    kind = relationship('Topic', back_populates='notes')

    



