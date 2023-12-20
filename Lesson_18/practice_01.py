# Lesson 18 Classwork; Task 1

# Створіть клас Book, який представляє книгу. Кожна книга має атрибути: назва, автор, рік видання та кількість сторінок.
# Перепишіть магічний метод __str__, щоб кожен об'єкт книги можна було зручно виводити у зрозумілому форматі.

class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return f'{self.title} is a {self.pages} pages book by {self.author} written in {self.year}.'
    

new_book = Book('Harry Potter', 'J.K. Rowling', 2023, 360)
print(new_book.__str__())