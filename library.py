from book import Book
from members import Member
from librarian import Librarian
from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.__book_list = []
        self.__member_list = []
        self.__librarian_list = []

    def add_book(self, book):
        self.__book_list.append(book)

    def remove_book(self, book):
        if book in self.__book_list:
            self.__book_list.remove(book)
            return True
        return False

    def register_member(self, user_id, name, email, password):
        new_member = Member(user_id, name, email, password)
        self.__member_list.append(new_member)
        return f"Member '{name}' registered successfully!"

    def add_librarian(self, user_id, name, email, password):
        new_librarian = Librarian(user_id, name, email, password)
        self.__librarian_list.append(new_librarian)
        return f"Librarian '{name}' added successfully!"

    def get_books(self):
        return self.__book_list

    def list_overdue_books(self):
        return [book.get_title() for book in self.__book_list if book.get_due_date() and book.get_due_date() < datetime.now()]