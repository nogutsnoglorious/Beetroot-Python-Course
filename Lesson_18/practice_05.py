# Lesson 18 Classwork; Task 5

# Створіть класи Grade та Student. Клас Student має включати об'єкт класу Grade для представлення його оцінок.

class Grade:
    def __init__(self, grades) -> None:
        self.grades = grades
    
    def print_grade(self):
        for grade in self.grades:
            print(f'Student\'s grade is {grade}')

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = Grade(grades)

student_1 = Student("Jeremy", [3, 4, 5])
student_1.grades.print_grade()