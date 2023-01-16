from Moodel.personal_ditals import ParentMoodel


class ClientMoodel(ParentMoodel):

    __client_id = 0
    def __init__(self, full_name: str, age: int, id_num: int, phone: int):
        super(ClientMoodel, self).__init__(full_name, age)
        ClientMoodel.__client_id += 1
        self.id = ClientMoodel.__client_id
        self.id_num = id_num
        self.phone = phone
