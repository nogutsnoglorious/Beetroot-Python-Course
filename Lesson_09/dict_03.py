item_dict = dict()
print("Let's create new items dictionary!")
while True:
    item_name = input("Enter item name: ")
    item_price = input("Enter item price: ")
    if item_name == "" or item_price == "":
        break
    else:
        item_dict.update({item_name: item_price})
print(item_dict)
while True:
    q1 = input("Do you want to search for items price? ")
    if q1 != "":
        q2 = input("Enter item name and get it's price: ")
        print(f'{q2} price is {item_dict.get(q2)}.')
    else:
        break
while True:
    q3 = input("Do you want to add new item? ")
    if q3 != "":
        item_name = input("Enter item name: ")
        item_price = input("Enter item price: ")
        if item_name == "" or item_price == "":
            break
        else:
            item_dict.update({item_name: item_price})
    else:
        break
print("Here's new items dictionary: ", item_dict)
print("Thanks, bye!")   