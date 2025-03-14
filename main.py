import datetime
from library import Library
from librarian import Librarian
from admin import Administrator
from members import Member
from book import Book
from user import User



def main():
    library = Library()

    while True:
        if library.get_current_user():
            print("\n1. List Books\n2. Logout")
            if isinstance(library._Library__current_user, Librarian):
                print("3. Add Book\n4. Remove Book")
            choice = input("Choose: ")

            if choice == "1":
                library.list_books()
            elif choice == "2":
                library.logout()
            elif choice == "3" and isinstance(library._Library__current_user, Librarian):
                library.add_book()
            elif choice == "4" and isinstance(library._Library__current_user, Librarian):
                library.remove_book()
            else:
                print("Invalid choice.")
        else:
            print("\n--- Library Management System ---")
            print("1. Register as Member")
            print("2. Register as Librarian (Admin)")
            print("3. Login")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                library.register_member()
            elif choice == "2":
                library.register_librarian()
            elif choice == "3":
                library.login()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
