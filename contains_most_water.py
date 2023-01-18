def contains_most_water(heights):
    max_area = 0
    l , r = 0 , len(heights) - 1

    while l < r:
        max_area = max(max_area, min(heights[l], heights[r]) * (abs(l-r)))

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return max_area
    