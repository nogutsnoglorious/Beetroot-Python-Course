# Lesson 14 Classwork; Task 3
# Клас "Книга":
# Створіть клас Book, який має атрибути title, author та year.
# Напишіть метод для виведення інформації про книгу.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def print_info(self):
        print(f'Mentioned book has next characteristics:\nTitle: {self.title}\nAuthor: {self.author}\nYear: {self.year}\n')

new_book = Book("Harry Potter and the Goblet of Fire", "J.K. Rowling", 2000)
another_book = Book("Catch 22", "Joseph Heller", 1961)
Book.print_info(new_book)
Book.print_info(another_book)

# print(f'New book has next characteristics:\nTitle: {new_book.title}\nAuthor: {new_book.author}\nYear: {new_book.year}')