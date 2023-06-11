def tower_of_hanoi(n,source, destination, helper):
    if n == 1:
        print("Move disk 1 from rod",source,"to rod",destination)
        return
    tower_of_hanoi(n-1, source, helper, destination)
    print("Move disk",n,"from rod",source,"to rod",destination)
    tower_of_hanoi(n-1, helper, destination, source)

tower_of_hanoi(3,'A','C','B')