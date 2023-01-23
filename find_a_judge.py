def find_judge(n,trusts):

    if len(trusts) < n-1:
        return -1
    indegree = [0] ( n+1 )
    outdegree = [0] ( n+1 )

    for x, y in trusts:
        indegree[y] += 1
        outdegree[x] += 1

    for i in range(1,n+1):
        if indegree[i] == n-1 and outdegree[i] == 0:
            return i

    return -1
    