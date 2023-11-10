print("Let's create items dict!")
items_dict = dict()
while True:
    name = input("Enter item's name: ")
    price = input("Enter items's price: ")
    if name == "" or price == "":
        break
    else:
        items_dict.update({name: int(price)})
print(f'This is items dict: {items_dict}')

