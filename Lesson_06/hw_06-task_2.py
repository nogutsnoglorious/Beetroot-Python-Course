# Lesson 6 Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random

number_list_1 = []
number_list_2 = []
i = 0
while i < 11:
    x = random.randint(1, 10)
    number_list_1.append(x)
    y = random.randint(1, 10)
    number_list_2.append(y)
    i += 1

number_list_3 = list(set(number_list_1).intersection(set(number_list_2)))
number_list_3.sort()

print('First number list is: {}.'.format(number_list_1))
print('Second number list is: {}.'.format(number_list_2))
print('Common values in both lists are: {}'.format(number_list_3))