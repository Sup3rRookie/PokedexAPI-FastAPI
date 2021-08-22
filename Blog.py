from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name' : 'aizham'}}

@app.get('/about')
def about():
    return {'data' : 'About Page'}

## Query Parameter
@app.get('/blog')
def myPosts(limit=10, published: bool = True, sort : Optional[str] = True):
    if published:
        return {'data' : f'{limit} published blogs from the db'}
    else:
        return {'data' : f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'Unpublished Blog'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data':id}

