from Moodel.book_file import BookMoodel
from View import constat


class BookControll:
    def __init__(self):
        self.__Author_li = []
        self.__Book_li = []

    def add_book(self, title: str, description: str, author_id, status: str):
        if not constat.ProjectUt.validate_empty_data(title, description, author_id, status):
            return "Invalied(Space in Data)"

        if not self.__validate_nums_data(status):
            return "Invalid (input number)"

        new_librarian = BookMoodel(title, description, author_id, int(status))
        self.__Book_li.append(new_librarian)

    def __validate_nums_data(self, *data: str) -> bool:
        for item in data:
            if not item.isdigit():
                return False
        return True

    def get_book_count(self):
        return len(self.__Book_li)

    def print_book(self, id):
        for book in self.__Book_li:
            if book.id == id:
                print("booh id: ", book.id)
                print("book title: ", book.title)
                print("book description: ", book.description)
                print("book status: ", book.status)
                for author in self.__Author_li:
                    if author.id == book.id:
                        print("book author: ", author.full_name)
                        return

                return
        print("Book with id: ", id, "is not found")

    def print_books(self):
        for book in self.__Book_li:
            print("book id: ", book.id)
            print("book title: ", book.title)
            print("book description: ", book.description)
            print("book status: ", book.status)
            for author in self.__Author_li:
                if author.id == book.id:
                    print("book author: ", author.full_name)
                    break

            print("-------------------------------------------")