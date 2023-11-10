exitpoll = list()
while True:
    answer = input("Did you vote? ")
    if answer != "":
        exitpoll.append(answer)
    else:
        break
unique = set(exitpoll)
print("All exitpoll answers are: ", exitpoll)
print("All unique answers are: ", unique)