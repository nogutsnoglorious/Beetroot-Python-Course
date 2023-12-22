# Lesson 20 Homework; Task 2
# Write tests for the Phonebook application, which you have implemented in module 1. Design tests for this solution and write tests using unittest library

import unittest
import phonebook_application
import os
from random import randint

class MyTest(unittest.TestCase):
    def test_run(self):
        path = 'Lesson_20/phonebook.json'
        self.assertTrue(os.path.exists(path))
    
    def test_create(self):
        self.assertEqual(phonebook_application.create_file(), 'File already exists.')

    def test_new_entry(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = randint(1000000, 9999999)
        city = input("Enter city: ")
        state = input("Enter state: ")
        new_entry = phonebook_application.new_entry(first_name, last_name, phone, city, state)
        check_item = list(phonebook_application.read_file())[-1]
        self.assertEqual(new_entry, check_item)
    
    def test_exit(self):
        self.assertTrue(phonebook_application.phonebook("Exit"))

if __name__ == '__main__':
    unittest.main()