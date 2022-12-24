def num_of_province(matrix):
    visited = [False] * len(matrix)
    count = 0
    for i in range(len(matrix)):
        if not visited[i]:
            dfs(matrix, visited, i)
            count += 1
    return count


def dfs(matrix, visited, i):
    for j in range(len(matrix)):
        if matrix[i][j] == 1 and not visited[j]:
            visited[j] = True
            dfs(matrix, visited, j)
