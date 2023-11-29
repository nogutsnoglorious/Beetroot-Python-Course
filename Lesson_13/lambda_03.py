# Lesson 13 Classwork; Task 3
# Напишіть лямбда-функцію для конвертації температури з градусів Цельсія
# в градуси Фаренгейта. Використайте цю функцію для конвертації кількох температур.

# convertion from Fahrenheit to Celsius
to_far_conv = lambda x: int(x*(9/5) + 32)

# convertion from Celsius to Fahrenheit
to_cels_conv = lambda x: int((x-32) * (5/9))

choice = input("What temperature you want to convert (C/F): ")
temp = input("Enter temperature value(s): ").split()    # use spaces between values

if choice == "C":
    input_data = ", ".join([str(el) for el in temp])
    result_list = [to_far_conv(int(x)) for x in temp]
    result = ", ".join([str(el) for el in result_list])
    print(f'{input_data} values in Celsius are {result} values in Fahrenheit.')

elif choice == "F":
    input_data = ", ".join([str(el) for el in temp])
    result_list = [to_cels_conv(int(x)) for x in temp]
    result = ", ".join([str(el) for el in result_list])
    print(f'{input_data} values in Celsius are {result} values in Fahrenheit.')

else:
    print("Unrecognized temperature unit.")
