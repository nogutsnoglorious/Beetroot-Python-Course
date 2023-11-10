"""name1 = "Jerry"
dishes_list1 = ("soup", "steak", "fries")
dishes_qty = len(dishes_list1)
order1 = (name1, dishes_list1, dishes_qty)
general_list = list()
general_list.append(order1)
print(order1)

name2 = input("Enter your name: ")
dishes_list2 = list()
exit = 0
while exit == 0:
    dish2 = input("Enter your desired dish(es): ")
    if dish2 != "":
        dishes_list2.append(dish2)
    else:
        exit = ""
order2 = (name2, dishes_list2, len(dishes_list2))

general_list.append(order2)
print(general_list)

"""

# fully working version

order_list = []
while True:
    name = input("What's your name: ")
    dish_list = []
    while True:
        dish = input("Enter a name of desired dish: ")
        if dish != "":
            dish_list.append(dish)
        else:
            break
    order_list.append([name, dish_list, len(dish_list)])
    question = input("Would you like to create an order for other person (y/n): ").lower()
    if question == "y":
        continue
    else:
        break
edit_list = order_list.copy()
while True:
    edit = input("Do you want to delete some order (y/n?: ").lower()
    if edit == "y":
        whom = int(input("Please, name an number of person who's order you want to delete: ")) - 1
        edit_list.pop(whom)
        continue
    else:
        break
print("Here's full list of orders: ", order_list)
print("Here's list of orders after edit: ", edit_list)