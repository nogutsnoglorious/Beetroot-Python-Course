# Task 1
# Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)


def reverse_sequence(sequence):
    stack = Stack()
    for char in sequence:
        stack.push(char)
    
    reversed_sequence = ''
    while not stack.is_empty():
        reversed_sequence += stack.pop()
    
    return reversed_sequence

if __name__ == "__main__":
    sequence = input("Enter a sequence of characters: ")
    reversed_sequence = reverse_sequence(sequence)
    print("Sequence in reverse order:", reversed_sequence)
