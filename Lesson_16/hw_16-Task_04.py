# Lesson 16 Homework; Task 4
# Create your custom exception named 'CustomException', you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named 'logs.txt'.
# Tips: Use __init__ method to extend functionality for saving messages to file

import logging
from datetime import datetime

logging.basicConfig(filename=r'Lesson_16//logs.txt', level=logging.ERROR)

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

    def log_error(self):
        logging.error(self.msg)

word_list = ["Availability", "Diver", "Corruption", "Gemini", "Striker"]

def CheckSize(word_list):
    for index, word in enumerate(word_list):
        try:
            if len(word) >= 10:
                time_now = datetime.now()
                raise CustomException(f'Too long name word. Try another one: {word} ____ {time_now}')
            else:
                print(f'Word number {index+1} is okay!')
        except CustomException as e:
            e.log_error()  # Log the error message from within CustomException

CheckSize(word_list)