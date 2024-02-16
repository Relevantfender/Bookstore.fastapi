from datetime import date
from beanie import Document
from pydantic import BaseModel


class AuthorDTO(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date

    class Config:
        # orm_mode
        from_attributes = True
