import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = {i: {} for i in range(1, V + 1)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = w if v not in graph[u] else min(w, graph[u][v])

heap = []
dist = [None] * (V + 1)
last_d = 0

heapq.heappush(heap, (0, start))
dist[start] = 0
while heap:
    d, u = heapq.heappop(heap)
    
    if dist[u] is not None and d > dist[u]:
        continue
    
    if u not in graph:
        continue
    
    for v, nd in graph[u].items():
        if dist[v] is None or d + nd < dist[v]:
            dist[v] = d + nd
            heapq.heappush(heap, (dist[v], v))

for d in dist[1:]:
    if d is None:
        sys.stdout.write('INF\n')
    else:
        sys.stdout.write(f'{d}\n')