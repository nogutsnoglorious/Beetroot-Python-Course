address_book = []
while True:
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    address_book.append([name, phone])
    answer = input("Do you wish to enter new user (y/n?): ").lower()
    if answer == "y":
        continue
    else:
        break
new_ab = address_book.copy()
while True:
    print("Here's all the data from your address book: ", new_ab)
    edit = input("Do you want to delete some contact (y/n)?: ").lower()
    if edit == "y":
        whom = int(input("Enter a number of a contact you want to delete: ")) - 1
        new_ab.pop(whom)
        continue
    else:
        break

print("Here's all the data from original address book: ", address_book)
print("Here's all the data from edited address book: ", new_ab)


"""
address_book = list()
user = list()
while True:
    if user != "":
        address_book.extend(user)
    while True:
        name = input("Enter your name: ")
        user.insert(0, name)
        phone = input("Enter your phone number: ")
        user.insert(1, phone)
        break
    answer = input("Do you wish to enter new user? ")
    if answer != "":
        continue
    else:
        break    
print("Here's all the data from your address book: ", address_book)
"""