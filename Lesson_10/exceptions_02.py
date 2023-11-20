# Lesson 10 Classwork; Task 2
# Запитайте користувача ввести число у вигляді рядка. Використайте блок try-except,
# щоб перевірити, чи введено коректне число, і виведіть повідомлення про помилку у протилежному випадку.

user_input = input("Please, enter a number: ")
try:
    print(user_input+1)
except TypeError:
    print("Here is a problem.")