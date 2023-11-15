# Lesson 9 Classwork; Task 1
# 1. Напишіть функцію, яка приймає будь-яку кількість аргументів та повертає їхню суму.

def args_sum(*args):
    x = 0
    for i in args:
        x += i
    return (x)

print(args_sum(1,4,6,4,2,7,454,3,1000))