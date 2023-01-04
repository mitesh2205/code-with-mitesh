def course_schedule2(numCourses, prerequisites):
    graph = collections.defaultdict(list)

    for course, pre in prerequisites:
        graph[course].append(pre)

    visited =set()
    cycle = set()
    output = []

    def dfs(crs):
        if crs in cycle: return False
        if crs in visited: return True

        cycle.add(crs)

        for pre in graph[crs]:
            if dfs(pre) == False: return False

        cycle.remove(crs)
        visited.add(crs)
        output.append(crs)

        return True

    for crs in range(numCourses):
        if dfs(crs) == False: return []

    return output

    