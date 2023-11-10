import random
my_list = []
i = 0
x = 0
while i < random.randint(1,20):
    x = random.randint(1,100)
    my_list.append(x)
    i += 1
sum_all = 0
for el in my_list:
    sum_all = sum_all + el
print(my_list)
print(sum_all)


