import random
print('Greetings! Lets play "Guess A Number" game.')

while True:
    comp_number = random.randint(1,10)
    user_number = input('Enter any number in the range from 1 to 10: ')
    if user_number == "":
            break
    elif type(int(user_number)) != int:
        print("It is a character, not a number.")
        continue
    else:        
        if user_number == comp_number:
            print("Congrats! You win!")
        elif user_number > 10 or user_number < 1:
            print("Entered number is out of range.")
        else:
            print("Sorry, you lost!")