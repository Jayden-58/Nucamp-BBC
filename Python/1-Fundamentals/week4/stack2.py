class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("pass" if (stack.size() == 5) else "fail")
stack.push(5)
print("pass" if (stack.size() == 5) else "fail")

print("pass" if (stack.pop() == 5) else "fail")
print("pass" if (stack.pop() == 4) else "fail")