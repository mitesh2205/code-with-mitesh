def subset2(nums):
    result = []
    subset = []
    nums.sort()

    def dfs(i):
        if i >= len(nums):
            if subset not in result:
                result.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)

    dfs(0)

    return result