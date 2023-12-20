# Lesson 18 Classwork; Task 2

# Створіть клас Transaction, який представляє транзакцію з банківського рахунку. Кожна транзакція має атрибути: сума транзакції, дата та опис.
# Перепишіть магічний метод __add__, щоб додавання двох транзакцій здійснювало об'єднання сум та описів транзакцій.

class Transaction:
    def __init__(self, sum, date, description):
        self.sum = sum
        self.date = date
        self.description = description
    def __add__(self, obj2):
        dict_ = {
            'total_sum': self.sum + obj2.sum,
            'desc': f'{self.description}; {obj2.description}'
            
        }
        return dict_
      
t1 = Transaction(100, '09.12.203', 'Desc 1')
t2 = Transaction(200, '09.12.203', 'Desc 2')
print(t1+t2)
print(t1.__add__(t2))