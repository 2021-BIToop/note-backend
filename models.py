from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, LargeBinary
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    topics = relationship('Topic', back_populates='topic_owner')
    notes = relationship('Note', back_populates='note_owner')

class Topic(Base):
    __tablename__ = "topics"

    lid = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    rank = Column(Integer)
    created_time = Column(Date)
    
    uid = Column(Integer, ForeignKey('users.uid'))
    topic_owner = relationship('User', back_populates='topics')

    notes = relationship('Note', back_populates='kind')

class Note(Base):
    __tablename__ = "notes"

    rid = Column(Integer, primary_key=True, index=True)
    content = Column(LargeBinary)
    priority = Column(Integer)
    modified_time = Column(Date)
    
    uid = Column(Integer, ForeignKey('users.uid'))
    note_owner = relationship('User', back_populates='notes')

    lid = Column(Integer, ForeignKey('topics.lid'))
    kind = relationship('Topic', back_populates='notes')

    



