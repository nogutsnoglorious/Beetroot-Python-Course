age = int(input("How old are you: "))
income = int(input("What's your annual income: "))
job = input("Do you have a job (yes/no): ").lower()
refuse = "Sorry, you're not eligible for a credit."

if age >= 18 and age <= 60:
    if income >= 50000:
        if job == "yes":
            credit = int(input("Congrats! You're eliginle for a credit. Enter a desired amount: "))
            if credit > 100000:
                    answer = input("Sorry! Available credit maximum is only 100000, would you like to get it? ").lower()
                    if answer == "yes":
                        tel = input("Congrats! Enter your contact number for further details: ")
                        print(f'You will be contacted via {tel} within a few days.')
                    elif answer == "no":
                        print("We are sorry to hear that. Bye!")
            elif credit < 100000:
                tel = input("Congrats! Enter your contact number for further details: ")
                print(f'You will be contacted via {tel} within a few days.')
        elif job == "no":
            print(refuse)
    else:
         print(refuse)
else:
     print(refuse)








"""
answer = input("Sorry! Available credit maximum is only 100000, would you like to get it? ").lower()
                    if answer == "yes":
                        tel = input("Congrats! Enter your contact number for further details: ")
                    elif answer == "no":
                        print("We are sorry to hear that. Bye!")
                    else:
                        input('Give us please only "yes" or "no": ')
"""