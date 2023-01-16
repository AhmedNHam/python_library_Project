from Moodel.clinet_file import ClientMoodel
from View import constat


class ClientControll:
    def __init__(self):
        self.__Client_li = []

    def add_client(self, full_name: str, age: str, id_num: str, phone: str):
        if not constat.ProjectUt.validate_empty_data(full_name, age, id_num, phone):
            return "Invalied(Space in Data)"

        if not self.__validate_nums_data(age, id_num, phone):
            return "Invalid (input number)"

        new_student = ClientMoodel(full_name, int(age), int(id_num), int(phone))
        self.__Client_li.append(new_student)

    def __validate_nums_data(self, *data: str) -> bool:
        for item in data:
            if not item.isdigit():
                return False
        return True

    def get_client_count(self):
        return len(self.__Client_li)


    def print_clients(self):
        for client in self.__Client_li:
            print("client id: ", client.id,
                  "client name: ", client.full_name,
                  "client age: ", client.age,
                  "client id num: ",  client.id_num,
                  "client phone: ",  client.phone)
            print("-------------------------------------------")