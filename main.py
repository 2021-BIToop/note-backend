from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/sign_up', response_model=schemas.User)
def sign_up(user: schemas.UserForm, db: Session = Depends(get_database)):
    db_user = crud.get_user_by_name(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username is already registered")
    return crud.create_user(db=db, user=user)

@app.post('/sign_in', response_model=schemas.User)
def sign_in(user: schemas.UserForm, db: Session = Depends(get_database)):
    db_user = crud.user_login(db=db, user=user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Username or password error")
    return db_user

@app.get('/user/{username}', response_model=schemas.User)
def user_info(username: str, db: Session = Depends(get_database)):
    db_user = crud.get_user_by_name(db=db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post('/add_topic', response_model=schemas.Topic)
def add_topic(topic: schemas.TopicForm, db: Session = Depends(get_database)):
    db_topic = crud.get_topic_by_name(db=db, user_id=topic.uid, topic_name=topic.name)
    if db_topic:
        raise HTTPException(status_code=400, detail="Topic name is already used")
    return crud.create_topic(db=db, topic=topic)

@app.get('/topic/{topic_id}', response_model=schemas.Topic)
def get_topic_by_id(topic_id: int, db: Session = Depends(get_database)):
    db_topic = crud.get_topic_by_id(db=db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic

@app.get('/topics/{user_id}', response_model=List[schemas.Topic])
def get_topics_by_user(user_id: str, offset: int = 0, limit: int = 100, db: Session = Depends(get_database)):
    db_topics = crud.get_topics_by_user(db=db, user_id=user_id, skip=offset, limit=limit)
    if db_topics is None:
        raise HTTPException(status_code=404, detail="Topic(s) not found")
    return db_topics