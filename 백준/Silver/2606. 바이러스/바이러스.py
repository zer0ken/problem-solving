import sys

lines = iter(sys.stdin.read().rstrip().splitlines())

N = int(next(lines))
M = int(next(lines))
adj = [[] for _ in range(N + 1)]
for line in lines:
    a, b = map(int, line.split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False]*(N + 1)

def dfs(cur):
    visited[cur] = True
    for next in adj[cur]:
        if not visited[next]:
            dfs(next)

dfs(1)
print(sum(visited) - 1)