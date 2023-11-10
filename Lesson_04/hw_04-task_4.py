exit = False
while exit == False:
    name = 'Valentyn'
    enter_name = input("Enter your name: ")
    if name.lower() == enter_name.lower():
        print("True!")
        exit = True
    else:
        print("Wrong! Try again.")