def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Args:
        numbers (list): A list of numeric values.
    Returns:
        float: The average of the input numbers.
    """
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    if count != 0:
        average = total / count
    else:
        average = 0
    return average

numbers_list = [10, 20, 30, 40, 50]
result = calculate_average(numbers_list)
print(f"The average is: {result}")