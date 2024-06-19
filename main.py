import uvicorn #fastAPI
from fastapi import FastAPI , Depends #framework to build API with python
from fastapi.middleware.cors import CORSMiddleware #allow other domain access
from sqlmodel import Session, select, func
from  db import get_session
from db import engine #from db.py 

#model classes of tables imported from the models package (file)
from models.author import Authors
from models.title import Titles
from models.directory import Directory
from fastapi.responses import JSONResponse

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
    allow_methods=["*"],#all HTTP methods (GET,POST,etc.)
    allow_headers=["*"]
)


#root endpoint 
@app.get("/") #"/"defines route for root url
async def root():
    return {"message": "Hello World"}

# get books in FastAPI
@app.get("/books")
def get_books(session:Session=Depends(get_session)):
    statement = select(
        Authors.name.label('author'),
        Titles.name.label ('title'), 
        Directory.rating,
    ).select_from(Directory).join(Authors, Authors.id == Directory.author_id).join(Titles, Titles.id == Directory.title_id).group_by(Authors,Titles,Directory.rating)
    results = session.exec(statement).mappings().all()
    return results



# add a new book to your library
@app.post("/books/add")   
def add_book (title: str, title_id, author:str, author_id, rating: int, session:Session = Depends(get_session)):
    book = book(title=title, author=author, rating = rating)
    session.add(book)
    session.commit()
    return {"Book Added:", book.name}


# get authors in FastAPI
@app.get("/author")#route
def list_authors(): #function - execute list of authors
    with Session(engine) as session: #create new database session?
        statement = select(Authors) #SELECT statement to query authors? 
        results = session.exec(statement).all()#execute and fetch results 
    return results #list of authors responding from results execution 

# get titles in FastAPI
@app.get("/title")
def list_titles():
    with Session(engine) as session:
        statement = select(Titles)
        results = session.exec(statement).all()
    return results


@app.get("/directory")
def list_directory():
    with Session(engine) as session:
        statement = select(Directory)
        results = session.exec(statement).all()
    return results

# get titles, author, and rating in directory
@app.get("/directory/authors")
def list_author_directory():
    with Session(engine) as session:
        statement = select(
        Authors.name.label('author'),
        func.json_agg(func.json_build_object(
            "title", Titles.name,
            "rating", Directory.rating,
            #queries start at select_from
            #inner join authors table and directory and overlapping where they match (==) and same with titles
    )).label('book')).select_from(Directory).join(Authors, Authors.id == Directory.author_id).join(Titles, Titles.id == Directory.title_id).group_by(Authors)
    results = session.exec(statement).mappings().all()
    return results


#only run code if main is directly executed
if __name__== '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
#runs fastAPI in uvicorn in main instance-hosts at localhost--at port 8000--auto reload code changes 

    




