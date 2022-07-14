nums =[0,-4,19,1,8,-2,-3,5]
if len(nums)==1:
    print(1)
        
    x = nums.index(max(nums))
    y = nums.index(min(nums))
    l = len(nums)
        
        
print(min(max(x+1,y+1), max(l-x,l-y), x+1+l-y, y+1+l-x))
    
    # max(x+1,y+1) -> length from the left side of the list till the number with the highest index
    # max(l-x,l-y) -> length from the right side of the list till the number with the highest index
    # x+1+l-y -> assuming the smallest number is in the left half of the list and the biggest on the right half, x+1 is the length from left end and l-y is the length from the right end
    # y+1+l-x -> assuming the biggest number is in the left half of the list and the smallest on the right half, y+1 is the length from left end and l-x is the length from the right end
    
    #These are the four possibilities, from which we compare and get the smallest length i.e. no. of cards that need to be picked.