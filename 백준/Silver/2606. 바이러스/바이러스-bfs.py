import sys

lines = iter(sys.stdin.read().rstrip().splitlines())

N = int(next(lines))
M = int(next(lines))
adj = [[] for _ in range(N + 1)]
for line in lines:
    a, b = map(int, line.split())
    adj[a].append(b)
    adj[b].append(a)

queue = [1]
visited = [False]*(N + 1)
visited[1] = True

while queue:
    cur = queue.pop(0)
    for next in adj[cur]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)

print(sum(visited) - 1)