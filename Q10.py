"""
Q10. Write a Python program to create a class named Stack with methods for pushing and
    popping elements from the stack. Also, implement an iterator for the Stack class that
    returns the elements in LIFO (last in first out) order."""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def __iter__(self):
        self.current = len(self.stack) - 1
        return self

    def __next__(self):
        if self.current >= 0:
            item = self.stack[self.current]
            self.current -= 1
            return item
        else:
            raise StopIteration

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Popped:", stack.pop())  

print("Elements in LIFO order:")
for element in stack:
    print(element)
