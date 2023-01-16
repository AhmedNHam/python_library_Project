from Moodel.borrowing_order import BorrowingMoodel


class BorrowingOrderControl:
    def __init__(self):
        self.__order_li = []

    def add_order(self, date: str, client_id, book_id, status: str):

        new_order = BorrowingMoodel(date, client_id, book_id, status)
        self.__order_li.append(new_order)

    def get_order_count(self):
        return len(self.__order_li)


    def print_orders(self):
        for order in self.__order_li:
            print("client id: ", order.id,
                  "client name: ", order.date,
                  "client age: ", order.client_id,
                  "client id num: ",  order.book_id,
                  "client phone: ",  order.status)
            print("-------------------------------------------")