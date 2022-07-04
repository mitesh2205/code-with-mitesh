nums = [10,20,30,5,10,50]
res = nums[0] # to compare the maximum value and store in the response
cur_max = nums[0] # to get the current maximum sum from the iteration
 
# Iterate the loop till nums -1 length
for i in range (1, len(nums)):
    if(nums[i] > nums[i-1]):  # for comparing the 2 numbers are in ascending or not if ascending  then true if condition
        cur_max += nums[i]
        res = max(res,cur_max)
    else:
        cur_max = nums[i]

print(res)