confirmed_number = "" 
while confirmed_number == "":
    phone_number = input("Please, enter your phone number in XXXXXXXXXX format: ")
    if len(phone_number) == 10:
        if phone_number.isdigit():
            print(f'Your number {phone_number} has been successfully recorded. Thanks!')
            confirmed_number = phone_number
        else:
            print("Wrong phone number format.")
            continue                                         
    else:
        print("Your phone number should have 10 characters.") 