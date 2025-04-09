import sys

lines = iter(sys.stdin.read().rstrip().splitlines())

N, M = map(int, next(lines).split())
edges = [list(map(int, line.split())) for line in lines]

INF = float('inf')
dist = [INF] * (N + 1)
dist[1] = 0

for i in range(N):
    for start, end, d in edges:
        if dist[end] > dist[start] + d:
            if i == N - 1:
                print('-1')
                exit(0)
            dist[end] = dist[start] + d

print(*(-1 if d >= INF else d for d in dist[2:]), sep='\n')