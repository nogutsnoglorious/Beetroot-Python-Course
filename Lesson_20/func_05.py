# 2. Система обліку запасів:
# Створіть функцію, яка дозволяє додавати товари до системи обліку запасів,
# відстежує кількість товарів та повертає інформацію про наявність товарів на складі.

new_list = {}

def warehouse_add_item(item_, amount):
    new_list.update({item_: amount})
    return "Product added!"

def warehouse_check_amount(item_):
    for key, value in new_list.items():
        if key == item_:
            return value
        
print(warehouse_add_item("apple", 50))
print(warehouse_check_amount("apple"))
print(warehouse_add_item("cherry", 1000))
print(new_list)