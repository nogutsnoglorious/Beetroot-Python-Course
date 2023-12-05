# Lesson 17 Classwork; Task 2
# Створіть базовий клас Vehicle з атрибутами та методами:
# make (public)
# model (public)
# _year (protected)
# __engine_type (private)
# Створіть підклас Car, який успадковує Vehicle та має свій власний атрибут num_doors. Спробуйте змінити атрибути класів залежно від їх видимості.

class Vehicle:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self._year = year
        self.__enginetype = ''

class Car(Vehicle):
    def __init__(self, maker, model, year, num_doors):
        super.__init__(maker, model, year)
        self.num_doors = num_doors


new_car = Vehicle('Bugatti', 'Veyron', 2016, 3)
print(new_car.model)