from BookStoreAPI.models import Author
from BookStoreAPI.models.Book import Book
from BookStoreAPI.schemas import BookDTO, AuthorDTO


def book_to_bookdto(book: Book) -> BookDTO:
    bookDTO = BookDTO(
        isbn=book.isbn,
        title=book.title,
        authors=book.authors,
        number_of_pages=book.number_of_pages,
        year_of_publishing=book.year_of_publishing,
        quantity=book.quantity,
        cover_photo=book.cover_photo
    )

    return bookDTO


def bookdto_to_book(book_dto: BookDTO) -> Book:
    book = Book(
        isbn=book_dto.isbn,
        title=book_dto.title,
        authors=[authordto_to_author(author) for author in book_dto.authors],
        number_of_pages=book_dto.number_of_pages,
        year_of_publishing=book_dto.year_of_publishing,
        quantity=book_dto.quantity,
        cover_photo=book_dto.cover_photo)

    return book


def authordto_to_author(authordto: AuthorDTO) -> Author:
    author = Author(
        first_name = authordto.first_name,
        last_name = authordto.last_name,
        date_of_birth = authordto.date_of_birth
    )
    return author
