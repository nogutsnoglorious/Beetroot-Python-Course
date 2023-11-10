exit = False
while exit == False:
    answer = input("What is the answer for this expression? 2 + 2 * 2 = ... ")
    if answer.isdigit():
        if int(answer) == 6:
            print("You are correct!")
            exit = True
        else:
            print("Wrong! Try again.")
    else:
        print ("Wrong! An answer should be numerical. Try again.")


