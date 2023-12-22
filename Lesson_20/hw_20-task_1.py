# Lesson 20 Homework; Task 1
# Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using unittest library. 

import unittest
import task1_for_test

class MyTest(unittest.TestCase):
    def test_info(self):
        book1 = task1_for_test.Book("Brooklyn", 1999, "J.J. Austin")
        self.assertEqual(book1.info(),"Brooklyn was written by J.J. Austin in 1999.")
    
    def test_str(self):
        book2 = task1_for_test.Book("Brooklyn", 1999, "J.J. Austin")
        self.assertEqual(book2.__str__(), "Author: J.J. Austin, Book: Brooklyn, Year: 1999.")

if __name__ == '__main__':
    unittest.main()
