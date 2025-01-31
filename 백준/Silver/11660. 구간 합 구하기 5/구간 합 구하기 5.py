import sys

N, M = map(int, sys.stdin.readline().split())
acc = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j, num in enumerate(map(int, sys.stdin.readline().split()), 1):
        acc[i][j] = acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1] + num

cache = {}
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{acc[x2][y2] - acc[x1-1][y2] - acc[x2][y1-1] + acc[x1-1][y1-1]}\n')