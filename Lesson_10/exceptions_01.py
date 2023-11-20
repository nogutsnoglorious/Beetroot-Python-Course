# Lesson 10 Classwork; Task 1
# Напишіть програму, яка приймає два числа від користувача і виводить результат ділення
# першого числа на друге. Оберіть такі числа, щоб викликати помилку ділення на нуль
# і використайте блок try-except для відловлення цієї помилки та виведення відповідного повідомлення.

number_1 = int(input("Please enter 1st number: "))
number_2 = int(input("Please enter 2nd number: "))
try:
    result = number_1 / number_2
    print('Here is the result of division: {}.'.format(result))
except ZeroDivisionError:
    print('Please, avoid zero.')
finally:
    print("Finally is here.")
print("Hello?")