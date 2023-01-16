from Moodel.personal_ditals import ParentMoodel


class AuthorMoodle(ParentMoodel):

    __author_id = 0
    def __init__(self, full_name: str, age: int, email: str):
        AuthorMoodle.__author_id += 1
        self.id = AuthorMoodle.__author_id
        super(AuthorMoodle, self).__init__(full_name, age)
        self.email = email
