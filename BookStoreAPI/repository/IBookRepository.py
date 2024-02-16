from abc import ABC, abstractmethod
from typing import List

from beanie import PydanticObjectId

from BookStoreAPI.models.Book import Book

class IBookRepository(ABC):
    @abstractmethod
    async def get_books(self) -> List[Book]:
        pass

    @abstractmethod
    async def create_book(self, book) -> Book:
        pass

    @abstractmethod
    async def get_book_by_id(self, id: PydanticObjectId) -> Book:
        pass

    @abstractmethod
    def delete_book(self, book):
        pass

