from book import Book
from member import Member
from staff import StaffMember

def main():
    library_inventory = []

    staff_user = StaffMember("Ahmed", "M100", "S55")
    print(f"--- Staff Created: {staff_user.name} (Staff ID: {staff_user.staff_id}) ---\n")

    book1 = Book("Python OOP", "John Doe", "123-456-789")
    book2 = Book("Data Structures", "Jane Smith", "987-654-321")
    
    staff_user.add_book(library_inventory, book1)
    staff_user.add_book(library_inventory, book2)
    print()

    print("--- Current Library Inventory ---")
    for book in library_inventory:
        book.display_info()
    print()

    regular_member = Member("Omar", "M202")
    print(f"--- Regular Member Created: {regular_member.name} ---\n")

    regular_member.borrow_book(book1)
    
    regular_member.borrow_book(book1)
    print()

    print("--- Inventory After Borrowing ---")
    book1.display_info()
    print()

    regular_member.return_book(book1)
    print()

    print("--- Inventory After Returning ---")
    book1.display_info()

if __name__ == "__main__":
    main()