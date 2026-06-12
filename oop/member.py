class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id  # Private attribute
        self.borrowed_books = []

    def get_membership_id(self):
        return self.__membership_id

    def set_membership_id(self, new_id):
        self.__membership_id = new_id

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"[{self.name}] successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"[{self.name}] successfully returned '{book.title}'.")
        else:
            print(f"[{self.name}] doesn't have '{book.title}' in their borrowed list.")