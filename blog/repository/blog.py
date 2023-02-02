from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException,status
import models
import schemas

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request : schemas.Blog, db : Session):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with {id} not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f'Blog with {id} not found'}
    return blog

def destroy(id : int, db : Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()

    return 'done'
