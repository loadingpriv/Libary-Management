from user import User

class Administrator(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.borrowing_limit = 5
        self.late_fee = 1.0  

    def register_member(self, library, user_id, name, email, password):
        return library.register_member(user_id, name, email, password)

    def register_librarian(self, library, user_id, name, email, password):
        return library.register_librarian(user_id, name, email, password)

    def set_library_rules(self, borrowing_limit= 5 , late_fee = None):
        if borrowing_limit is not 5:
            self.borrowing_limit = borrowing_limit
        if late_fee is not None:
            self.late_fee = late_fee
        return f"Library rules updated: Borrowing Limit = {self.borrowing_limit}, Late Fee = £{self.late_fee}/day"

    def get_library_rules(self):
        return f"Current Rules - Borrowing Limit: {self.borrowing_limit}, Late Fee: £{self.late_fee}/day"