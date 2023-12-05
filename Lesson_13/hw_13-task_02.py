# Lesson 13 Homework; Task 2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

import random

num_list = [random.randint(1,50) for i in range(random.randint(3,10))]

def to_pow_of(*args):
    sqr_list = [arg ** 2 for arg in args]
    return sqr_list

def access_function(func, *args):
    return func(*args)

print(access_function(to_pow_of, *num_list))



