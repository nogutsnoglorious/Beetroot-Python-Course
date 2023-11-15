# Lesson 8 Homework; Task 3
# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator
# as a first parameter (to keep things simple let it only be '+', '-' or '*') and an arbitrary
# number of arguments (only numbers) as the second parameter. Then return the sum or product of
# all the numbers in the arbitrary parameter.

def make_operation(oper, *args):
    result = 0
    if oper == "-":
        for i in args:
            result -= i
        print("You chose subtraction. The result of this operation among all input number is", result)
    elif oper == "+":
        for i in args:
            result += i
        print("You chose addition. The result of this operation among all input number is", result)
    elif oper == "*":
        result = 1
        for i in args:
            result *= i
        print("You chose multiplication. The result of this operation among all input number is", result)


operation = input("Please, enter an operator for mathematical operation (+, - or * are only possible)")
numbers_list = []
while True:
    number = input("Please, enter any number: ")
    if number == "":
        break
    else:
        numbers_list.append(int(number))

make_operation(operation,*numbers_list)
