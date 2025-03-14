from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, status="Available"):
        self.__title = title
        self.__author = author
        self.__status = status
        self.__due_date = None

    def get_title(self):
        return self.__title

    def get_status(self):
        return self.__status

    def update_status(self, status):
        self.__status = status

    def set_due_date(self, due_date):
        self.__due_date = due_date
