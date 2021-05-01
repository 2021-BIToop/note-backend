from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

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
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.post('/sign_in', response_model=schemas.User)
def sign_in(user: schemas.UserForm, db: Session = Depends(get_database)):
    db_user = crud.user_login(db=db, user=user)
    if db_user is None:
        raise HTTPException(status_code=401, detail="Username or password error")
    return db_user

@app.get('/user/{username}', response_model=schemas.User)
def user_info(username: str, db: Session = Depends(get_database)):
    db_user = crud.get_user_by_name(db=db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user