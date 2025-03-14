from user import User
from datetime import datetime, timedelta

class Member(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(name, email, password)
        self.__user_id = user_id  
        self.__borrowed_books = []
        self.__reserved_books = []


    def get_email(self):
        return self._email  

    def check_password(self, password):
        return self._password == password  # Check password securely

    def borrow_book(self, book):
        if len(self.__borrowed_books) < 5 and book.get_status() == "Available":
            book.update_status("Borrowed")
            book.set_due_date(datetime.now() + timedelta(days=14))
            self.__borrowed_books.append(book)
            return f"{book.get_title()} borrowed successfully!"
        return "Cannot borrow book. Limit reached or book unavailable."

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.update_status("Available")
            book.set_due_date(None)
            self.__borrowed_books.remove(book)
            return f"{book.get_title()} returned successfully!"
        return "Book not found in borrowed list."

    def reserve_book(self, book):
        if book.get_status() == "Borrowed" and book not in self.__reserved_books:
            self.__reserved_books.append(book)
            return f"{book.get_title()} reserved successfully!"
        return "Cannot reserve this book."
