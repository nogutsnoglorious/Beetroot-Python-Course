# Lesson 16 Homework; Task 1
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender
    
    def print_info(self):
        attributes = vars(self)
        print(f'\nThis is {self.__class__.__name__}\'s info: ')
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

class Student(Person):
    def __init__(self, full_name, age:int, gender, faculty, course, ave_grade:float, uni_sports_team: bool):
        super().__init__(full_name, age, gender)
        self.faculty = faculty
        self.course = course
        self.ave_grade = ave_grade
        self.uni_sports_team = uni_sports_team

    def is_eligible_for_scholarship(self):
        if self.ave_grade > 4.0:
            return f'\nWith {self.ave_grade} average grade {self.full_name} is eligible for scholarship.'
        else:
            return f'\nUnfortunately average grade of {self.full_name} is not eligible for scholarship.'
    
    def is_eligible_for_auto_exam(self):
        if self.uni_sports_team == True:
            return f'\nNice! {self.full_name} is eligible to pass 1 exam automaticly.'
        else:
            return f'\nSorry! {self.full_name} has to pass all exams.'

class Teacher(Person):
    def __init__(self, full_name, age:int, gender, length_of_service, PhD:bool, salary: int):
        super().__init__(full_name, age, gender)
        self.length_of_service = length_of_service
        self.PhD = PhD
        self.salary = salary

    def is_eligible_for_bonus(self):
        if self.length_of_service > 15 and self.PhD == True:
            return f'\n{self.full_name} is eligible for bonus and will recieve additional payment of {int(self.salary * 0.1)}.'
        else:
            return f'\nThanks for your work! No bonus for this year.'
    
    def can_become_a_curator(self):
        if self.PhD == True:
            return f'Great! {self.full_name} can become a curator for a chosen group.'
        else:
            return f'Unfortunately, due to the fact {self.full_name} doesn\'t have a PhD, it\'s impossible to become a curator for now.'

student_Thorne = Student("Scott Thorne", 20, "Male", "Economics", "Trading", 3.2, True)
student_Storp = Student("Wanda Storp", 22, "Female", "Biology", "Botanics", 4.8, False)
teacher_Hudson = Teacher("Jordana Hudson", 57, "Female", 10, True, 60000)
teacher_Jonhson = Teacher("Thomas Johnson", 44, "Female", 21, False, 75500)

student_Thorne.print_info()
print(student_Thorne.is_eligible_for_scholarship())
print(student_Thorne.is_eligible_for_auto_exam())

student_Storp.print_info()
print(student_Storp.is_eligible_for_scholarship())
print(student_Storp.is_eligible_for_auto_exam())

teacher_Hudson.print_info()
print(teacher_Hudson.can_become_a_curator())
print(teacher_Hudson.is_eligible_for_bonus())

teacher_Jonhson.print_info()
print(teacher_Jonhson.can_become_a_curator())
print(teacher_Jonhson.is_eligible_for_bonus())