while True:
    phone_number = input("Please, enter your phone number in XXXXXXXXXX format: ")
    if phone_number == "":
        break
    elif len(phone_number) != 10:
        print("Your phone number should have 10 characters.")
        continue 
    else:
        if phone_number.isdigit():
            print(f'Your number {phone_number} has been successfully recorded. Thanks!')
            break
        else:
            print("Wrong phone number format.")
            continue