# Lesson 14 Homework; Task 1
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

from functools import wraps

def print_decorator(func):
    @wraps(func)
    def wrapper(*args):
        arguments = []
        for arg in args:
            arguments.append(str(arg))
        function_full_name = f'{func.__name__}({", ".join(arguments)})'
        print(function_full_name)
        result = func(*args)
        return result
    return wrapper

@print_decorator
def calculate(*args):
    results = []
    for arg in args:
        result = int(arg) ** 2 - 100
        results.append(result)
    return results

numbers = [1, 22, 333]
print(calculate(*numbers))