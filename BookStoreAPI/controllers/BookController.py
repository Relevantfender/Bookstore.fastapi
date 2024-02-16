from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status, Depends
from pymongo.errors import DuplicateKeyError

from BookStoreAPI.dependencies.query_dependencies import book_query
from BookStoreAPI.models.Book import Book
from BookStoreAPI.schemas.BookDTO import BookDTO
from typing import List, Annotated
from BookStoreAPI.services.BookService import get_book_service
from BookStoreAPI.services.IBookService import IBookService

Books = APIRouter()


class BookController:
    def __init__(self, book_service: IBookService = get_book_service()):
        self.book_service = book_service

    async def get_books(self, query):
        return await self.book_service.get_books()

    async def create_book(self, book_dto: BookDTO):
        return await self.book_service.create_book(book_dto)

    async def delete_book(self, id: PydanticObjectId):
        return await self.book_service.delete_book(id)


book_controller = BookController()


@Books.get("/", response_model=list[BookDTO])
async def get_books(query: Annotated[dict, Depends(book_query)]):
    return await book_controller.get_books()


@Books.post("/", status_code=status.HTTP_201_CREATED, response_model=BookDTO)
async def create_book(book_dto: BookDTO):
    try:
        return await book_controller.create_book(book_dto)
    except DuplicateKeyError as e:
        duplicate_key_value = e.details.get("keyvalue", {}).get("isbn")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Book with ISBN '{duplicate_key_value}' already exists."
        )


@Books.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_description="Book successfully deleted")
async def delete_book(id: PydanticObjectId):
    book = await book_controller.delete_book(id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book doesn't exist"
        )


# @Books.put("/{id}", response_model=BookDTO)
# async def update_book(id: PydanticObjectId):
#     book = await BookDTO.get(id)
#     if not BookDTO:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Book with {id} not found"
#         )
#     updated_book = await BookDTO.get(id)
#     return updated_book
#
#
#     _ = await book.update({"$push": {"reviews": review}})
#     updated_book = await book.get(id)
#     return updated_book

