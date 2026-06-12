class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn  
        self.available = True

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title} | Author: {self.author} | ISBN: {self.__isbn} | Status: {status}")