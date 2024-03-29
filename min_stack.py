def __init__(self):
    self.stack = []
    self.min_stack = [float('inf')]


def push(self, val):
    self.stack.append(val)
    self.min_stack.append(min(val, self.min_stack[-1]))


def pop(self):
    self.stack.pop()
    self.min_stack.pop()


def top(self):
    return self.stack[-1]


def getMin(self):
    return self.min_stack[-1]
