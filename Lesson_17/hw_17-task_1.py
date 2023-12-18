# Lesson 17 Homework; Task 1

# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.  

class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return 'woof woof'

class Cat(Animal):
    def talk(self):
        return 'meow'

def GenFunc(animal):
    return animal.talk()

NewCat = Cat()
NewDog = Dog()

print(GenFunc(NewDog))
print(GenFunc(NewCat))
