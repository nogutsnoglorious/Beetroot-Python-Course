# Lesson 20 Classwork; Task 1
# Тести для функції суми:
# Створіть тест, щоб перевірити, чи правильно функція обробляє невід‘ємні числа.
# Додайте тест для перевірки суми від‘ємних чисел.
# Переконайтесь, що функція правильно обробляє комбінації невід‘ємних та від‘ємних чисел.

# Напишіть функцію, яка приймає два аргументи (числа) і повертає їх суму.

import unittest
import func_01

class MyTest(unittest.TestCase):
    def test_func_01_pos(self):
        result1 = func_01.numbers_sum(1,2)
        self.assertEqual(result1,3)
    
    def test_func_01_neg(self):
        result2 = func_01.numbers_sum(-2,-3)
        self.assertEqual(result2,-5)
    
    def test_func_01_neg_pos(self):
        result2 = func_01.numbers_sum(-4,3)
        self.assertEqual(result2,-1)

if __name__ == '__main__':
    unittest.main()