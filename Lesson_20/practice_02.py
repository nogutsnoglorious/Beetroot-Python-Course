# Lesson 20 Classwork; Task 2
# Тести для функції перевірки парності:
# Створіть тест для перевірки парного числа.
# Додайте тест для непарного числа.
# Переконайтесь, що функція працює коректно для різних цілих чисел.

import unittest
import func_02

class MyTest(unittest.TestCase):
    def test_func_02_even(self):
        result1 = func_02.check_number(6)
        self.assertEqual(result1,True)
    
    def test_func_02_odd(self):
        result1 = func_02.check_number(3)
        self.assertEqual(result1,False)

if __name__ == '__main__':
    unittest.main()