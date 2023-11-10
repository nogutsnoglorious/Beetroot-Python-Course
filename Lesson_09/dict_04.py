print("Let's create first name dictionary!")
name_dict_1 = dict()
while True:
    name = input("Enter person's name: ")
    age = input("Enter person's age: ")
    if name == "" or age == "":
        break
    else:
        name_dict_1.update({name: int(age)})
print(name_dict_1)

print("Well done! Let's create second name dictionary!")
name_dict_2 = dict()
while True:
    name = input("Enter person's name: ")
    age = input("Enter person's age: ")
    if name == "" or age == "":
        break
    else:
        name_dict_2.update({name: int(age)})
print(name_dict_2)

print("Great!")

while True:
    q1 = input("Do you want to search for person's age? ")
    if q1 !=  "":
        while True:
            q2 = input("Enter number of the list you're interested in: ")
            print(q2)
            if q2 == "":
                break
            elif int(q2) == 1:
                q3 = input("Enter person's name: ")
                print(f'{q3} age is {name_dict_1.get(q3)}.')
                continue
            elif int(q2) == 2:
                q3 = input("Enter person's name: ")
                print(f'{q3} age is {name_dict_2.get(q3)}.')
                continue
            else:
                print("Sorry, I didn't understand. Let's try once again.")
                continue
    else:
        break

name_dict_3 = dict()
name_dict_3.update(name_dict_1)
name_dict_3.update(name_dict_2)
print(f'Heres a result of merging of 2 dictionaries!: {name_dict_3}')