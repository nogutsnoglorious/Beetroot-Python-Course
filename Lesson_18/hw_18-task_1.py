# Lesson 18 Classwork; Task 1

# Створіть клас Rectangle, який має атрибути для зберігання довжини та ширини прямокутника. Використовуйте декоратор @property для повернення площі прямокутника.

from random import randint

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    @property
    def square(self):
        return self.width * self.length

newRec = Rectangle(randint(1,20),randint(1,20))
print(newRec.square)