# Lesson 10 Classwork; Task 5
# Запитайте користувача ввести своє ім'я та вік. Використайте блок try-except,
# щоб перевірити правильність введення даних та вивести повідомлення про помилку за необхідності.

name = input("Enter your name: ")
age = input("Enter your age: ")
try:
    name1 = name.split() + name.split()
    age1 = int(age)
    print('Your name is {} and you are {} years old.'.format(name,age1))
except TypeError:
    print("Your name can't be numerical.")
except ValueError:
    print("Your age can be only numerical.")