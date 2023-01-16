
class BorrowingMoodel:
    __borrowing_id = 0
    def __init__(self, date: str, client_id, book_id, status: int):
        BorrowingMoodel.__borrowing_id += 1
        self.id = BorrowingMoodel.__borrowing_id
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.status = status
