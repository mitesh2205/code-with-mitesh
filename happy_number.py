def happynumber(nums):
    seen = set()
    while nums!=1 or nums not in seen:
        seen.add(nums)
        nums = sum(int(i)** 2 for i in str(nums))
    return nums == 1

    