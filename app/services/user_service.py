from sqlalchemy.orm import Session
from app.db import models
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password

# Create new user
def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Get all users
def get_all_users(db: Session):
    return db.query(models.User).all()
