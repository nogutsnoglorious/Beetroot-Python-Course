# Lesson 11 Classwork; Task 2
# Створіть програму, яка приймає від користувача кілька рядків тексту.
# Запишіть ці рядки у новий текстовий файл output.txt.

sentence_1 = input("Write anything you want: ") + "\n"
sentence_2 = input("Repeat the action above: ")

file_2 = open("example2.txt","w+")
file_2.write(sentence_1)
file_2.write(sentence_2)
file_2.close()

file_2 = open("example2.txt","r")
print(file_2.read())
file_2.close()

