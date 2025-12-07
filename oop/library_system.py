class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
    def __str__(self):
        return "Book"

class EBook(Book):
    def __init__(self, title, author, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return "EBook"

class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return "PrintBook"
    
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book:Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            
            if str(book) == "Book":
                print(f"Book: {book.title} by {book.author}")
            elif str(book) == "EBook":
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif str(book) == "PrintBook":
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print("Book type not found.")

            """match str(book):
                case "Book":
                    print(f"Book: {book.title} by {book.author}")
                case "EBook":
                    print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}")
                case "PrintBook":
                    print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
                case _:
                    print("Book type not found.")"""