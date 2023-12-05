# Lesson 16 Classwork; Task 2
# Створіть ієрархію класів для представлення різних типів транспортних засобів.
# Почніть з базового класу під назвою Vehicle і додайте такі атрибути, як марка, модель і рік.
# Створіть підкласи для певних типів транспортних засобів, таких як автомобіль, мотоцикл і вантажівка.
# Кожен підклас повинен мати додаткові атрибути та методи, специфічні для типу автомобіля.
# Тестуйте свої класи, створюючи екземпляри різних транспортних засобів і отримуючи доступ до їхніх атрибутів і методів.

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def print_info(self):
        attributes = vars(self)
        print(f'\nThis is {self.__class__.__name__}\'s info: ')
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

class Car(Vehicle):
    def __init__(self, brand, model, year, doors, body_type, pass_capacity):
        super().__init__(brand, model, year)
        self.doors = doors
        self.bodytype = body_type
        self.pass_capacity = pass_capacity
    
    def for_family(self):
        if self.pass_capacity > 2:
            return f'{self.brand} {self.model} {self.year} will be a good choice for family with {self.pass_capacity} passanger seats.'
        
class Moto(Vehicle):
    def __init__(self, brand, model, year, engine_type, top_speed, riding_position):
        super().__init__(brand, model, year)
        self.engine_type = engine_type
        self.top_speed = top_speed
        self.riding_position = riding_position
    
    def for_long_ride(self):
        if self.riding_position != "cruiser":
            return f'{self.brand} {self.model} {self.year} won\'t be a good choice for long rides because of {self.riding_position} riding position.'

class Truck(Vehicle):
    def __init__(self, brand, model, year, payload_capacity, towing_capacity, drivetrain):
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity
        self.towing_capacity = towing_capacity
        self.drivetrain = drivetrain
    
    def deliver_cargo(self):
        cargo_weight = int(input("Enter cargo's weight: "))
        truck_max_load = ""
        trucks_by_payload = {
            "Light Duty": 2722,
            "Medium Duty": 11793,
            "Heavy Duty": 20000
        }

        for key, value in trucks_by_payload.items():
            if self.payload_capacity != key:
                continue
            else:
                truck_max_load = value
                break

        if truck_max_load < int(cargo_weight):
            return f'\nUnfortunately, {self.brand} {self.model} {self.year} won\'t be able to deliver cargo of {cargo_weight} kg because exceeds the maximum payload for {self.payload_capacity} type trucks by {cargo_weight - truck_max_load} kg.'
        else:
            return f'\nGreat! {self.brand} {self.model} {self.year} will be able to deliver your cargo with weight of {cargo_weight} kg.\nYou\'re still able to add load of {truck_max_load - cargo_weight} kg.'
        
    
car_Ford_Focus = Car("Ford", "Focus", 2022, 5, "sedan", 6)
moto_Yamaha_YZF_R1 = Moto("Yamaha", "YZF-R1", 2022, "Inline-four", 300, "sporty")
truck_Chevrolet_Express = Truck("Chevrolet", "Express", 2011, "Light Duty", 3000, "RWD")

car_Ford_Focus.print_info()
print(car_Ford_Focus.for_family())

moto_Yamaha_YZF_R1.print_info()
print(moto_Yamaha_YZF_R1.for_long_ride())

truck_Chevrolet_Express.print_info()
print(truck_Chevrolet_Express.deliver_cargo())
