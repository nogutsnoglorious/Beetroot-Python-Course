# Lesson 18 Classwork; Task 2

# Створіть дескриптор DiscountLimit, який визначає максимальний обсяг знижки для товару.
# Забороніть встановлення знижки більше, ніж встановлено за лімітом.

class DiscountLimit:
    def __init__(self, max_discount):
        self.max_discount = max_discount
        self.name = None

    def __get__(self, instance, owner):
        return instance.__dict__
        
    def __set__(self, instance, value):
        if value > self.max_discount:
            raise ValueError(f'Value cannot exceed {self.max_discount}%.')
        instance.__dict__[self.name] = value
        print(f'New discount value of {value}% was successfully set.\n')

class Product:
    discount = DiscountLimit(30)

product = Product()
product.discount = 20
product.discount = 30
product.discount = 40



    
    
