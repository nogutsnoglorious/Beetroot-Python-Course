# Lesson 16 Classwork; Task 1
# Створіть ієрархію класів для представлення шкільної системи.
# Почніть з базового класу під назвою Person, який включає такі атрибути,
# як ім'я та вік. Створіть підкласи для студента та викладача, які успадковують від Person.
# Кожен підклас повинен мати додаткові атрибути та методи, специфічні для їх ролі. 
# Тестуйте свої класи, створюючи екземпляри студентів і викладачів і отримуючи доступ
# до їхніх атрибутів і методів.

class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, full_name, age:int, gender, faculty, course, ave_grade:float):
        super().__init__(full_name, age, gender)
        self.faculty = faculty
        self.course = course
        self.ave_grade = ave_grade
    
    def print_info(self):
        attributes = vars(self)
        print("\nThis is student's info: ")
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')
    
    def is_eligible_for_scholarship(self):
        if self.ave_grade > 4.0:
            return f'\nWith {self.ave_grade} average grade {self.full_name} is eligible for scholarship.'
        else:
            return f'\nUnfortunately erage grade {self.full_name} is not eligible for scholarship.'

class Teacher(Person):
    def __init__(self, full_name, age:int, gender, length_of_service, PhD:bool, salary: int):
        super().__init__(full_name, age, gender)
        self.length_of_service = length_of_service
        self.PhD = PhD
        self.salary = salary

    def print_info(self):
        attributes = vars(self)
        print("\nThis is teachers's info: ")
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

    def is_eligible_for_bonus(self):
        if self.length_of_service > 15 and self.PhD == True:
            return f'\n{self.full_name} is eligible for bonus and will recieve additional payment of {int(self.salary * 0.1)}.'
        else:
            return f'\nThanks for your work! No bonus for this year.'

student_Henderson = Student("Adam Henderson", 25, "Male", "Informatics", "Cybersecurity", 4.2)
teacher_Wilson = Teacher("Jessica Wilson", 46, "Female", 20, True, 60000)

student_Henderson.print_info()
print(student_Henderson.is_eligible_for_scholarship())

teacher_Wilson.print_info()
print(teacher_Wilson.is_eligible_for_bonus())
