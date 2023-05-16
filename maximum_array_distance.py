def maximum_array_distance(array):
    output = 0
    min_array = array[0][0]
    max_array = array[0][-1]
    for i in range(1, len(array)):
        output = max(output, abs(array[i][0] - max_array), abs(array[i][-1] - min_array))
        min_array = min(min_array, array[i][0])
        max_array = max(max_array, array[i][-1])
    return output

print(maximum_array_distance([[1, 2, 3], [4, 5], [1, 2, 3]]))