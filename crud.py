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
    return db.query(models.User).filter(models.User.username == user.username, models.User.password == hashed_password).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_name(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_topic(db: Session, topic: schemas.TopicForm):
    created_time = datetime.now()
    db_topic = models.Topic(user_id=topic.user_id, name=topic.name, rank=topic.rank, created_time=created_time)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

def update_topic(db: Session, topic: schemas.TopicForm):
    db_topic = db.query(models.Topic).filter(models.Topic.topic_id == topic.topic_id).first()
    db_topic.name = topic.name
    db_topic.rank = topic.rank
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

def get_topic_by_id(db: Session, topic_id: int):
    return db.query(models.Topic).filter(models.Topic.topic_id == topic_id).first()

def get_topic_by_name(db: Session, user_id: int, topic_name: int):
    return db.query(models.Topic).filter(models.Topic.user_id == user_id, models.Topic.name == topic_name).first()

def get_topic_by_id_user(db: Session, topic_id: int, user_id: int):
    return db.query(models.Topic).filter(models.Topic.topic_id == topic_id, models.Topic.user_id == user_id).first()

def get_topics_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Topic).filter(models.Topic.user_id == user_id).offset(skip).limit(limit).all()

def remove_topic_by_user(db: Session, user_id: int, topic_id: int):
    db_topic = db.query(models.Topic).filter(models.Topic.user_id == user_id, models.Topic.topic_id == topic_id).first()
    db.delete(db_topic)
    db.commit()
    return get_topics_by_user(db, user_id)

def create_note(db: Session, note: schemas.NoteForm):
    modified_time = datetime.now()
    db_note = models.Note(content=note.content, priority=note.priority, modified_time=modified_time, user_id=note.user_id, topic_id=note.topic_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note: schemas.NoteForm):
    modified_time = datetime.now()
    db_note = db.query(models.Note).filter(models.Note.note_id == note.note_id).first()
    db_note.content = note.content
    db_note.priority = note.priority
    db_note.topic_id = note.topic_id
    db_note.modified_time = modified_time
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_note_by_id(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.note_id == note_id).first()

def get_note_by_user_topic(db: Session, user_id: int, topic_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Note).filter(models.Note.user_id == user_id, models.Note.topic_id == topic_id).offset(skip).limit(limit).all()

def remove_note_by_user(db: Session, user_id: int, topic_id: int, note_id: int):
    db_note = db.query(models.Note).filter(models.Note.user_id == user_id, models.Note.topic_id == topic_id, models.Note.note_id == note_id).first()
    db.delete(db_note)
    db.commit()
    return get_note_by_user_topic(db, user_id, topic_id)