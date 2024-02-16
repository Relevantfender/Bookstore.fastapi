from fastapi import Depends

from BookStoreAPI.mapper.BookMapper import book_to_bookdto, bookdto_to_book
from BookStoreAPI.models.Book import Book
from BookStoreAPI.repository.BookRepository import get_book_repository
from BookStoreAPI.repository.IBookRepository import IBookRepository
from BookStoreAPI.schemas import BookDTO
from BookStoreAPI.services.IBookService import IBookService
from automapper import mapper


class BookService(IBookService):

    def __init__(self, book_repository: IBookRepository = get_book_repository()):
        self.book_repository = book_repository

    async def get_books(self) -> list[BookDTO]:
        books = await self.book_repository.get_books()
        booksDTO = []
        for book in books:
            booksDTO.append(book_to_bookdto(book))
        return booksDTO

    async def create_book(self, book_dto: BookDTO):
        book = bookdto_to_book(book_dto)
        return await self.book_repository.create_book(book)

    async def delete_book(self, id):
        book = await self.book_repository.get_book_by_id(id)
        if book is None:
            return None
        return await self.book_repository.delete_book(book)

def get_book_service():
    return BookService()
