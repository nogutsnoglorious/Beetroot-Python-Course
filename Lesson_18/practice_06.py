# Lesson 18 Classwork; Task 6

# Створіть класи Order та User. Клас Order має включати інформацію про замовлення та об'єкт класу User як його власника.


class User:
    def __init__(self, name):
        self.name = name


class Order:
    def __init__(self, items, name):
        self.items = items
        self.name = User(name).name
    
    def print_order(self):
        print(f'{self.name} ordered next items:')
        for item in self.items:
            print(f'{item}')

new_Order = Order(['apple', 'pear', 'strawberry'], 'Jim')

new_Order.print_order()
    
    
