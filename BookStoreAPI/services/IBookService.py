from abc import ABC, abstractmethod

from BookStoreAPI.schemas import BookDTO


class IBookService(ABC):

    @abstractmethod
    async def get_books(self):
        pass

    @abstractmethod
    async def create_book(self, bookDTO: BookDTO):
        pass

    @abstractmethod
    async def delete_book(self, id):
        pass
