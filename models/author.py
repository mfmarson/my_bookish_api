from.base import Base
from sqlmodel import SQLModel, Field

class Authors(Base, SQLModel, table=True):
    __tablename__ = "authors"
    
    name: str
 
    def __repr__(self):
        return f"<Author {self.name!r}>"