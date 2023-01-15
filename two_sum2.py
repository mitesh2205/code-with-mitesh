def two_sum(nums, target):
    mapp = {}
    for i in range(len(nums)):
        if target - nums[i] in mapp:
            return [mapp[target - nums[i]], i]
        mapp[nums[i]] = i

# two sum 2 with two pointers

def two_sum2(nums, target):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            return [i+1, j+1]
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1

