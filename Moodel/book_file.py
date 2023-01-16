from View.constat import Avilable, Unavilable


class BookMoodel:
    __book_id = 0
    def __init__(self, title: str, description: str, author_id, status: int):
        BookMoodel.__book_id += 1
        self.id = BookMoodel.__book_id
        self.title = title
        self.description = description
        self.author_id = author_id
        self.status = Avilable if status == 1 else Unavilable
