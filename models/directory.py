from sqlmodel import Field, Relationship
from .base import Base

class Directory(Base, table=True):
    __tablename__ = "directory"

    author_id: int | None = Field(default=None, foreign_key="authors.id")
    title_id: int | None = Field(default=None, foreign_key="titles.id")
    rating: int | None