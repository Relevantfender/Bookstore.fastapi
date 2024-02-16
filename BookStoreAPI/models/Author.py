from datetime import date
from typing import Optional

from beanie import Document, PydanticObjectId
from pydantic import BaseModel


class Author(Document):
    first_name: str
    last_name: str
    date_of_birth: date

    class Config:
        from_attributes = True
