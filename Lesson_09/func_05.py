# 2. Система обліку запасів:
# Створіть функцію, яка дозволяє додавати товари до системи обліку запасів,
# відстежує кількість товарів та повертає інформацію про наявність товарів на складі.

item_list = []
while True:
    item = input("Enter new item: ")
    if item == "":
        break
    elif item.isdigit():
        print("Enter only characters.")
        continue
    else:
        item_list.append(item.lower())


def warehouse(x):
    print('This is items list of warehouse with total number of {} positions: {}'.format(len(x),x))
    
    new_list = []
    while True:
        q1 = input("Do you want to add new items? ")
        if q1 != "":
            new_item = input("Enter new item: ")
            new_list.append(new_item.lower())      # чи можна якось змусити програму вважати, що змінна Х буде листом?
        else:
            break
    new_list.extend(x)               # чи можна до ліста Х додати new_list?
    
    print('This is updated items list of warehouse with total number of {} positions: {}'.format(len(new_list),new_list))

    while True:
        q2 = input("Do you want to check the product availabity in the warehouse? ")
        if q2 != "":
            search_item = input("Please, enter the name of an item you're looking for: ").lower()
            check = 0
            for el in range(len(new_list)+1):
                if search_item != new_list[el]:
                    continue
                else:
                    check += 1
                    print(f'Great! The item is available and its number in the list is {el+1}.')
                    break
            if check == 0:
                print('There is no such item in the list.')
            else:
                continue
        else:
            break
    
    print("Thanks, bye!")

warehouse(item_list)