from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas

def create_user(db: Session, user: schemas.UserForm):
    hased_password = user.password + '_hashed'
    db_user = models.User(username=user.username, password=hased_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def user_login(db: Session, user: schemas.UserForm):
    hashed_password = user.password + '_hashed'
    return db.query(models.User).filter(models.User.username == user.username and models.User.password == hashed_password).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.uid == user_id).first()

def get_user_by_name(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_topic(db: Session, topic: schemas.TopicForm):
    created_time = datetime.now()
    db_topic = models.Topic(uid=topic.uid, name=topic.name, rank=topic.rank, created_time=created_time)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

def get_topic(db: Session, user_id: int, topic_id: int):
    return db.query(models.Topic).filter(models.Topic.uid == user_id and models.Topic.lid == topic_id).first()

def get_topics_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Topic).offset(skip).limit(limit).all()

def create_note(db: Session, note: schemas.NoteForm):
    modified_time = datetime.now()
    db_note = models.Note(content=note.content, priority=note.priority, modified_time=modified_time, uid=note.uid, lid=note.lid)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.rid == note_id).first()

def get_note_by_user_topic(db: Session, user_id: int, topic_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Note).filter(models.Note.uid == user_id and models.Note.lid == topic_id).offset(skip).limit(limit).all()