while True:
    number = input("Enter any integer number: ")

    def check_number():
        print(int(number) % 2 == 0)

    if number == "":
        break
    elif number.isdigit() == False:
        print("This is not a number!")
        continue
    else:
        check_number()