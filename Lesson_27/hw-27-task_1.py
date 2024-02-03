# Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS. 
# Compare the results and performance of each of them.

import concurrent.futures
import math

NUMBERS = [
    2,
    1099726899285419,
    1570341764013157,
    1637027521802551,
    1880450821379411,
    1893530391196711,
    2447109360961063,
    3,
    2772290760589219,
    3033700317376073,
    4350190374376723,
    4350190491008389,
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,
]

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    sqrt_num = int(math.sqrt(number))
    for i in range(5, sqrt_num + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True

def check_primes_with_threadpool(numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return results

def check_primes_with_processpool(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return results

if __name__ == "__main__":
    results_threadpool = check_primes_with_threadpool(NUMBERS)
    results_processpool = check_primes_with_processpool(NUMBERS)

    print("Results using ThreadPoolExecutor:")
    for num, result in zip(NUMBERS, results_threadpool):
        print(f"{num}: {'Prime' if result else 'Not Prime'}")

    print("\nResults using ProcessPoolExecutor:")
    for num, result in zip(NUMBERS, results_processpool):
        print(f"{num}: {'Prime' if result else 'Not Prime'}")
