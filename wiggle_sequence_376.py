nums = [1,7,4,9,2,5]
high = dip = 0
for i in range(1,len(nums)):
    if(nums[i-1] < nums[i]):
        high = dip + 1
                
    elif nums[i-1] > nums[i]:
        dip = high + 1
                
print(1 + max(dip, high))
                