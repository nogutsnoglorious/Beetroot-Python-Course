# Task 1
# Extend UnsortedList
# Implement append, index, pop, insert methods for UnsortedList.
# Also implement a slice method, which will take two parameters 'start' and 'stop', and return a copy of the list
# starting at the position and going up to but not including the stop position.

class UnsortedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        return self.items.index(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty list")

    def insert(self, index, item):
        self.items.insert(index, item)

    def slice(self, start, stop):
        return self.items[start:stop]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    my_list = UnsortedList()

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)

    print("Original list:", my_list)

    print("Index of 3:", my_list.index(3))

    print("Popped element:", my_list.pop())
    print("List after pop:", my_list)

    my_list.insert(2, 10)
    print("List after inserting 10 at index 2:", my_list)

    sliced_list = my_list.slice(1, 4)
    print("Sliced list:", sliced_list)
