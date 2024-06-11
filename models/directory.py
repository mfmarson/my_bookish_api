from.base import Base

class Directory(Base, table=True):
    __tablename__ = "directory"
    
    name: str
 
    def __repr__(self):
        return f"<Directory {self.name!r}>"
    
    
    # something is missing from this...goal is to have Directory listing author, rating, and title