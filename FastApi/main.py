from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

#get is operatiom
#index ---> path operation function
# @app path operation decorator



@app.get("/blog")
def index(limit = 10, published : bool = True, sort : Optional[str] = None):
    if published:
        return {"data": f'{limit} blog from the db'}
    else:
        return {'data' : "dont return anything"}

# @app.get('/about')
# def xyz():
#     return {"this is about section"}

# @app.get('/blog/{id}')
# def show(id):
#     return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data' : {'1', '2'}}


@app.get('/blog/unpublished')

def unpublished():
    return {
        "data" : 'all unpublished blogs'
    }

@app.get('/blog/{id}')
def show(id : int):
    return {'data' : id}


class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blog')
def create_blog(request : Blog):
    # return request
    return {"data" : f"blog is created {request.title}"}

# if __name__ == "__main__":
#     uvicorn.run(app, host = "127.0.0.1" , port = 9000)






