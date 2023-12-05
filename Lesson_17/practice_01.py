# Lesson 17 Classwork; Task 1
# Створіть клас Person з атрибутами:
# - name (public)
# - _age (protected)
# - __address (private)
# Додайте методи для встановлення та отримання значень атрибутів. Створіть об'єкт цього класу та використовуйте методи для доступу до атрибутів.

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__address = 'Queens'

    def get_name(self):
        return self.name
    
    def set_name(self):
        new_name = input("Enter new name: ")
        self.name = new_name
        return new_name
        
    def get_age(self):
        return self._age
    
    def set_age(self):
        new_age = input("Enter new age: ")
        self.age = new_age
        return new_age
    
    def get_addr(self):
        return self.__address
    
    def set_addr(self):
        new_age = input("Enter new age: ")
        self.age = new_age
        return new_age
    
    def print_info(self):
        attributes = vars(self)
        print(f'\nThis is {__class__.__name__}\'s info: ')
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')
    
            
new_person = Person("Walter", 44)

print(new_person.get_name())
print(new_person.get_age())
print(new_person.get_addr())
# print(new_person.__address)
# new_person.set_name()
print(new_person.name)
# new_person.set_age()
new_person.print_info()
        

        