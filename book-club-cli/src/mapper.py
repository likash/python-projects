from .models import Status, Book

def book_to_data(book: Book) -> dict:
    return {
        "title": book.title,
        "author": book.author,
        "status": book.status.value
    }

def data_to_book(data: dict) -> Book:
    return Book(
        title=data["title"],
        author=data["author"],
        status=Status(data["status"])
    )

def books_to_data(books: list) -> list:
    return [book_to_data(book) for book in books]

def data_to_books(data: list) -> list:
    return [data_to_book(book_data) for book_data in data]