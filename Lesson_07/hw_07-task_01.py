# Lesson 7 Homework; Task 1
# Make a program that has some sentence (a string) on input and returns a dict
# containing all unique words as keys and the number of occurrences as values.

new_dict = dict()
example = input("Enter a sentence, that will be turned into a dictionary: ").split()
for el in example:
    rep = 0
    for x in example:
        if el == x:
            rep += 1
        else:
            continue
    new_dict.update({el: rep})
print(new_dict)