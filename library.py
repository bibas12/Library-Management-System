# module for library
class library:
    def __init__(self, count_book, name):
        self.count_book_dict = count_book
        self.name = name
        self.bookdict = {}
        self.max_book_count = {}
        self.count_book_dict
        
    def display_books(self):
#  Display deatils about the book available in the library 
        for books in self.count_book_dict.items():
            print(books)
