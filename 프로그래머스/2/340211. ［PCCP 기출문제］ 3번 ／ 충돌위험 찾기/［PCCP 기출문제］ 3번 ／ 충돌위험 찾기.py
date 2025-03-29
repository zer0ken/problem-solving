def solution(points, routes):
    path = [[[] for _ in range(len(points) + 1)] for _ in range(len(points) + 1)]
    for i, (row1, col1) in enumerate(points, 1):
        for j, (row2, col2) in enumerate(points, 1):
            row, col = row1, col1
            path[i][j].append((row, col))
            while row < row2:
                row += 1
                path[i][j].append((row, col))
            while row > row2:
                row -= 1
                path[i][j].append((row, col))
            while col < col2:
                col += 1
                path[i][j].append((row, col))
            while col > col2:
                col -= 1
                path[i][j].append((row, col))
    
    path_of_bot = [[] for _ in range(len(routes))]
    for i, plan in enumerate(routes):
        path_of_bot[i].append(tuple(plan))
        for start, end in zip(plan, plan[1:]):
            path_of_bot[i].pop()
            path_of_bot[i].extend(path[start][end])
    
    collision = 0
    
    for t in range(max(map(len, path_of_bot))):
        pos = set()
        colliding_pos = set()
        for route in path_of_bot:
            if t >= len(route):
                continue
            if route[t] in pos:
                colliding_pos.add(route[t])
            else:
                pos.add(route[t])
        collision += len(colliding_pos)
                
    return collision