# Lesson 9 Homework; Task 1
# Imports practice
# Make a directory with 2 modules; make a function in one of them;
# then import this function in the other module and use that in your script of choice.

from modules import module1, module2

your_name = module2.name
your_age = module2.age

print(module1.intro(your_name))
print(module1.greet(your_age))