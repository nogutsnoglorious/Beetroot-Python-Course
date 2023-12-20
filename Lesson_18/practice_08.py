# Lesson 18 Classwork; Task 8

# Створіть класи School, Classroom та Student. Клас School має включати список класів (Classroom), а клас Classroom - список учнів (Student).

from random import randint

class School:
    classrooms = []

    def add_classroom(self, classroom):
        self.classrooms.extend(classroom)

    def info(self):
        for index in range(len(self.classrooms)):
            print(f'Classroom {index + 1}:')
            for student in self.classrooms[index].students:
                print(f"  Student: {student.name}, Height: {student.height}, Age: {student.age}")


class Classroom:
    

    # def add_student(self, student):
    #     self.students.append(student)

    def add_student(self, student):
        self.students = []
        self.students.extend(student)

class Student:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

# Створюємо об'єкти студентів
student_1 = Student("Kirk", randint(130, 170), randint(10, 16))
student_2 = Student("Andy", randint(130, 170), randint(10, 16))
student_3 = Student("Michael", randint(130, 170), randint(10, 16))
student_4 = Student("Hellen", randint(130, 170), randint(10, 16))
student_5 = Student("Michelle", randint(130, 170), randint(10, 16))

# Створюємо об'єкти класів і школи
classroom_1 = Classroom()
classroom_1.add_student([student_1, student_2, student_3])
# classroom_1.add_student(student_2)
# classroom_1.add_student(student_3)

classroom_2 = Classroom()
classroom_2.add_student([student_4, student_5])
# classroom_2.add_student(student_5)

school_1 = School()
school_1.add_classroom([classroom_1, classroom_2])
# school_1.add_classroom(classroom_2)

# Виводимо інформацію про школу, класи та студентів
school_1.info()
# print(School().classrooms)