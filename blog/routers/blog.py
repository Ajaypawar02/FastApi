from fastapi import APIRouter, Depends,status, Response, HTTPException

from typing import List
from database import get_db
from sqlalchemy.orm import Session
import models

import schemas
from repository import blog


router = APIRouter(
    prefix="/blogs",
    tags=["blogs"]
)

@router.get('/', response_model = List[schemas.ShowBlog])
def all(db : Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog, db : Session = Depends(get_db)):
    return blog.create(request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response : Response, db : Session = Depends(get_db)):
    return blog.show(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db : Session = Depends(get_db)):
    return blog.destroy(id, db)