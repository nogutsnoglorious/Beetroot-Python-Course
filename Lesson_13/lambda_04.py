# Lesson 13 Classwork; Task 4
# Напишіть лямбда-функцію для обчислення суми чисел у списку.
# Створіть список чисел та використайте цю функцію для знаходження їхньої суми.

my_list = []
while True:
    number = input("Enter any number: ")
    if number == "":
        break
    else:
        my_list.append(int(number))
elements_sum = lambda x: sum(x)
result = elements_sum(my_list)
print("You entered next numbers:", ", ".join([str(x) for x in my_list]))
print("Total sum of these numbers is", result)