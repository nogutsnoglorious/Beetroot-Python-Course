# Lesson 19 Classwork; Task 1

# Створіть клас EvenNumbers, який є ітератором для парних чисел. Ітератор повинен повертати парні числа від 2 до певного максимального значення.

from random import randint

class EvenNumbers:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.sequence):
            if self.sequence[self.index] % 2 == 0:
                result = self.sequence[self.index]
                self.index += 1
                return result
            else:
                self.index += 1
        raise StopIteration

num_list = [randint(2, 100) for x in range(randint(5, 15))]
even_numbers = EvenNumbers(num_list)

even_list = [num for num in even_numbers]

print(even_list)