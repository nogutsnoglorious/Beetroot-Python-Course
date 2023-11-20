# Lesson 11 Classwork; Task 4
# Створіть CSV файл, який містить інформацію про фрукти (назва, кількість, ціна) для трьох різних фруктів.
# Зчитайте інформацію з файлу CSV та виведіть її на екран.
# Додайте новий рядок інформації про фрукт у існуючий CSV файл.
# Створіть програму, яка обчислює загальну вартість усіх фруктів у файлі та виводить її на екран.

import csv

# Read existing data from the CSV file
rows = []
with open("D:\GLORY\Education\Beetroot Python Course\Lesson_11\my_csv.csv", "r") as csv_wrapper:
    csv_reader = csv.reader(csv_wrapper)
    fields = next(csv_reader)
    for row in csv_reader:
        rows.append(row)
    print(f'Heres initial cvs file content: {rows}')

# Append new data to the CSV file
new_fruit = ["grapefruit", 2, 100]
with open("D:\GLORY\Education\Beetroot Python Course\Lesson_11\my_csv.csv", "a", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(new_fruit)  # Use writerow() to write a single row
    print("New data has been appended to the CSV file")

# Verify the appended data
with open("D:\GLORY\Education\Beetroot Python Course\Lesson_11\my_csv.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)