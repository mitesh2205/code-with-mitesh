def surrounded_region(borad):
    row, col = len(board), len(board[0])

    def dfs(i, j):
        if i in ([0,row-1] or j in [0,col-1]) and board[i][j] == 'O':
            board[i][j] = 'D'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

    for i in range(row):
        for j in range(col):
            if board[i][j] == "O":
                dfs(i, j)

    for i in range(row):
        for j in range(col):
            if borad[i][j] == "O":
                board[i][j] = "X"

    for i in range(row):
        for j in range(col):
            if board[i][j] == "D":
                board[i][j] = "O"


print(surrounded_region([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))

