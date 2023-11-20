# Lesson 10 Classwork; Task 3
# Спробуйте отримати доступ до елементу списку за індексом, який перевищує розмір списку.
# Використайте блок try-except, щоб відловити виняток і вивести повідомлення про помилку.

import random

new_list = []
y = random.randint(5,13)
for i in range(1,y):
    x = random.randint(1,100)
    new_list.append(x)
print(new_list)
try:
    print(new_list[len(new_list)+2])
except IndexError:
    print("List index is out of range.")