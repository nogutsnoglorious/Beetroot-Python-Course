age = int(input("How old are you?: "))
name = input('What do you want to buy? Enter "a" for alcohol, enter "e" for energetics, enter "o" for other: ').lower()


if name == "a" or name == "e" or name == "o":

    if age >= 14 and age < 18 and name == "a":
        print("Sorry, you're too young!")

    elif age >= 14 and age < 18 and (name == "e" or name == "o"):
        print("Thank you! Come again.")

    elif age < 14 and (name == "a" or name == "e"):
        print("Sorry, you're too young!")

    elif age < 14 and name == "o":
        print("Thank you! Come again.")

    else:
        print("Thank you! Come again.")

else:
    print("There's no such item.")