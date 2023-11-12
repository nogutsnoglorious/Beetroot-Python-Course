# Lesson 6 Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random

number_list = []
i = 0
while i < 11:
    x = random.randint(1, 1001)
    number_list.append(x)
    i += 1

print('Final number list is: {}.'.format(number_list))
number_list.sort()
print('Highest number in this list is {}.'.format(number_list[-1]))
