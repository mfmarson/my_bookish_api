from sqlmodel import Field, SQLModel

class Base(SQLModel):
    id: str = Field(
        default=None,
        primary_key=True,
        index=True,
        nullable=False 
    )