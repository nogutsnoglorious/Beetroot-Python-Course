# Lesson 10 Homework; Task 2
# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given
# by the input function were not numbers, and if value b was zero (cannot divide by zero).    


number_1 = input("Please enter 1st number: ")
number_2 = input("Please enter 2nd number: ")

def calc_func(a,b):
    return a**2 / b

try:
    result = calc_func(int(number_1), int(number_2))
    print('Here is the result of division: {}.'.format(result))
except ZeroDivisionError:
    print('Please, avoid zero.')
except ValueError:
    print('One of input values is not a number.')