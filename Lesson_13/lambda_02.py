# Lesson 13 Classwork; Task 2
# Напишіть лямбда-функцію, яка приймає два аргументи (числа) і повертає їхню суму.

while True:
    input_x = input("Enter any number: ")
    input_y = input("Enter any number once again: ")
    if input_x == "" or input_y == "":
        break
    else:
        sum_func = lambda x,y : x+y
        result = sum_func(int(input_x),int(input_y))
        print(result)