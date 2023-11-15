# Lesson 9 Classwork; Task 2
# 2. Напишіть функцію, яка приймає будь-яку кількість словників і зливає їх у один.


def dict_combine(**kwargs):
    all_dicts = dict()
    all_dicts.update(main_info)
    all_dicts.update(add_info)
    return(all_dicts)

main_info = {
    "name": "John",
    "surname": "Doe",
    "city": "Odesa"
}

add_info = {
    "age": 20,
    "work": True,
    "married": False,
    "children": 3
}

print(dict_combine(**main_info, **add_info))