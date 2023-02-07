def fruit_in_basket(fruits):
    mapp = {}
    i = 0
    result = 0

    for j in range(len(fruits)):
        mapp[fruits[j]] += 1
        while len(mapp) > 2:
            mapp[fruits[i]] -= 1
            if mapp[fruits[i]] == 0:
                del mapp[fruits[i]]
            i += 1
        result = max(result, j - i + 1)
    return result

# Time Complexity: O(n)
# Space Complexity: O(1)