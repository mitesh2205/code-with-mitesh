def busSchedule(source, target, routes):
    graph = collecitoons.defaultdict(list)

    for i, route in enumerate(routes):
        for stop in route:
            graph[stop].append(i)
    
    num_of_bus = 0
    q = collections.deque([(source, 0)])
    visit_routes = set()
    visit_stops = set()

    while q:
        stop = q.popleft()

        if stop == target:
            return stop

        for routeid in graph[stop]:
            if routeid not in visit_routes:
                visit_routes.add(routeid)
                for stop in routes[routeid]:
                    if stop not in visit_stops:
                        visit_stops.add(stop)
                        q.append((stop, stop[1]+1))
        num_of_bus += 1
    return -1