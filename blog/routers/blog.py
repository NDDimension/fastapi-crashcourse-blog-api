from typing import List
from fastapi import APIRouter, status, Depends, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)
get_db = database.get_db


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Blog])
def all(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(
    id: int,
    response: Response,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.show(id, response, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.delete(id, db)


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update(
    id: int,
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.update(id, request, db)
