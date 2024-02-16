from typing import List

from beanie import PydanticObjectId

from BookStoreAPI.models.Book import Book
from BookStoreAPI.repository.IBookRepository import IBookRepository


class BookRepository(IBookRepository):

    async def get_books(self) -> List[Book]:
        books = await Book.find_all().to_list()
        return books

    async def create_book(self, book: Book) -> Book:
        return await Book.insert_one(book)

    async def get_book_by_id(self, id: PydanticObjectId) -> Book:
        return await Book.get(id)

    async def delete_book(self, book):
        return await Book.delete(book)

    # async def update_book(id: PydanticObjectId):
    # book = await BookDTO.get(id)
    # if not BookDTO:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"Book with {id} not found"
    #     )
    # updated_book = await BookDTO.get(id)
    # return updated_book
    #  pass

    # async def add_review(id: PydanticObjectId, review: str):
    # book = await BookDTO.get(id)
    # if not BookDTO:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"Book with {id} not found"
    #     )
    # _ = await book.update({"$push": {"reviews": review}})
    # updated_book = await book.get(id)
    # return updated_book
    #   pass



def get_book_repository():
    return BookRepository()
