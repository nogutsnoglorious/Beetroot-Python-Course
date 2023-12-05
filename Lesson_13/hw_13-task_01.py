# Lesson 13 Homework; Task 1
# Write a Python program to detect the number of local variables declared in a function.

# ------------------------------------------------------------------------------

# неправильно зрозумів задачу і підрахував кількість аргументів

# import random

# def define_loc_var(*args):
#     answer = 0
#     for arg in args:
#         answer += 1
#     return answer

# new_list = [random.randint(1,100) for i in range(random.randint(3,50))]

# print('List values:', new_list)
# print('Total arguments in list is:', define_loc_var(*new_list))

# ------------------------------------------------------------------------------

# дізнався про існування вбудованої функції locals()

def calc_local_vars():
    a = "One"
    b = 2
    c = True
    d = list()
    e = dict()
    f = tuple()
    g = None

    vars_quantity = len(locals())
    print("Quantity of locally defined variables is:", vars_quantity)

calc_local_vars()