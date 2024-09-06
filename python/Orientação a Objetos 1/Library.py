# Global variables
#Usando POP
library = [] # Represents the library as a list of dictionaries
# Functions
def add_book(title, author):
    book = {'title': title, 'author': author}
    library.append(book)
    def list_books():
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}")
            # Main program
            add_book("The Great Gatsby", "F. Scott Fitzgerald")
            add_book("To Kill a Mockingbird", "Harper Lee")
            list_books()

#Usando OOP
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        class Library:
            def __init__(self):
                self.books = []
            def add_book(self, book):
                self.books.append(book)
            def list_books(self):
                for book in self.books:
                    print(f"Title: {book.title}, Author: {book.author}")
# Main program
                library = Library()
                book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
                book2 = Book("To Kill a Mockingbird", "Harper Lee")
                library.add_book(book1)
                library.add_book(book2)
                library.list_books()
