# class Student:
#     def __init__(self, name, age, faculty, grades):
#         self.name = name
#         self.age = age
#         self.faculty = faculty
#         self.grades = grades

class Valentyn:
    def __init__(self):
        self.name = "Valentyn"
        self.surname = "Kryvoruchenko"
        self.group = "PY_118"

class Valentyn:
    def __init__(self, surname, group):
        self.name = "Valentyn"
        self.surname = surname
        self.group = group

class Student:
    def __init__(self, name, surname, group, age):
        self.name = name
        self.surname = surname
        self.group = group
        self.age = age
    
    def sleep(self, sleep_standard: float, start: float, end: float) -> str:
        duration = end - start
        if duration >= sleep_standard:
            print("Enough!")
        else:
            print("Not enough!")

    def study(self):
        pass

    def eat(self):
        pass

student_Valentyn = Student("Valentyn", "Kryvoruchenko", "PY_118", 31)
student_Valentyn.sleep(8.0, 16.2, 5.4)
student_Ihor = Student("Ihor", "Kapshuk", "PY_118", 25)