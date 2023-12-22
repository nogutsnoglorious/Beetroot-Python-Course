# Lesson 19 Classwork; Task 1

# Ітератор для обліку використання робочого часу.
# Створіть клас WorkHoursCounter, який буде ітератором для обліку витраченого робочого часу.
# Користувач може додавати витрачений час на різні завдання, і ітератор буде підраховувати загальний витрачений час та виводити повідомлення про продуктивність.

class WorkHoursCounter:
    def __init__(self):
        self.work_day = {}
        self.total_time = 0
        self.task_iterator = None
    
    def add_task(self, task_name, time_task):
        if time_task in self.work_day:
            self.work_day[task_name] += time_task
        else:
            self.work_day[task_name] = time_task
        self.total_time += time_task
        self.task_iterator = iter(self.work_day.items())
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            task_name, time_task = next(self.task_iterator)
            return task_name, time_task
        except StopIteration:
            raise StopIteration

    def report(self):
        for task_name, time_task in self.work_day.items():
            if time_task >= 60:
                print(f'{time_task // 60} hours and {time_task % 60} minutes total spent on {task_name}.')
            else:
                print(f'{time_task} total minutes spent on {task_name}.')
        print(f'Total productivity level is {self.total_time // 60} hours and {self.total_time % 60} minutes, which is {round(self.total_time / 480 * 100, 2)}% of necessary amount. ')
        
work = WorkHoursCounter()
work.add_task('coding', 35)
work.add_task('debugging', 86)
work.add_task('meeting', 68)
work.add_task('coding', 203)
work.add_task('researching', 125)
work.add_task('debugging', 44)
work.report()
# print(work.__next__())

# Особисто для мене це досить різкий стрибок в плані складності завдань. Коли в LMS і на уроці розглядаються прості приклади, накшталт, перший елемент,
# останній елемент і крок, а тут ще треба створити клас і самому зрозуміти, яким чином це ще може бути ітератор. Я розумію, що в ітераторі має бути ітер і некст,
# але в простих прикладах ми одразу усе визначаємо і передаємо, а тут не зрозуміло, яким чином визначити те, що повертає ітер, і яким чином ми визначаємо функціонал
# некст, якщо знову ж таки в більш простих прикладах ми це одразу вручну визначаємо. І я не розумію, як ще вручну можна протестувати __next__.