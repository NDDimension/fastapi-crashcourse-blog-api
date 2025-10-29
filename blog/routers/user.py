from fastapi import APIRouter, Depends
from .. import schemas, database
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import user as userRepo

router = APIRouter(tags=["Users"], prefix="/user")
get_db = database.get_db


@router.post("/", response_model=schemas.User)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userRepo.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return userRepo.show(id, db)
