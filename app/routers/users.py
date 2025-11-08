from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user_schema import UserResponse
from app.services.user_service import get_all_users

router = APIRouter()

@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="No users found.")
    return users
