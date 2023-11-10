import random
print('Greetings! Lets play "Guess A Number" game.')

while True:
    user_number = int(input('Enter any number in the range from 1 to 10: '))
    comp_number = random.randint(1,10)
    if user_number == "exit":
        break
    elif user_number == comp_number:
        print("Congrats! You win!")
    elif user_number > 10 or user_number < 1:
        print("Entered number is out of range.")
    else:
        print("Sorry, you lost!")