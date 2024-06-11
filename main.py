import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from sqlmodel import Session, select
from db import engine
from models.author import Authors
from models.rating import Ratings
from models.title import Titles
from models.directory import Directory

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods=['*'],
    allow_headers=['*']
)
    
@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.get("/author")
def list_authors():
    with Session(engine) as session:
        statement = select(Authors)
        results = session.exec(statement).all()
    return results

@app.get("/title")
def list_titles():
    with Session(engine) as session:
        statement = select(Titles)
        results = session.exec(statement).all()
    return results

@app.get("/rating")
def list_ratings():
    with Session(engine) as session:
        statement = select(Ratings)
        results = session.exec(statement).all()
    return results
    
@app.get("/directory")
def list_directory():
    with Session(engine) as session:
        statement = select(Directory)
        results = session.exec(statement).all()
    return results
    



if __name__== '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)

