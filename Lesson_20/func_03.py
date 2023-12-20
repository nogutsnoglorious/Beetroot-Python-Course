# 3. Напишіть функцію, яка приймає список чисел і повертає найбільше з них.

from random import randint

num_list_pos = [randint(1,100) for x in range(randint(5,10))]
num_list_neg = [randint(-100,0) for y in range(randint(5,10))]

def biggest_num(list_):
    list_.sort()
    return list_[-1]
    
