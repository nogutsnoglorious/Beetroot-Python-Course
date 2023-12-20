# Lesson 18 Classwork; Task 4

# Створіть класи Author та Book. Клас Book має включати інформацію про книгу (назва, рік випуску тощо) та об'єкт класу Author як її автора.

class Author:
    def __init__(self, name):
        self.name = name

# new_author = Author("J.K. Rowling", 56)

class Book:
    def __init__(self, title, year, name):
        self.title = title
        self.year = year
        self.author = Author(name)

    def info(self):
        return f'{self.title} was written by {self.author.name}.'

new_book = Book('Harry Potter', 2023, 'J.K. Rowling')

print(new_book.info())