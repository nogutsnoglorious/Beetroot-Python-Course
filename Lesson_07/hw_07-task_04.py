# Lesson 7 Homework; Task 4
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
normal_dict = {}
position = 0
for i in list:
    position += 1
    normal_dict.update({i: position})
print(normal_dict)

reverse_dict = {}
for key,value in normal_dict.items():
    reverse_dict.update({value: key})
print(reverse_dict)