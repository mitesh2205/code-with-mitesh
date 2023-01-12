def asteriodCollision(asteriods):
    stack =[]
    for a in asteriods:
        while stack and stack[-1]>0 and a<0: # if stack is not empty and last element is positive and current element is negative
            if stack[-1] + a < 0: stack.pop()
            elif stack[-1] + a > 0: break
            else: stack.pop(); break
        else: stack.append(a)
    return stack

# brute force method of solving asteriod collision

def asteriodCollision(asteriods):
    stack =[]
    for a in asteriods:
        if a>0: stack.append(a)
        else:
            while stack and stack[-1]>0 and a<0:
                if stack[-1] + a < 0: stack.pop()
                elif stack[-1] + a > 0: break
                else: stack.pop(); break
            else: stack.append(a)
    return stack

# TC: O(n^2) SC: O(n) where n is the length of asteriods