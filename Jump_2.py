def jump(nums):
    if len(nums) == 1:
        return 0

    end = jump = farthest = 0

    for i in range(len(nums)-1):
        farthest = max(farthest, i + nums[i])

        if i == end:
            end = farthest
            jump += 1

    return jump