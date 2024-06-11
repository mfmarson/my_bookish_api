from.base import Base

class Titles(Base, table=True):
    __tablename__ = "titles"
    
    name: str
 
    def __repr__(self):
        return f"<Title {self.name!r}>"