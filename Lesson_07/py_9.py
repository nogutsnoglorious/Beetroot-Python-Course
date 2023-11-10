my_list = ['gun', 'watercolor', 'catnip', 'smiling', 'hydrofoam', 'full']
new_list = []
for el in my_list:
    if len(el) > 5:
        new_list.append(el)
print(new_list)