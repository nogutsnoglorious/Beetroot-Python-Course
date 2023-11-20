# Lesson 11 Classwork; Task 1
# Створіть текстовий файл example.txt і напишіть в ньому кілька рядків тексту.
# Напишіть програму, яка відкриває цей файл і виводить його вміст на екран.


# a = "Hello, World.\n"
# b = "I'm learning Python.\n"
# c = "How are you?\n"

# text_file = open("example.txt", "w+")
# text_file.write(a)
# text_file.write(b)
# text_file.write(c)
# text_file.close()

# text_file = open("example.txt", "r")
# data = text_file.read()
# print(data)
# text_file.close()


a = "Hello, World.\n"
b = "I'm learning Python.\n"
c = "How are you?\n"

# text_file = open("example.txt", "a+")
# text_file.write(a)
# text_file.write(b)
# text_file.write(c)
# print(text_file.read())

with open("example.txt", "r+") as text_file:
    text_file.write(a)
    text_file.write(b)
    text_file.write(c)
    data = text_file.read()
    print(data)