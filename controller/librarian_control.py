from Moodel.librarian_file import LibrarianMoodel
from View import constat


class LibrarianControll:
    def __init__(self):
        self.__Librarian_li = []

    def add_librarian(self, full_name: str, age: str, id_num: str, emp_type: str):
        if not constat.ProjectUt.validate_empty_data(full_name, age, id_num, emp_type):
            return "Invalied(Space in Data)"

        if not self.__validate_nums_data(age, id_num, emp_type):
            return "Invalid (input number)"

        new_librarian = LibrarianMoodel(full_name, int(age), int(id_num), int(emp_type))
        self.__Librarian_li.append(new_librarian)

    def __validate_nums_data(self, *data: str) -> bool:
        for item in data:
            if not item.isdigit():
                return False
        return True

    def get_librarian_count(self):
        return len(self.__Librarian_li)

    def print_librarian(self, id):
        for librarian in self.__Librarian_li:
            if librarian.id == id:
                print("librarian name: ", librarian.id,
                      "librarian name: ", librarian.full_name,
                      "librarian age: ", librarian.age,
                      "librarian id num: ", librarian.id_num,
                      "librarian emp_type: ", librarian.emp_type)
                return
            print("Librarian with id: ", id, "is not found")

    def print_librarians(self):
        for librarian in self.__Librarian_li:
            print("librarian name: ", librarian.id,
                  "librarian name: ", librarian.full_name,
                  "librarian age: ", librarian.age,
                  "librarian id num: ", librarian.id_num,
                  "librarian emp_type: ", librarian.emp_type)
            print("-------------------------------------------")
