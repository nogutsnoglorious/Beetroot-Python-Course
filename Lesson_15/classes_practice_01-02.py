# Lesson 14 Classwork; Task 1, 2
# 1. Створіть клас Car, який має атрибути brand, model і year.
# Також, створіть об'єкт(інстанс/екземпляр) цього класу та виведіть інформацію про цей автомобіль.
# 2. Розширте клас Car з попереднього завдання, додавши метод start(), який виводить
# повідомлення про те, що автомобіль почав рухатися.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self, speed:float) -> bool:
        if speed > 0:
            return True
        else:
            return False

new_car = Car("Ford", "Mustang", 1969)
print(f'New car has next characteristics:\nBrand: {new_car.brand}\nModel: {new_car.model}\nYear: {new_car.year}')

is_car_moving = new_car.start(234.5)
print(f'New car is moving: {is_car_moving}')