from typing import Optional, List
from beanie import Document, PydanticObjectId, Indexed
from BookStoreAPI.models.Author import Author


class Book(Document):
    id: Optional[PydanticObjectId] = None
    isbn: Indexed(int, unique=True)
    title: str
    authors: List[Author] = []
    number_of_pages: Optional[int] = 0
    year_of_publishing: int
    quantity: int
    cover_photo: Optional[str] = ""

    class Settings:
        name = "Library"

    class Config:
        indexes = ["isbn"]
