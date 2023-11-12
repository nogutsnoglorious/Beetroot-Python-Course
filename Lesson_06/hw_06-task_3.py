# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

import random

number_list = []
i = 1
while i < 101:
    number_list.append(i)
    i += 1

filter_list = []
x = 1
while x < len(number_list):
    if x % 7 == 0 and x % 5 != 0:
        filter_list.append(x)
        x += 1
    else:
        x += 1
    
print('Main list looks like this:\n{}.'.format(number_list))
print('\nA list of numbers from the main list that are divisible by 7 but not a multiple of 5 is:\n{}.'.format(filter_list))