# Lesson 14 Classwork; Task 1, 2, 3
# 1. Спробуйте модифікувати попередній приклад, додавши якийсь свій функціонал
# 2. Напишіть декоратор, який виводить час виконання функції.
# 3. Створіть декоратор, який перевіряє аргументи, передані у функцію, і виводить повідомлення
#    про помилку, якщо аргументи не задовольняють певні умови.

from functools import wraps
import time

# ----------------------------------------------

# Task 0 Testing with numbers

# def calc_decorator(func):
#     @wraps(func)
#     def wrapper(x,y):
#         result = 0
#         if x<y:
#             result = add_num(x,y)
#             return result
#         elif x>y:
#             result = subtract_num(x,y)
#             return result
#     return wrapper


# @calc_decorator
# def count_num(x,y):
#     return x,y

# def add_num(x,y):
#     return x+y

# def subtract_num(x,y):
#     return x-y

# print(count_num(12,9))

# ----------------------------------------------

# Task 1

# def cond_decorator(func):
#     @wraps(func)
#     def wrapper():
#         if len(func()) > 20:
#             return func().title()
#         elif len(func()) <= 20:
#             return func().replace(" ", " (-----) ")
#     return wrapper


# @cond_decorator
# def say_hi():
#     "This will say hi"
#     return 'hello there how are'

# print(say_hi())

# ----------------------------------------------

# Task 2

# def new_decorator(func):
#     @wraps(func)
#     def wrapper():
#         start = time.perf_counter()
#         result = func().replace("e", "3")
#         end = time.perf_counter()
#         print(func.__name__, "took", ((end - start) * 1000), "ms to complete.")
#         return result
#     return wrapper


# @new_decorator
# def say_hi():
#     "This will say hi"
#     return 'hello there how are'

# print(say_hi())

# ----------------------------------------------

# Task 3

def error_decorator(func):
    @wraps(func)
    def wrapper(x,y):
        result = func(x,y)
        output = x + " " + y
        if y == 'word':
            raise SyntaxError("You have a mistake!")
        else: 
            return output
    return wrapper


@error_decorator
def say_hi(x,y):
    return x,y

print(say_hi('hello', 'word'))