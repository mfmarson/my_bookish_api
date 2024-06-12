from.base import Base

class Ratings(Base, table=True):
    __tablename__ = "ratings"
    
    rating: int
 
    def __repr__(self):
        return f"<Rating {self.rating!r}>"