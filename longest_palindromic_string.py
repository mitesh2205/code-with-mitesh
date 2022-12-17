def palindromic_string(s):
    mapp = {}
    for c in s:
        mapp[c] = mapp.get(c, 0) + 1
    result = 0
    odd = False
    for _, c in mapp:
        if c % 2 == 0:
            result += c
        else:
            odd = True
            result += c - 1
    if odd:
        result += 1
    return result

# Time: O(n)
# Space: O(n)
