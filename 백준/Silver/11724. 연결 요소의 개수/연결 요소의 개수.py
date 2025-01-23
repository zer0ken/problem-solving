import sys
from collections import deque

readline = sys.stdin.readline

n, m = map(int, readline().split())
graph = {str(i + 1) : [] for i in range(n)}

for _ in range(m):
    u, v = readline().split()
    graph[u].append(v)
    graph[v].append(u)

def count_connected():
    visited = []
    count = 0
    for vertex in graph.keys():
        if vertex in visited:
            continue
        count += 1
        queue = deque([vertex])
        while queue:
            cur = queue.popleft()
            for next_ in graph[cur]:
                if next_ in visited:
                    continue
                queue.append(next_)
                visited.append(next_)
    return count

sys.stdout.write(str(count_connected()))