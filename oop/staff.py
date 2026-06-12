from member import Member

class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library_list, new_book):
        library_list.append(new_book)
        print(f"[Staff: {self.name}] added a new book: '{new_book.title}' to the library.")