def wiggle_sort(array):
    for i in range(1, len(array)):
        if i % 2 == 1 and array[i] < array[i-1] or i % 2 == 0 and array[i] > array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
    return array

print(wiggle_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))