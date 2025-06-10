class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack Underflow")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack (top to bottom):")
        for item in reversed(self.items):
            print(item)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print("Popped:", stack.pop())
print("Top element:", stack.peek())
print("Is stack empty?", stack.is_empty())