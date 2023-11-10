alphabet = {
    "bbbb": 4,
    "aaa": 3,
    "wwwwww": 5,
    "yy": 2,
    "eeeeee": 6
}

while True:
    characters = input("Enter characters: ")
    print(f'There are {alphabet.get(characters)} letters.')
    q1 = input("Do you want to check other letters: ")
    if q1 != "":
        continue
    else:
        break

print("Thanks, bye!")