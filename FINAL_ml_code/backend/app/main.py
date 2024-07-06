from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, database, auth

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/signup", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    return auth.authenticate_user(db, user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_users(db, skip=skip, limit=limit)
