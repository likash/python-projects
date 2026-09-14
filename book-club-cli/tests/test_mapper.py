from src.mapper import data_to_books, books_to_data
from src.models import Book, Status

def test_book_to_data():
    book = Book("1984", "George Orwell", Status.READ)
    data = books_to_data([book])

    assert len(data) == 1
    assert data[0]["title"] == "1984"
    assert data[0]["author"] == "George Orwell"
    assert data[0]["status"] == "read"  

def test_data_to_book():
    data = [
        {"title": "1984", "author": "George Orwell", "status": "read"}
    ]
    books = data_to_books(data)

    assert len(books) == 1
    assert books[0].title == "1984"
    assert books[0].author == "George Orwell"
    assert books[0].status == Status.READ

def test_data_to_book_invalid_status():
    data = [
        {"title": "1984", "author": "George Orwell", "status": "invalid-status"}
    ]
    
    try:
        books = data_to_books(data)
        assert False, "Expected ValueError for invalid status"
    except ValueError as e:
        assert str(e) == "'invalid-status' is not a valid Status"

def test_books_to_data_empty():
    books = []
    data = books_to_data(books)

    assert data == []

def test_data_to_books_empty():
    data = []
    books = data_to_books(data)

    assert books == []