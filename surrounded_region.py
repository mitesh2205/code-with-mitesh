def surrounded_region(borad):
    row, col = len(board), len(board[0])

    def dfs(i, j):
        if i < 0 or j < 0 or i == row or j == col or board[i][j] != "O":
            return
        board[i][j] = 'D'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    for i in range(row):
        for j in range(col):
            if board[i][j] == "O" and (i == 0 or i == row - 1 or j == 0 or j == col - 1):
                dfs(i, j)

    for i in range(row):
        for j in range(col):
            if board[i][j] == "O":
                board[i][j] = "X"

    for i in range(row):
        for j in range(col):
            if board[i][j] == "D":
                board[i][j] = "O"

    return board


print(surrounded_region([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))

