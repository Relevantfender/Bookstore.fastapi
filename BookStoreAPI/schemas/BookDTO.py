from typing import Optional, List
from beanie import Document
from pydantic import BaseModel
from BookStoreAPI.schemas.AuthorDTO import AuthorDTO


class BookDTO(BaseModel):
    isbn: int
    title: str
    authors: List[AuthorDTO] = []
    number_of_pages: Optional[int] = 0
    year_of_publishing: int
    quantity: int
    cover_photo: Optional[str] = ""

    class Settings:
        name = "Library"

    class Config:
        json_schema_extra = {
            "example": {
                "isbn": 1123456,
                "title": "The Great Gatsby",
                "authors": [{
                    "first_name": "F.Scott",
                    "last_name": "Fitzgerald",
                    "date_of_birth": "yyyy-mm-dd"
                    }],
                "number_of_pages": 632,
                "year_of_publishing": 1926,
                "quantity": 100,
                "cover_photo": "http://www.example.com"
            }
        }
