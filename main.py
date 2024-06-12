import uvicorn #fastAPI
from fastapi import FastAPI #framework to build API with python
from fastapi.middleware.cors import CORSMiddleware #allow other domain access
from sqlmodel import Session, select #in db.py?
from db import engine #from db.py 

#model classes of tables imported from the models package (file)
from models.author import Authors
from models.rating import Ratings
from models.title import Titles
from models.directory import Directory

app = FastAPI()

#what domains have access 
origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods=['*'],#all HTTP methods (GET,POST,etc.)
    allow_headers=['*']
)
#root endpoint 
@app.get("/") #"/"defines route for root url
async def root():
    return {"message": "Hello World"}

#CRUD endpoints:
@app.get("/author")#route
def list_authors(): #function - execute list of authors
    with Session(engine) as session: #create new database session?
        statement = select(Authors) #SELECT statement to query authors? 
        results = session.exec(statement).all()#execute and fetch results 
    return results #list of authors responding from results execution 

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

# @app.get("/directory/authors")
# def list_author_directory():
#     with Session(engine) as session:
#         statement = select(
#         func.array_agg(Authors.name).label('author_name'),
#         Authors.name.label('authors')
#     ).select_from(Directory).join(Authors, Authors.id == Directory.author_id).join(Titles, Titles.id == Directory.title_id)
#     results = session.exec(statement).mappings().all()
#     return results


#only run code if main is directly executed
if __name__== '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
#runs fastAPI in uvicorn in main instance-hosts at localhost--at port 8000--auto reload code changes 

    




