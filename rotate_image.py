def rotate_image(matrix):
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r-l):
            top, bottom = l, r
            topleft = matrix[top][l+i]
            matrix[top][l+i] = matrix[bottom-i][l]
            matrix[bottom-i][l] = matrix[bottom][r-i]
            matrix[bottom][r-i] = matrix[top+i][r]
            matrix[top+i][r] = topleft
        l += 1
        r -= 1
    return matrix
