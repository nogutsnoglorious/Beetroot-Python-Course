# Lesson 11 Classwork; Task 3
# Створіть JSON об'єкт, який представляє інформацію про книгу (назва, автор, рік видання) та збережіть його у файл з ім'ям "book.json".
# Зчитайте інформацію з файлу "book.json" та виведіть на екран у зручному форматі.
# Виведіть кількість книг у списку.

import json

with open(r"D:\GLORY\Education\Beetroot Python Course\Lesson_11\books.json", "r") as json_file:
    import_json = json.load(json_file)
    book = 0
    for el in import_json:
        book += 1
    print(import_json)
    print(f'There are {book} books in json file.')