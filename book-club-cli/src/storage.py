from .mapper import data_to_books, books_to_data
import json

data_path = "data/books.json"

def load_books() -> list:
    books = []

    with open(data_path, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("Could not read books data.")
            return []

    books = data_to_books(data)

    return books

def save_books(books: list) -> None:
    data = books_to_data(books)

    with open(data_path, "w") as file:
        json.dump(data, file, indent=4)