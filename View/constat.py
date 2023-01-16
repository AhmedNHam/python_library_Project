
Full = "full time"
Part = "part time"
Avilable = "avilable"
Unavilable = "unavilable"

class ProjectUt:
    @staticmethod
    def validate_empty_data(self, *data: str) -> bool:
        for item in data:
            if item.isspace():
                return False
        return True




# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# print("1_ +")
# print("2_ -")
# print("3_ *")
# print("4_ /")
# print("5_ ^")
# print("6_ %")
#
# operation = input("Enter the number or symbol for the operation you want to perform: ")
#
# if operation == "1" or operation == "+":
#   result = num1 + num2
# elif operation == "2" or operation == "-":
#   result = num1 - num2
# elif operation == "3" or operation == "*":
#   result = num1 * num2
# elif operation == "4" or operation == "/":
#   result = num1 / num2
# elif operation == "5" or operation == "^":
#   result = num1 ** num2
# elif operation == "6" or operation == "%":
#   result = num1 % num2
#
# print("Result:", result)
#
# print("1_ Normal rounding")
# print("2_ Take the number without")
# print("3_ Exit")
#
# output_option = input("Enter the number for the output option you want: ")
#
# if output_option == "1":
#   print("Rounded result:", round(result))
# elif output_option == "2":
#   print("Result without point:", int(result))
# elif output_option == "3":
#   exit()
#
# print("Thank you for using my program")


# numbers = []
#
# num1 = int(input("Enter a number: "))
# numbers.append(num1)
#
# num2 = int(input("Enter a number: "))
# numbers.append(num2)
#
# num3 = int(input("Enter a number: "))
# numbers.append(num3)
#
# num4 = int(input("Enter a number: "))
# numbers.append(num4)
#
# num5 = int(input("Enter a number: "))
# numbers.append(num5)
# print(numbers)
#
# numbers.sort()
# min = numbers[0]
# max = numbers[4]
#
# print("The largest value is", max)
# print("The smallest value is", min)
