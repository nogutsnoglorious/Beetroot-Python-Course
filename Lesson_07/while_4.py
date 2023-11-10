password = input("Enter new password: ")
while True:
    check = input("Repeat your new password: ")
    if check != password:
        continue
    else:
        break
print("Thanks, password is correct!")
