from fastapi import FastAPI, Depends, status, Response, HTTPException
from pydantic import BaseModel
from typing import List
from blog import models
from blog.database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from blog.routers import blog
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog', status_code=status.HTTP_201_CREATED)
# def create(request : schemas.Blog, db : Session = Depends(get_db)):
#     new_blog = models.Blog(title = request.title, body = request.body)
#     db.add(new_blog)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get('/blog', response_model = List[schemas.ShowBlog])
# def all(db : Session = Depends(get_db)):
#     blogs =  db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
# def show(id, response : Response, db : Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:

#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with {id} not found')
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail' : f'Blog with {id} not found'}
#     return blog

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id, db : Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     db.commit()

#     return 'done'










