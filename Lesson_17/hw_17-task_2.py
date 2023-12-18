# Lesson 17 Homework; Task 2

# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books

class Author:
    def __init__(self, name, country, birthday):
        self.books = []
        self.name = name
        self.country = country
        self.birthday = birthday
    
    def __str__(self):
        return f'{self.name} was born in {self.country} on {self.birthday}.'
    
    def __repr__(self):
        return self.__str__()
    
    def add_book(self, book):
        self.books.append(book.name)
        print(f'{book.name} was successfully added to a list of {self.name}\'s book list.')
    
    def show_authors_books(self):
        print(f'\nThis is a list of {self.name}\'s books:')
        for book in self.books:
            print(book)
        print('\n')

class Book(Author):
    book_amount = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        Book.book_amount += 1
        if isinstance(author, Author):
            self.author = author
        else:
            raise ValueError(f'{self.author.name} is not an instance of Author.')
    
    def __str__(self):
        return f'{self.name} was written by {self.author.name} in {self.year}.'
    
class Library:
    def __init__(self, name):
        self.books = []
        self.authors = []
        self.name = name
    
    def new_book(self, book):
        book_dict = {
            book.name: book.year
        }
        self.books.append(book_dict)
        print(f'{book.name} was successfully added to {self.name} book list.')
    
        author_dict = {
            book.author.name: book.name
        }
        self.authors.append(author_dict)
        print(f'{book.author.name} was successfully added to {self.name} author list.')
        return f'{book}\n'
    
    def group_by_author(self, author):
        for el in self.authors:
            for key, value in el.items():
                if key == author:
                    print(f'"{value}"')
        return f'These are the books by {author}.\n'

    def group_by_year(self, year:int):
        for el in self.books:
            for key, value in el.items():
                if int(value) == year:
                    print(f'"{key}"')
        return f'These are the books written in {year}.\n'
    
    def __str__(self):
        item = ""
        for el in self.authors:
            books = []
            for key, value in el.items():
                item = key
                if key == item:
                    books.append(value)
                    print(f'{key} wrote {value}')
        return ""
    
    def __repr__(self):
        return self.__str__()
    
FirstAuthor = Author("Andy Green", "France", "01/01/1923")
A1FirstBook = Book("An Apple", "1950", FirstAuthor)
A1SecondBook = Book("Red Cup", "1954", FirstAuthor)
A1ThirdBook = Book("Embroidery", "1957", FirstAuthor)

SecondAuthor = Author("Samantha Owen Lee", "China", "04/17/1937")
A2FirstBook = Book("Image of a Phantom", "1950", SecondAuthor)
A2SecondBook = Book("Crimson Curtain", "1954", SecondAuthor)
A2ThirdBook = Book("Thrill", "1957", SecondAuthor)
A2FourthBook = Book("The Broken Crown", "1950", SecondAuthor)

FirstAuthor.add_book(A1FirstBook)
FirstAuthor.add_book(A1SecondBook)
FirstAuthor.add_book(A1ThirdBook)
FirstAuthor.show_authors_books()
SecondAuthor.add_book(A2FirstBook)
SecondAuthor.add_book(A2SecondBook)
SecondAuthor.add_book(A2ThirdBook)
SecondAuthor.add_book(A2FourthBook)
SecondAuthor.show_authors_books()

MyLibrary = Library("VaLibrary")
print(MyLibrary.new_book(A1FirstBook))
print(MyLibrary.new_book(A1ThirdBook))
print(MyLibrary.new_book(A2SecondBook))
print(MyLibrary.new_book(A2FourthBook))
print(MyLibrary.group_by_author('Andy Green'))
print(MyLibrary.group_by_year(1950))
print(MyLibrary)
print(f'Total number of created books is {Book.book_amount}.')