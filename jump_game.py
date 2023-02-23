def can_jump(nums):
    last = len(nums) - 1

    for i in range(len(nums)-1,-1,-1):
        if i + nums[i] >= last:
            last = i
    return last == 0