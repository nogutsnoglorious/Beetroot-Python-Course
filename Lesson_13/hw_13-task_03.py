# Lesson 13 Homework; Task 3
# Write a function called "choose_func" which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one.

import random

def choose_func(*args, func1, func2):
    positive = True
    for arg in args:
        if arg > 0:
            continue
        else:
            positive = False
    if positive == True:
        print("All numbers in list are positive, so we are running func1.")
        return func1(*args)
    else:
        print("Negative numbers are detected. func2 will be executed.")
        return func2(*args)

def sqr_nums(*args):
    sqr_num_list = [arg ** 2 for arg in args]
    return sqr_num_list

def mult_by_3(*args):
    mult_by_3_list = [arg * 3 for arg in args]
    return mult_by_3_list

rand_num_list = [random.randint(-10,100) for i in range(random.randint(5,10))]

print("Random number list is:", rand_num_list)

print(choose_func(*rand_num_list, func1=sqr_nums, func2=mult_by_3))
