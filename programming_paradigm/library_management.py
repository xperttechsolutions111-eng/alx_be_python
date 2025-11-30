class Book:
    def __init__(self, title, author):
        self.title = title                # Public attribute
        self.author = author              # Public attribute
        self._is_checked_out = False      # Private attribute

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list of Book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"Checked out '{title}'"
        return f"'{title}' is not available"

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"Returned '{title}'"
        return f"'{title}' was not checked out"

    def list_available_books(self):
        return [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
if __name__ == "__main__":
    # Create a library instance
    library = Library()

    # Create book instances
    b1 = Book("Brave New World", "Aldous Huxley")
    b2 = Book("1984", "George Orwell")

    # Add books to the library
    library.add_book(b1)
    library.add_book(b2)

    # Display available books after setup
    print("Available books after setup:")
    for book in library.list_available_books():
        print(book)

    # Check out a book
    print("\n" + library.check_out_book("1984"))
    print("Available books after checking out '1984':")
    for book in library.list_available_books():
        print(book)

    # Return the book
    print("\n" + library.return_book("1984"))
    print("Available books after returning '1984':")
    for book in library.list_available_books():
        print(book)
