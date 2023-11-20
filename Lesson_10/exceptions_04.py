# Lesson 10 Classwork; Task 4
# (optional) Напишіть функцію, яка приймає два аргументи і виконує ділення першого на друге.
# Використайте блок try-except, щоб вивести повідомлення про помилку, якщо дільник рівний нулю

import random

def division(x,y):
    try:
        result = int(x) / int(y)
        print(result)
    except ZeroDivisionError:
        print("Error! Entered number must not be zero.")

a = random.randint(1,100)
b = input("Enter any number: ")

division(a,b)