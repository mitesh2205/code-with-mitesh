from collections import defaultdict
def redundant_connection(edges):
    graph = defaultdict(list)

    def dfs(node,find):
        if node == find:
            return True
        
        visited.add(node)

        for nei in graph[node]:
            if nei not in visited and dfs(nei,find):
                return True
        return False


    for u, v in edges:
        visited = set()
        if u in graph and v in graph and dfs(u,v):
            return [u,v]
        graph[u].append(v)
        graph[v].append(u)
    

