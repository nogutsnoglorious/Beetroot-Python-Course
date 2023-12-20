# Lesson 18 Classwork; Task 9

# Створіть класи Restaurant, Menu, Dish та Order. Клас Restaurant має включати список меню (Menu),
# а Menu - список страв (Dish). Замовлення (Order) може містити різні страви (Dish).

class Restaurant:
    menus = []

    def add_menu(self, menu, type_):
        self.menus.append({'Type':type_, 'Items': menu.dishes})


class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append({'Name': dish.name, 'Price': dish.price})

class Order:
    def __init__(self):
        self.orders = []

    def add_order(self, dishes):
        self.orders.extend(dishes)
    

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price


salad = Dish("salad", 70)
fries = Dish("fries", 40)

menu1 = Menu()
menu1.add_dish(salad)
menu1.add_dish(fries)

res1 = Restaurant()
res1.add_menu(menu1, 'Vegan')

print(res1.menus)