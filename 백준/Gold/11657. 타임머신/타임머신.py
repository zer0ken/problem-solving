import sys
input = sys.stdin.readline
INF = int(1e8)

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

distance = [INF] * (n+1)
distance[1] = 0
iscycle = False
for i in range(n):
    for a, b, c in edges:
        if distance[a] != INF and distance[b] > distance[a] + c:
            distance[b] = distance[a] + c
            if i == n-1:
                iscycle = True

if iscycle:
    print(-1)
else:
    for i in range(2, n+1):
        print(distance[i] if distance[i] != INF else -1)