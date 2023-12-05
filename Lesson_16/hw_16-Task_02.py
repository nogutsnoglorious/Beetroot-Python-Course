# Lesson 16 Homework; Task 2
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# - square_nums (takes a list of integers and returns the list of squares)
# - remove_positives (takes a list of integers and returns it without positive numbers
# - filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

import random, calendar

class Mathematician:
    def __init__(self) -> None:
        pass

    def square_nums(*args):
        square_nums_list = [arg ** 2 for arg in args]
        return square_nums_list

    def remove_positives(*args):
        positives_only = [arg for arg in args if arg >0]
        return positives_only
    
    def filter_leaps(*args):
        leaps_only = [arg for arg in args if calendar.isleap(arg)]
        return leaps_only


list_for_squares = [random.randint(1, 50) for i in range(random.randint(3,10))]
list_leave_positives = [random.randint(-50, 50) for i in range(random.randint(3,10))]
list_years_list = [random.randint(0, 2050) for i in range(random.randint(5,20))]

print(list_for_squares)                                                         # original list for squares
print(Mathematician.square_nums(*list_for_squares),"\n")                        # edited list for squares
print(list_leave_positives)                                                     # original list for positives and negatives 
print(Mathematician.remove_positives(*list_leave_positives),"\n")               # edited list with positives only
print(list_years_list)                                                          # original list with year values
print(Mathematician.filter_leaps(*list_years_list),"\n")                        # edited list with leap years only

