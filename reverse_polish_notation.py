def reverse_polish_notation(expression):
    stack = []
    for i in expression:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            stack.append(stack.pop() - stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            stack.append(stack.pop() / stack.pop())
        else:
            stack.append(int(i))
    return stack.pop()