import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
dist = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = dist[b][a] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

min_person = -1
min_bacon = INF
for i in range(N):
    bacon = sum(dist[i])
    if min_bacon > bacon:
        min_bacon = bacon
        min_person = i

sys.stdout.write(str(min_person + 1))