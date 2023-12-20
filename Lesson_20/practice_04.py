# Lesson 20 Classwork; Task 4

# Калькулятор податків:
# Перевірте, чи функція правильно обчислює податок для суми доходу в межах одного діапазону ставок.
# Додайте тест для випадку, коли сума доходу знаходиться в межах кількох діапазонів ставок.
# Впевніться, що функція правильно обробляє великі суми доходу.

import unittest
import func_04

class MyTest(unittest.TestCase):
    def test_func_04_ESV_True(self):
        result1 = func_04.calc_tax(*[7000,6000,3000,4000], ESV=True)
        self.assertEqual(result1,3000)
    
    def test_func_04_ESV_False(self):
        result1 = func_04.calc_tax(*[7000,6000,3000,4000], ESV=False)
        self.assertEqual(result1,4000)

if __name__ == '__main__':
    unittest.main()