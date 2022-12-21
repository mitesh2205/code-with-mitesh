def rob(nums):
    if len(nums) == 1:
        return nums[0]

    def helper(nums):
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

    return max(helper(nums[1:]), helper(nums[:-1]))


if __name__ == '__main__':
    nums = [2, 3, 2]
    print(rob(nums))

    nums = [1, 2, 3, 1]
    print(rob(nums))

    nums = [0]
    print(rob(nums))

    nums = [1, 2, 3]
    print(rob(nums))

    nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(rob(nums))
