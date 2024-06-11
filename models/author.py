from.base import Base

class Authors(Base, table=True):
    __tablename__ = "authors"
    
    name: str
 
    def __repr__(self):
        return f"<Author {self.name!r}>"