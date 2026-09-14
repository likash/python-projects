from .services import add_book, list_books, remove_book, change_status, search_book
from .models import Status, Book

def start_cli(books: list[Book]) -> list[Book]:
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
            add_book(books, title, author)
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
                except ValueError:
                    print("Unknown status. Please enter read, currently-reading or to-read.")
        elif choice == "6":
            print("Goodbye!")
            return books
        else:
            print("Unknown command")        