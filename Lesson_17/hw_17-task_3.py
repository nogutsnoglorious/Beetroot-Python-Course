# Lesson 17 Homework; Task 3

# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *)
# з належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

from math import gcd

class Fraction:
    def __init__(self, numerator, denom):
        if denom == 0:
            raise ValueError("denom cannot be zero")
        common = gcd(numerator, denom)
        self.numerator = numerator // common
        self.denom = denom // common

    def __str__(self):
        return f"{self.numerator}/{self.denom}"


    def __add__(self, other):
        new_numerator = self.numerator * other.denom + other.numerator * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_numerator, new_denom)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denom - other.numerator * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_numerator, new_denom)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denom = self.denom * other.denom
        return Fraction(new_numerator, new_denom)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        new_numerator = self.numerator * other.denom
        new_denom = self.denom * other.numerator
        return Fraction(new_numerator, new_denom)

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    result_add = x + y
    print(f"{x}+{y} = {result_add}")

    result_sub = x - y
    print(f"{x}-{y} = {result_sub}")

    result_mul = x * y
    print(f"{x}*{y} = {result_mul}")

    result_div = x / y
    print(f"{x}/{y} = {result_div}")

