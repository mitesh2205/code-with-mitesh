def course_schedule(numCourses, prerequisites):
    if not prerequisites:
        return True

    graph = collections.defaultdict(list)

    for course, pre in prerequisites:
        graph[course].append(pre)

    visited = set()

    def dfs(crs):
        if crs in visited: return False

        if graph[crs] == []: return True

        visited.add(crs)

        for pre in graph[crs]:
            if not dfs(pre): return False
        
        visited.remove(crs)

        graph[crs] = []

        return True

    for crs in range(numCourses):
        if not dfs(crs): return False

    return True

