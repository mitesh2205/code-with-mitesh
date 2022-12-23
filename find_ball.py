def find_ball(grid):
    m, n = len(grid), len(grid[0])
    res = []
    for j in range(n):
        i, col = 0, j
        while i < m:
            if grid[i][col] == 1 and (col == n-1 or grid[i][col+1] == -1):
                res.append(-1)
                break
            elif grid[i][col] == -1 and (col == 0 or grid[i][col-1] == 1):
                res.append(-1)
                break
            elif grid[i][col] == 1:
                col += 1
            elif grid[i][col] == -1:
                col -= 1
            i += 1
        else:
            res.append(col)
    return res
