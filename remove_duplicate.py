nums = [1,1,2]
i = 0
while i < len(nums) - 1:
    if nums[i] == nums[i + 1]:
        nums.pop(i)
    else:
        i += 1
print(nums)