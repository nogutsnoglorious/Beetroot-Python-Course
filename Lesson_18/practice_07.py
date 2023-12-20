# Lesson 18 Classwork; Task 7

# Створіть класи Bank, Account та Customer. Клас Bank повинен містити список облікових записів (Account), а клас Customer - список облікових записів користувача.


from random import randint

class Customer:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

customer_1 = Customer("Kirby", "1/1/1990")
customer_2 = Customer("Jeremy", "3/6/1984")

class Account:
    customer_dict = {}
    
    def add_account(self, customer):
        self.customer_dict.update({customer.name: randint(100000, 999999)})
        return self.customer_dict

class Bank:
    account_list = []

    def account_info(self, customer_dict):
        for value in customer_dict.values():
            print(value)


print(Account().add_account(customer_1))
print(Account().add_account(customer_2))
Bank().account_info(Account.customer_dict)