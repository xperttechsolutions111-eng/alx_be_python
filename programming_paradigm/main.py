from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    for book in library.list_available_books():
        print(book)

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    for book in library.list_available_books():
        print(book)

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    for book in library.list_available_books():
        print(book)

if __name__ == "__main__":
    main()
