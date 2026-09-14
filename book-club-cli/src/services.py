from .models import Status, Book

def add_book(books: list[Book], title: str, author: str) -> None:
    new_book = Book(title, author)
    books.append(new_book)
    print(f"Book '{new_book.title}' by '{new_book.author}' added.")

def remove_book(books: list[Book]  , title: str) -> None:
    for book in books:
        if book.title == title:
            books.remove(book)
            print(f"Book '{title}' removed.")
            return
    print(f"Book '{title}' not found.")

def search_book(books: list[Book], title: str) -> None:
    book_found = False
    for book in books:
        if title in book.title:
            print(f"- {book.title} by {book.author}")
            book_found = True
    
    if not book_found:
        print(f"Book '{title}' not found.")

def change_status(books: list[Book], title: str, new_status: Status) -> None:
    for book in books:
        if title == book.title:
            old_status = book.status
            book.status = new_status
            print(f"- {book.title} by {book.author}. {old_status.value} -> {new_status.value}")
            return
    print(f"Book '{title}' not found.")
    

def list_books(books: list[Book]) -> None:
    if not books:
        print("No books in the list")
    else:
        for book in books:
            print(f"- {book.title} by {book.author} ({book.status.value})")