# 3. Напишіть функцію, яка приймає список чисел і повертає найбільше з них.

def biggest_num(x):
    x.sort()
    print("{} is your highest number on your list.".format(x[-1]))

num_list = []
while True:
    num = input("Enter any number: ")
    if num == "":
        break
    elif num.isdigit() == False:
        print("This is not a number")
        continue
    else:
        num_list.append(int(num))
    

print("This is your numbers list: ", num_list)
biggest_num(x=num_list)


# чому не працюють варіанти нижче

# big_num = biggest_num(num_list)
# print(f'The highest number in your list is {big_num}.')
# print(f'The highest number in your list is {biggest_num(num_list)}.')
# print("{} is your highest number in the list".format(biggest_num))
