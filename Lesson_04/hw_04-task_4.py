name = 'Valentyn'
while True:
    enter_name = input("Enter your name: ")
    if name.lower() == enter_name.lower():
        print("True!")
        break
    else:
        print("Wrong! Try again.")