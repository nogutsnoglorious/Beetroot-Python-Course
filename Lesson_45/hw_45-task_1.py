# Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

from random import randint

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

arr = [1, 3, 5, 7, 9]
target = randint(1,10)

result = binary_search(arr, target)
if result is not None:
    print(f"Target element of {target} is found on {result} position.")
else:
    print("Target element not found.")
