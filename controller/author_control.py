from Moodel.author_file import AuthorMoodle
from View import constat


class AuthorControll:
    def __init__(self):
        self.__Book_li = []
        self.__Author_li = []

    def add_author(self, full_name: str, age: str, email: str):
        if not constat.ProjectUt.validate_empty_data(full_name, age, email):
            return "Invalied(Space in Data)"

        if not self.__validate_nums_data(age):
            return "Invalid (input number)"

        new_author = AuthorMoodle(full_name, email, int(age))
        self.__Author_li.append(new_author)

    def __validate_nums_data(self, *data: str) -> bool:
        for item in data:
            if not item.isdigit():
                return False
        return True

    def get_author_count(self):
        return len(self.__Author_li)

    def print_author(self, id):
        for author in self.__Author_li:
            if author.id == id:
                print("Author id: ", author.id,
                      "Author name: ", author.full_name,
                      "Author age: ", author.age,
                      "Author email: ",  author.email)
                return
            print("Author with id: ", id, "is not found")

    def print_authors(self):
        for author in self.__Author_li:
            print("Author id: ", author.id,
                  "Author name: ", author.full_name,
                  "Author age: ", author.age,
                  "Author email: ",  author.email)
            print("-------------------------------------------")

    def print_authors_books(self, id):
        is_author_exist = False
        author_name = ""
        for author in self.__Author_li:
            if author.id == id:
                is_author_exist = True
                author_name = author.full_name
                break
        if is_author_exist == False:
            print("author with id: ", id, "is not found")
            return

        print("books of author ", author_name, ": ")
        for book in self.__Book_li:
            if book.author_id == id:
                print("Tittel: ", book.title)
