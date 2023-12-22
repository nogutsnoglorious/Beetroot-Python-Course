# Lesson 19 Classwork; Task 1

# Генератор RandomTasks:
# Напишіть генератор, який генерує рандомні завдання для користувача. Кожне завдання повинно мати опис та приблизний час виконання.
# Генератор може створити, наприклад, список завдань на тиждень.

# training plan for week

import random

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]        # weekdays
exercise = ["pushups", "pullups", "airsquats", "plank", "situps"]                               # list of exercises
ex_time = ["1 minute", "2 minutes", "3 minutes"]                                                # time for each exercise

def RandomTasksGenerator(list_1, list_2, list_3):
    for index, i in enumerate(list_1):
        plan_for_day = []
        plan_for_day.append(list_1[index])                                                      # day of week
        plan_for_day.append(random.choice(list_2))                                              # random exercise
        plan_for_day.append(random.choice(list_3))                                              # random time
        yield plan_for_day
        
    
training_plan = list(RandomTasksGenerator(weekday, exercise, ex_time))
for i in training_plan:
    print('For {} you have to do {} of {}'.format(i[0],i[2],i[1]))


# не дуже зрозуміло було, яким чином і з чого відбувається генерація, тому така реалізація - єдиний варіант, який прийшов в голову.