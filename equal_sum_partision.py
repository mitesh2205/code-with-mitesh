def equal_sum_partision(arr):
    summ =0
    for i in range(len(arr)):
        summ += arr[i]
    
    if summ % 2 != 0:
        return False
    else:
        return subset_sum(arr, summ//2)

def subset_sum(arr,summ):   # optimized version to solve the subset sum problem
    dp = [False for i in range(len(arr)+1)]

    for i in range(1,len(arr)+1):
        for j in range(summ, arr[i-1]- 1, -1):
            dp[j] = dp[j] or dp[j - dp[j - arr[i-1]]]
    return dp[summ]

