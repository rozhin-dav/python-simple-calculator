# Project: Simple Calculator
# Version: 1.0
# Author: Rozhin

def show_title():
    print("====== Simple Calculator ======")


def get_numbers():
    a = int(input("Give me the first number: "))
    b = int(input("Give me the second number: "))
    return a, b


def get_operation():
    operation = input("Enter the operation (+, -, *, /): ")
    return operation


def calculate(a, b, operation):

    if operation == "+":
        print("Result:", a + b)

    elif operation == "-":
        print("Result:", a - b)

    elif operation == "*":
        print("Result:", a * b)

    elif operation == "/":
        if b == 0:
            print("You can't divide by zero.")
        else:
            print("Result:", a / b)

    else:
        print("Invalid operation")


while True:

    show_title()

    a, b = get_numbers()

    operation = get_operation()

    calculate(a, b, operation)

    again = input("Do you want another calculation? (yes/no): ")

    if again.lower() != "yes":
        break

print("Thanks for using my calculator!")
