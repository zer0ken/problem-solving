import sys
from collections import deque

lines = iter(sys.stdin.read().rstrip().splitlines())

N, M, V = map(int, next(lines).split())
adj = [[] for _ in range(N + 1)]
for line in lines:
    a, b = map(int, line.split())
    adj[a].append(b)
    adj[b].append(a)
for x in range(1, N + 1):
    adj[x].sort()

visited = [False] * (N + 1)
results = []

def dfs(cur):
    visited[cur] = True
    results.append(cur)
    for next in adj[cur]:
        if not visited[next]:
            dfs(next)

dfs(V)
print(*results)

results = []
visited = [False] * (N + 1)
visited[V] = 1
queue = deque([V])

while queue:
    cur = queue.popleft()
    results.append(cur)
    
    for next in adj[cur]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)

print(*results)