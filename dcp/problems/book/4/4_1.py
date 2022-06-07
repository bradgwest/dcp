class Stack:
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, x):
        self.stack.append(x)
        if self.maxes:
            x = max(self.maxes[-1], x)
        self.maxes.append(x)

    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.maxes[-1]


s = Stack()
for x in [2, 1, 3, 0, 1]:
    s.push(x)
    print(s.maxes)

for _ in range(4):
    s.pop()
    print(s.maxes)
