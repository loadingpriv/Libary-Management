from book import Book
from members import Member
from librarian import Librarian
from admin import Administrator  
from datetime import datetime

class Library:
    def __init__(self):
        self.__members = []
        self.__librarians = []
        self.__books = []
        self.__current_user = None

    def register_member(self):
        user_id = len(self.__members) + 1
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if any(m.get_email() == email for m in self.__members):
            print("Email already registered.")
            return

        new_member = Member(user_id, name, email, password)
        self.__members.append(new_member)
        print(f"Member registration successful! Your user ID is: {user_id}")

    def register_librarian(self):
        if not isinstance(self.__current_user, Administrator):
            print("Only an administrator can register librarians!")
            return

        user_id = len(self.__librarians) + 1
        name = input("Enter librarian name: ")
        email = input("Enter librarian email: ")
        password = input("Enter librarian password: ")

        if any(l.get_email() == email for l in self.__librarians):
            print("Email already registered.")
            return

        new_librarian = Librarian(user_id, name, email, password)
        self.__librarians.append(new_librarian)
        print(f"Librarian registration successful! Librarian ID: {user_id}")

    def login(self):
        print("\nChoose user type to log in:")
        print("1. Member")
        print("2. Librarian")
        print("3. Admin")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_list = self.__members
        elif choice == "2":
            user_list = self.__librarians
        elif choice == "3":
            email = input("Enter admin email: ")
            password = input("Enter password: ")
            if email == "admin@library.com" and password == "admin123":
                self.__current_user = "Admin"
                print("\nLogin successful! Welcome, Admin.")
                return
            else:
                print("Invalid Admin credentials.")
                return
        else:
            print("Invalid choice.")
            return

        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in user_list:
            if user.get_email() == email and user.check_password(password):
                self.__current_user = user
                print(f"\nLogin successful! Welcome, {user.get_name()}.")
                return

        print("Invalid credentials.")

    def logout(self):
        if self.__current_user:
            print(f"Goodbye, {self.__current_user.get_name()}!")
            self.__current_user = None

    def get_current_user(self):
        return self.__current_user

    
    def get_members(self):
        return self.__members

    def get_librarians(self):
        return self.__librarians
    
    def list_overdue_books(self):
        overdue_books = [book for book in self.__books if book.get_status() == "Borrowed" and book.get_due_date() and book.get_due_date() < datetime.now()]
        
        if overdue_books:
            print("\nOverdue Books Report:")
            for book in overdue_books:
                print(f"Title: {book.get_title()}, Borrowed Until: {book.get_due_date().strftime('%Y-%m-%d')}")
        else:
            print("No overdue books.")

    def list_books(self):
        """Displays all books in the library with their status."""
        if not self.__books:
            print("No books available in the library.")
            return

