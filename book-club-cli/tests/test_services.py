from src.services import add_book, list_books, remove_book, change_status, search_book
from src.models import Book, Status

def test_add_book():
    books = []

    add_book(books, "Solaris", "Stanisław Lem")

    assert len(books) == 1
    assert books[0].title == "Solaris"
    assert books[0].author == "Stanisław Lem"
    assert books[0].status == Status.TO_READ
    
def test_list_books_empty(capsys):
    books = []

    list_books(books)

    # Capture the output
    captured = capsys.readouterr()

    assert "No books in the list" in captured.out

def test_remove_book_not_found(capsys):
    books = [Book("Solaris", "Stanisław Lem")]

    remove_book(books, "Non-Existing Book")

    # Capture the output
    captured = capsys.readouterr()

    assert "Book 'Non-Existing Book' not found." in captured.out

def test_remove_book():
    books = [Book("Solaris", "Stanisław Lem")]

    remove_book(books, "Solaris")

    assert len(books) == 0


def test_list_books(capsys):
    books = [Book("Solaris", "Stanisław Lem")]

    list_books(books)

    # Capture the output
    captured = capsys.readouterr()

    assert "- Solaris by Stanisław Lem (to-read)" in captured.out

def test_change_status(capsys):
    books = [Book("Solaris", "Stanisław Lem")]

    # Change status to CURRENTLY_READING
    change_status(books, "Solaris", Status.CURRENTLY_READING)

    # Capture the output
    captured = capsys.readouterr()

    assert "- Solaris by Stanisław Lem. to-read -> currently-reading" in captured.out
    assert books[0].status == Status.CURRENTLY_READING

def test_change_status_not_found(capsys):
    books = [Book("Solaris", "Stanisław Lem")]

    # Attempt to change status of a non-existing book
    change_status(books, "Non-Existing Book", Status.READ)

    # Capture the output
    captured = capsys.readouterr()

    assert "Book 'Non-Existing Book' not found." in captured.out

def test_search_book(capsys):
    books = [Book("Solaris", "Stanisław Lem")]

    # Search for the book
    search_book(books, "Solaris")

    # Capture the output
    captured = capsys.readouterr()

    assert "- Solaris by Stanisław Lem" in captured.out

def test_search_book_not_found(capsys):
    books = [Book("Solaris", "Stanisław Lem")]

    # Search for a non-existing book
    search_book(books, "Non-Existing Book")

    # Capture the output
    captured = capsys.readouterr()

    assert "Book 'Non-Existing Book' not found." in captured.out
