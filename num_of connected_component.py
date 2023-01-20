def connected_component(n,edges):
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node):
        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)
    
    visited = set()
    count = 0

    for node in range(n):
        if node not in visited:
            dfs(node)
            count += 1
    return count
