import random

word = input("Enter any word: ")

for x in range(5):
    character_list = []
    for i in word:
        character_list.append(i.lower())
        random.shuffle(character_list)

    new_word = ""
    for el in character_list:
        new_word += el

    print (new_word)

# не розумію, як можна вирішити завдання без списків