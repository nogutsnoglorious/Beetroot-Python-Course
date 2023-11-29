# Lesson 13 Classwork; Task 1
# Напишіть лямбда-функцію, яка приймає число і повертає його квадрат.

while True:
    input_number = input("Enter any number: ")
    if input_number == "":
        break
    else:
        square_func = lambda x : x**2
        result = square_func(int(input_number))
        print(result)