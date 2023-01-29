def findCelebrity(n):
    candidate = 0

    for i in range(1,n):
        if knwon(candidate,i):
            candidate = i
        
    for i in range(n):
        if i != candidate and (knows(candidate,i) or not knows(i,candidate)):
            return -1
    return candidate