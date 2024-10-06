class Book:
    def __init__(self, title, author, is_checked_out):
        self.title = title
        self.author = author
        self.__is_checked_out = is_checked_out

class Library:
        def __init__(self):
             self._books = []
        def add_book(self, book):
             self._books.append(book)
        def check_out_book(self,title):
             for book in self._books:
                  if book.title == title:
                        book.checkout_book()
        def return_book(self,title):
             for book in self._books:
                  if book.title == title:
                       book.return_book()
        def list_available_books(self):
             for book in self._books:
                  if book.__is_checked_out == False:
                       print(f"{book.title} by {book.author}")