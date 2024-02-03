from multiprocessing import Pool
import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def square(n):
    return n * n

def cube(n):
    return n * n * n

def calculate_all(number):
    return fibonacci(number), factorial(number), square(number), cube(number)

def multiprocessing_main():
    with Pool() as pool:
        results = pool.map(calculate_all, range(1, 11))
    fibs, facts, squares, cubes = zip(*results)
    print("Fibonacci:", fibs)
    print("Factorial:", facts)
    print("Squares:", squares)
    print("Cubes:", cubes)

if __name__ == "__main__":
    start_time = time.time()
    multiprocessing_main()
    multiprocessing_duration = time.time() - start_time
    print(f"Multiprocessing execution time: {multiprocessing_duration} seconds")
