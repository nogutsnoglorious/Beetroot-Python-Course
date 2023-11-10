import random
while True:
    a = random.randint(1,11)
    b = random.randint(1,11)
    answer = input(f'What is the answer for this expression? {a} + {a} * {b} = ... ')
    if answer == "":
        break
    elif answer.isdigit():
        if int(answer) == a + a * b:
            print("You are correct!")
            continue
        else:
            print("Wrong! Try again.")
            continue
    else:
        print ("Wrong! An answer should be numerical. Try again.")