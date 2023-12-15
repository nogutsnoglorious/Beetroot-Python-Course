# Lesson 15 Homework; Task 2

# Create a class Dog with class attribute 'age_factor' equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

from random import randint

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age
    
    def human_age(self):
        human_age = self.age * self.age_factor
        return f'Your dog is {self.age} y.o. which is equivalent to {human_age} years of human life.'

MyDog = Dog(randint(1,16))
print(MyDog.human_age())