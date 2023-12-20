# Lesson 20 Classwork; Task 5

# Система обліку запасів:
# Створіть тест для додавання нового товару до системи обліку.
# Перевірте, чи функція правильно відстежує кількість товарів.
# Впевніться, що функція виводить коректну інформацію про наявність товарів на складі.

import unittest
import func_05

class MyTest(unittest.TestCase):
    def test_func_05_add_item1(self):
        result1 = func_05.warehouse_add_item("apple", 50)
        self.assertEqual(result1,"Product added!")

    def test_func_05_check_amount(self):
        result1 = func_05.warehouse_check_amount("apple")
        self.assertEqual(result1, 50)
    
    def test_func_05_add_item2(self):
        result1 = func_05.warehouse_add_item("cherry", 1000)
        self.assertEqual(result1,"Product added!")

    def test_func_05_show_info(self):
        print(func_05.new_list, {'apple': 50, 'cherry': 1000})

if __name__ == '__main__':
    unittest.main()