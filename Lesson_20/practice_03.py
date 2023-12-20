# Lesson 20 Classwork; Task 3
# Тести для функції знаходження максимуму:
# Створіть тест для перевірки найбільшого числа в  списку з невід‘ємних значень.
# Додайте тест для перевірки найменшого числа в списку з від’ємними значеннями.
# Переконайтесь, що функція правильно обробляє найбільший елемент в будь-якому списку.

import unittest
import func_03

class MyTest(unittest.TestCase):
    def test_func_03_pos(self):
        result1 = func_03.biggest_num([1,300,30,50,999,4,6])
        self.assertEqual(result1,999)
    
    def test_func_02_neg(self):
        result1 = func_03.biggest_num([-1,-300,-30,-50,-999,-4,-6])
        self.assertEqual(result1,-1)

if __name__ == '__main__':
    unittest.main()