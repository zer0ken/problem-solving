import sys

N, M, V = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]
for line in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (N + 1)
results = []

def dfs(cur):
    visited[cur] = True
    results.append(cur)
    adj[cur].sort()
    for next in adj[cur]:
        if not visited[next]:
            dfs(next)

dfs(V)
print(*results)

results = []
visited = [False] * (N + 1)
visited[V] = 1
queue = [V]

while queue:
    cur = queue.pop(0)
    results.append(cur)
    
    for next in adj[cur]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)

print(*results)