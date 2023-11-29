# Lesson 13 Classwork; Task 6
# Напишіть функцію calculator, яка приймає два числа і функцію операції (додавання, віднімання, множення, ділення)
# і повертає результат цієї операції.

def add(x,y):
    return x+y

def subtr(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

def calculator(func,x,y):
    result = func(x,y)
    print(round(result,2))

calculator(div,123,98)