import random

word = input("Enter any word: ")

for x in range(5):
    new_word = ""
    for i in word:
        if new_word != "":
            substitution_index = random.randint(0, len(new_word)-1)
            new_word = new_word[:substitution_index] + i + new_word[substitution_index:]
        else:
            new_word += i
    print (new_word)