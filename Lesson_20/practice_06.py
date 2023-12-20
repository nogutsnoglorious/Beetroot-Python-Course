# Lesson 20 Classwork; Task 6

# Обчислення вартості доставки:
# Перевірте, чи функція правильно обчислює вартість доставки для різних вагових та відстаневих категорій.
# Додайте тест для випадку, коли вага або відстань дорівнює нулю.
# Впевніться, що функція правильно обробляє великі значення ваги та відстані.

import unittest
import func_06

class MyTest(unittest.TestCase):
    def test_func_06_case1(self):
        result1 = func_06.send_price(20,100)
        self.assertEqual(result1,12000)
    
    def test_func_06_case2(self):
        result1 = func_06.send_price(0,0)
        self.assertEqual(result1,"Error")
        result2 = func_06.send_price(0,1)
        self.assertEqual(result2,"Error")
        result3 = func_06.send_price(1,0)
        self.assertEqual(result3,"Error")
    
    def test_func_06_case3(self):
        result1 = func_06.send_price(1000,1000)
        self.assertEqual(result1,25000000)

if __name__ == '__main__':
    unittest.main()