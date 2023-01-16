from Moodel.personal_ditals import ParentMoodel
from View.constat import Part, Full


class LibrarianMoodel(ParentMoodel):
    __librarian_id = 0
    def __init__(self, full_name: str, age: int, id_num: int, emp_type: int):
        LibrarianMoodel.__librarian_id += 1
        self.id = LibrarianMoodel.__librarian_id
        super(LibrarianMoodel, self).__init__(full_name, age)
        self.id_num = id_num
        self.emp_type = Full if emp_type == 1 else Part
