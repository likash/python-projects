from dataclasses import dataclass
from enum import Enum
import json

class Status(Enum):
    TO_READ = "to-read"
    CURRENTLY_READING = "currently-reading"
    READ = "read"

@dataclass
class Book:
    title: str
    author: str
    status: Status = Status.TO_READ

def add_book(books, new_book: Book):
    books.append(new_book)
    print(f"Book '{new_book.title}' by '{new_book.author}' added.")

def remove_book(books, title):
    for book in books:
        if book.title == title:
            books.remove(book)
            print(f"Book '{title}' removed.")
            return
    print(f"Book '{title}' not found.")

def search_book(books, title):
    book_found = False
    for book in books:
        if title in book.title:
            print(f"- {book.title} by {book.author}")
            book_found = True
    
    if not book_found:
        print(f"Book '{title}' not found.")

def change_status(books, title, new_status):
    for book in books:
        if title == book.title:
            old_status = book.status
            book.status = new_status
            print(f"- {book.title} by {book.author}. {old_status.value} -> {new_status.value}")
            return
    print(f"Book '{title}' not found.")
    

def list_books(books):
    if not books:
        print("No books in the list")
    else:
        for book in books:
            print(f"- {book.title} by {book.author} ({book.status.value})")

def main(books):
    print("Welcome to Book Club!")

    while True:
        print("\nWhat do you want to do?")
        print("1. Add book")
        print("2. List books")
        print("3. Remove book")
        print("4. Search book")
        print("5. Update book status")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("Add book")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(books, Book(title, author))
        elif choice == "2":
            list_books(books)
        elif choice == "3":
            title = input("Enter book title to remove: ")
            remove_book(books, title)
        elif choice == "4":
            title = input("Enter book title to search: ")
            search_book(books, title)
        elif choice == "5":
            title = input("Enter book title to update status: ")

            while True:   
                status_value = input("Enter read, currently-reading or to-read: ")
                try:
                    status = Status(status_value)
                    change_status(books, title, status)
                    break
                except(ValueError):
                    print("Unknown command")
        elif choice == "6":
            print("Goodbye!")
            return books
        else:
            print("Unknown command")


if __name__ == "__main__":
    data_path = "../data/books.json"
    books = []

    with open(data_path, "r") as file:
        data = json.load(file)

        for book_data in data:
            book = Book(
                book_data["title"],
                book_data["author"],
                Status(book_data["status"])
            )
            books.append(book)

    books = main(books)

    data = []
    
    for book in books:
        book_data = {
            "title": book.title,
            "author": book.author,
            "status": book.status.value
        }
                
        data.append(book_data)

    with open(data_path, "w") as file:

        json.dump(data, file, indent=4)