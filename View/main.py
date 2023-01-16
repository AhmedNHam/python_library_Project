from controller.author_control import AuthorControll
from controller.book_control import BookControll
from controller.borrowing_order_control import BorrowingOrderControl
from controller.client_control import ClientControll
from controller.librarian_control import LibrarianControll

client_controller = ClientControll()
author_controller = AuthorControll()
librarian_controller = LibrarianControll()
book_controller = BookControll()
order_controller = BorrowingOrderControl()

def get_client_input():
    full_name = input("Welcome, please enter your full name: ")
    age = input("please enter your age: ")
    id_num = input("please enter your id Num: ")
    phone = input("please enter your phone: ")

    client_controller.add_client(full_name, age, id_num, phone)

def get_libririan_input():
    full_name = input("please enter libririan full name: ")
    age = input("please enter age: ")
    id_num = input("please enter id Num: ")
    emp_type = input("please enter emp_type: ")

    librarian_controller.add_librarian(full_name, age, id_num, emp_type)

def get_author_input():
    full_name = input("please enter author full name: ")
    age = input("please enter author age: ")
    email = input("please enter author email: ")

    author_controller.add_author(full_name, age, email)

def get_book_input():
    title = input("please enter book name: ")
    description = input("please enter book description: ")
    author_id = input("please enter author id: ")

    author_controller.add_author(title, description, author_id)

def get_order_input():
    date = input("please enter date: ")
    client_id = input("please enter client_id: ")
    book_id = input("please enter book_id: ")
    status = input("please enter status: ")

    order_controller.add_order(date, client_id, book_id, status)

print("1-join as client")
print("2-join as libririan")

user_input = input("Signin as: ")
if user_input == "1":
    print("welcome our client: ")
    print("1_print my old orders")
    print("2_Add New Order")
    print("3_Register New Client")
    user_input = input("enter your choice")
    if user_input == "1":
        print("Ahmed donot make this list yet")
    elif user_input == "2":
        get_order_input()
    elif user_input == "3":
        get_client_input()

elif user_input == "2":
    print("welcome our libririan: ")
    print("1_print orders")
    print("2_print avilable books")
    print("3_Register New book")
    print("4_Register New libririan")
    print("5_Register New author")
    print("6_print client list")
    print("7_print author list")
    print("8_print client count")
    print("9_print libririan count")
    print("10_print author count")
    print("11_print author books")


    user_input = input("your choice")
    if user_input == "1":
        order_controller.print_orders()

    elif user_input == "2":
        print("Ahmed donot make this list yet")

    elif user_input == "3":
        get_book_input()

    elif user_input == "4":
        get_libririan_input()

    elif user_input == "5":
        get_author_input()

    elif user_input == "6":
        client_controller.print_clients()

    elif user_input == "7":
        author_controller.print_authors()

    elif user_input == "8":
        print(client_controller.get_client_count())

    elif user_input == "9":
        print(librarian_controller.get_librarian_count())

    elif user_input == "10":
        print(author_controller.get_author_count())

    elif user_input == "11":
        print(author_controller.print_authors_books(id=input("enter author id: ")))

    else:
        exit()
