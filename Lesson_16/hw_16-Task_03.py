# Lesson 16 Homework; Task 3
# Write a class Product that has three attributes:
# - type
# - name
# - price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods,in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
# - add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
# - set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name).
# The discount must be specified in percentage
# - sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error.
# It also increments income if the sell_product method succeeds.
# - get_income() - returns amount of many earned by ProductStore instance.
# - get_all_products() - returns information about all available products in the store.
# - get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

class Product:
    def __init__(self, prod_type, name, price):
        self.prod_type = prod_type
        self.name = name
        self.price = price

class ProductStore:
    store_database = []
    predef_price = 1.3      # 30 percent price premium
    income = 0

    def add(self, product, quantity):
        new_product = {
            "Type": product.prod_type,
            "Name": product.name,
            "Price": product.price,
            "Quantity": quantity
        }
        
        self.store_database.append(new_product)
    
    def show_database(self):
        for product in self.store_database:
            print(product)
        print("*"*100, "\n")

    def set_discount(self, name_or_type, discount):
        for el in self.store_database:
            if el["Type"] == name_or_type:
                el.update({"Discount": str(discount) + "%"})
            elif el["Name"] == name_or_type:
                el.update({"Discount": str(discount) + "%"})
    
    def sell_product(self, prod_type, amount):
        for el in self.store_database:
            if "Discount" in el and el["Discount"]:
                if el["Type"] == prod_type:
                    if el["Quantity"] >= amount:
                        el["Quantity"] -= amount
                        print(f'{el["Discount"]} discount is applied!')
                        discount = int(el["Discount"].replace("%","")) / 100
                        self.income += amount * el["Price"] * self.predef_price * (1 - discount)
                        print(f'We\'ve just sold {amount} {el["Type"]} and our total income is {self.income}.\n{"*"*100}\n')
                    else:
                        raise ValueError ("There's not enough items in the warehouse for this operation")
            else:
                if el["Type"] == prod_type:
                    if el["Quantity"] >= amount:
                        el["Quantity"] -= amount
                        self.income += amount * el["Price"] * self.predef_price
                        print(f'We\'ve just sold {amount} {el["Type"]} and our total income is {self.income}.\n{"*"*100}\n')
                    else:
                        raise ValueError ("There's not enough items in the warehouse for this operation")
    
    def get_income(self):
        print(f'Total income at this moment is ${self.income}.\n{"*"*100}\n')

    def get_all_products(self):                 # get only product that are available for sale
        for product in self.store_database:
            if product["Quantity"] > 0:
                print(product)
        print("*"*100, "\n")
    
    def get_product_info(self, name):
        for product in self.store_database:
            if product["Name"] == name:
                for key, value in product.items():
                    print(f'{key}: {value}')
        print("*"*100, "\n")

shoes = Product('shoes', 'Nike', 20)
glasses = Product('glasses', 'Ray-Ban', 10)
jeans = Product('jeans', 'Levis', 9)

store = ProductStore()
store.add(shoes, 5)
store.add(glasses, 11)
store.show_database()
store.add(jeans, 3)
store.get_income()
store.set_discount('shoes', 30)
store.set_discount('Levis', 5)
store.show_database()
store.sell_product('glasses', 9)
store.show_database()
store.sell_product('shoes', 5)
store.sell_product('jeans', 2)
store.get_all_products()
store.show_database()
store.get_product_info('Levis')