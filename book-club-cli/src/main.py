from .storage import load_books, save_books
from .cli import start_cli

def main():
    books = load_books()
    books = start_cli(books)
    save_books(books) 


if __name__ == "__main__":
   main()

    
