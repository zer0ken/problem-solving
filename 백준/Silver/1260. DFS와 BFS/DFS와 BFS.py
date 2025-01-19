import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, 1 + n)}

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for k, l in graph.items():
    graph[k] = sorted(l)

def dfs(cur, visited):
    visited.append(cur)
    
    for next_ in graph[cur]:
        if next_ not in visited:
            dfs(next_, visited)

def bfs(start, visited):
    visited.append(start)
    
    queue = deque([start])
    
    while queue:
        cur = queue.popleft()
        for next_ in graph[cur]:
            if next_ not in visited:
                queue.append(next_)
                visited.append(next_)

dfs_visited = []
dfs(v, dfs_visited)

bfs_visited = []
bfs(v, bfs_visited)

sys.stdout.write(' '.join(map(str, dfs_visited)) + '\n')
sys.stdout.write(' '.join(map(str, bfs_visited)))