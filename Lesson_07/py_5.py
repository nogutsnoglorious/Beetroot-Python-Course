set_1 = set()
x = 0
while x < 21:
    if x % 2 == 0:
        set_1.add(x)
    x += 1
set_2 = set()
i = 0
while i < 100:
    if i % 3 == 0:
        set_2.add(i)
    i += 1
print(set_1)
print(set_2)
print(set_1.union(set_2))
