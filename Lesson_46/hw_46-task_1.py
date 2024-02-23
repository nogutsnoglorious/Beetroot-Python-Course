# ДЗ: Вибрати 2-3 алгоритми з туторіалу і порівняти швидкість відпрацювання різних алгоритмів на одну і тому ж наборі даних.
# Comparing bubble sort to quick sort algorithms.

import random
import time

data = [random.randint(1, 10000) for _ in range(1000)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

start_time = time.time()
bubble_sorted_data = data[:]
bubble_sort(bubble_sorted_data)
bubble_sort_time = time.time() - start_time

start_time = time.time()
quick_sorted_data = data[:]
quick_sort(quick_sorted_data, 0, len(quick_sorted_data)-1)
quick_sort_time = time.time() - start_time

print(f"Bubble Sort Time: {bubble_sort_time*1000} miliseconds")
print(f"Quick Sort Time: {quick_sort_time*1000} miliseconds")
