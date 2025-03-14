
class User:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self._password = password

    def get_email(self):
        return self.__email

    def check_password(self, password):
        return self.__password == password
    
    def get_name(self):
        return self.name


class Member(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(name, email, password)  # Ensure User class initializes correctly
        self.user_id = user_id
        self.__borrowed_books = []
        self.__returned_books = []
        self.__reserved_books = []
