def account_merger(accounts):
    graph = defaultdict(list)
    email_to_name = {}

    for account in accounts:
        name = account[0]

        for email in account[1:]:
            graph[account[1]].append(email)
            graph[email].append(account[1])
            email_to_name[email] = name
        
    
    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)
        result.append(node)

    result = []
    visited = set()
    final_result = []

    for email in graph:
        if email not in visited:
            dfs(email)
            result.sort()
            result = [email_to_name[email]] + result
            final_result.append(result)
        
    return final_result