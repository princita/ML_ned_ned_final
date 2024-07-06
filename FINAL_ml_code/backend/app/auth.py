from passlib.context import CryptContext
from sqlalchemy.orm import Session
from .models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, user):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user and verify_password(user.password, db_user.hashed_password):
        return db_user
    return False
