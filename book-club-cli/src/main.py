books = [
    {
        "title": "The Great Gatsby", 
        "author": "F. Scott Fitzgerald", 
        "status": "to-read"
    },
    {
        "title": "To Kill a Mockingbird", 
        "author": "Harper Lee", 
        "status": "read"
    },
    {
        "title": "1984", 
        "author": "George Orwell", 
        "status": "to-read"
    },
]
book_statuses = {"read", "to-read", "currently-reading"}

def add_book(title, author):
    books.append({
        "title": title, 
        "author": author, 
        "status": "to-read"
    })
    print(f"Book '{title}' by '{author}' added.")

def remove_book(title):
    for book in books:
        if book["title"] == title:
            books.remove(book)
            print(f"Book '{title}' removed.")
            return
    print(f"Book '{title}' not found.")

def search_book(title):
    book_found = False
    for book in books:
        if title in book["title"]:
            print(f"- {book["title"]} by {book["author"]}")
            book_found = True
    
    if not book_found:
        print(f"Book '{title}' not found.")

def change_status(title, new_status):
    for book in books:
        if title == book["title"]:
            old_status = book["status"]
            book["status"] = new_status
            print(f"- {book["title"]} by {book["author"]}. {old_status} -> {new_status}")
            return
    print(f"Book '{title}' not found.")
    

def list_books():
    if not books:
        print("No books in the list")
    else:
        for book in books:
            print(f"- {book["title"]} by {book["author"]} ({book["status"]})")

def main():
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
            add_book(title, author)
        elif choice == "2":
            list_books()
        elif choice == "3":
            title = input("Enter book title to remove: ")
            remove_book(title)
        elif choice == "4":
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == "5":
            title = input("Enter book title to update status: ")

            while True:   
                status = input("Enter read, currently-reading or to-read: ")

                if status in book_statuses:
                    change_status(title, status)
                    break
                else:
                    print("Unknown command")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()