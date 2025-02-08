import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

buses = {i: [(i, 0)] for i in range(1, N + 1)}
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    buses[start].append((end, cost))

departure, arrival = map(int, sys.stdin.readline().split())

visited = [0] * (N + 1)
heap = [(0, departure)]
dist_to = [0 if i == departure else -1 for i in range(N + 1)]
while heap:
    cost, here = heapq.heappop(heap)
    if visited[here]:
        continue
    visited[here] = 1
    
    for there, next_cost in buses[here]:
        if dist_to[there] == -1 or dist_to[there] > cost + next_cost:
            dist_to[there] = cost + next_cost
            heapq.heappush(heap, (dist_to[there], there))

sys.stdout.write(str(dist_to[arrival]))