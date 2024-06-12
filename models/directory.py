# from.base import Base

# class Directory(Base, table=True):
#     __tablename__ = "directory"
    
#     name: str
 
#     def __repr__(self):
#         return f"<Directory {self.name!r}>"
    
    
    # something is missing from this...goal is to have Directory listing author, rating, and 
    
    
from sqlmodel import Field, Relationship
from .base import Base

class Directory(Base, table=True):
    __tablename__ = "directory"

    author_id: int | None = Field(default=None, foreign_key="authors.id")
    title_id: int | None = Field(default=None, foreign_key="titles.id")
    rating_id: int | None= Field(default=None, foreign_key="ratings.id")