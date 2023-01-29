def first_bad_version(n):
    l, r = 1, n
    while l < r:
        mid = (l + r) // 2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid + 1
    return l
