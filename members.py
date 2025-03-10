from user import User


class member(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.__borrowed_book = []
        self.__returned_book= []