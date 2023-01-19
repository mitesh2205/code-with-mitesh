def diagonal_matrix(mat):
    primary_diagonal = 0
    secondary_diagonl = 0

    for i in range(len(mat)):
        primary_diagonal += mat[i][i]
        secondary_diagonl += mat[i][len(mat) - i - 1]

        if len(mat) % 2 == 0 and i == len(mat) // 2:
            primary_diagonal -= mat[i][i]
    return primary_diagonal + secondary_diagonl