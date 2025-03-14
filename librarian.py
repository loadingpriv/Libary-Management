from user import User
from datetime import datetime

class Librarian(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(name, email, password)
        self.__user_id = user_id

    def get_email(self):
        return self._User__email

    def check_password(self, password):
        return self._User__password == password

    def add_book(self, library, book):
        library.add_book(book)
        return f"Book '{book.get_title()}' added."

    def remove_book(self, library, book):
        library.remove_book(book)
        return f"Book '{book.get_title()}' removed."
    
    def register_librarian(self):
        print("\n--- Librarian Registration ---")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if any(user.email == email for user in self.members):
            print("Email already registered. Try logging in.")
            return

        user_id = len(self.members) + 1
        new_librarian = Librarian(user_id, name, email, password)
        self.members.append(new_librarian)
        print(f"Registration successful! Librarian ID: {user_id}")
