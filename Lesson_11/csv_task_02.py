# Lesson 11 Classwork; Task 5
# 1. Читання та виведення даних:
# Зчитайте дані з CSV файлу та виведіть перші 5 рядків для ознайомлення.

# 2. Фільтрація та сортування:
# Виведіть список працівників, які проживають в певному місті.

# 3. Статистика:
# Обчисліть середній вік працівників.
# Визначте кількість працівників з кожного відділу.

# 4. Додавання та видалення даних:
# Додайте нового працівника у файл та збережіть зміни.
# Видаліть працівника за певною умовою та оновіть файл.

# 5. Збереження в новий файл:
# Створіть новий CSV файл та збережіть туди лише певні поля працівників (наприклад, ім'я, вік, відділ).

# 6. Застосування умов:
# Створіть функцію, яка приймає назву відділу та повертає список працівників у цьому відділі.

import csv
import os

# Read first 5 lines from the CSV file
rows = []
with open(r"D:\GLORY\Education\Beetroot Python Course\Lesson_11\nestle_employee.csv", "r") as csv_wrapper:
    csv_reader = csv.reader(csv_wrapper)
    fields = next(csv_reader)
    for row in csv_reader:
        rows.append(row)

print("\nHere's 5 first rows in nestle_employee.csv:")
for el in rows[:5]:
    print(el)

# Filtering out workers from Tallinn
print("\nHere's the list of workers from Tallinn:")
for el in rows:
    if el[4] == "Tallinn":
        print(el[0] + " " + el[1])

# Average employee age
total_age = 0
for el in rows:
    total_age += int(el[2])
av_age = total_age / len(rows)
print(f'\nAverage employee age is {round(av_age,1)} y.o.')

# Calculating size of each department
print("\nHere's the headcount of each department in the company: ")
department_set = set()
for el in rows:
    department_set.add(el[6])
quantity = 0
for i in department_set:
    for x in rows:
        if i == x[6]:
            quantity += 1
    print(f'In {i} department work {quantity} people.')

# Add new employee
new_employee = ['Harry', 'Styles', '30', '+1 44345677346', 'Amsterdam', 'Netherlands', 'Human Resources']
with open(r"D:\GLORY\Education\Beetroot Python Course\Lesson_11\nestle_employee.csv", "a", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(new_employee)  # Use writerow() to write a single row
    print("New data has been appended to the CSV file")

# Check CSV
rows2 = []
with open(r"D:\GLORY\Education\Beetroot Python Course\Lesson_11\nestle_employee.csv", "r") as csv_wrapper:
    csv_reader = csv.reader(csv_wrapper)
    fields = next(csv_reader)
    for row in csv_reader:
        rows2.append(row)
    print("Here's updated CSV file:\n", rows2)

# Delete some employee
rows_to_keep = []
original_file = r"D:\GLORY\Education\Beetroot Python Course\Lesson_11\nestle_employee.csv"
with open(original_file, "r") as csv_wrapper:
    csv_reader = csv.reader(csv_wrapper)
    for row in csv_reader:
        if row[5] != 'Germany':
            rows_to_keep.append(row)

# Insert a new list into temp file
temp_file = r'D:\GLORY\Education\Beetroot Python Course\Lesson_11\temp_nestle_employee.csv'
with open(temp_file, "a", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in rows_to_keep:
        csv_writer.writerow(row)
    print("Here's new CSV file:\n", rows_to_keep)

os.replace(temp_file, original_file)

# Filter out name, age, city
with open(original_file, "r") as csv_wrapper:
    csv_reader = csv.reader(csv_wrapper)
    data_to_filter = []
    for row in csv_reader:
        filtered = []  # Initialize filtered for each row
        for index, value in enumerate(row):
            if index == 0 or index == 2 or index == 4:
                filtered.append(value)
        data_to_filter.append(filtered)
print(data_to_filter)

# Write filtered data into csv
filtered_csv = r'D:\GLORY\Education\Beetroot Python Course\Lesson_11\filtered_nestle_employee.csv'
with open(filtered_csv, "a", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in data_to_filter:
        csv_writer.writerow(row)             
    print("Here's filtered CSV file:\n", data_to_filter)

# Filter out workers by department
def Define_Workers(x):
    dep_workers = []
    for row in rows_to_keep:
        if row[6] == x:
            name = row[0] + " " + row[1]
            dep_workers.append(name)
    print(f'These are people who work in {x} department:')
    for el in dep_workers:
        print(el)
    
what_dep = input("Enter name of Department? ")
Define_Workers(what_dep)