import sys
from collections import deque

readline = sys.stdin.readline
N, K = map(int, readline().split())

matrix = []
queue = deque()
for i in range(N):
    row = list(map(int, readline().split()))
    matrix.append(row)
    for j in range(N):
        if row[j] == 0:
            continue
        queue.append((i, j))

S, X, Y = map(int, readline().split())

deltas = ((0, 1), (1, 0), (0, -1), (-1, 0))
for _ in range(S):
    queue_size = len(queue)
    infected = dict()
    for __ in range(queue_size):
        row, col = queue.popleft()
        virus = matrix[row][col]
        for drow, dcol in deltas:
            nrow = row + drow
            ncol = col + dcol
            npos = (nrow, ncol)
            if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N:
                continue
            cell = matrix[nrow][ncol]
            if cell != 0:
                continue
            if npos not in infected:
                queue.append(npos)
                infected[npos] = virus
            elif infected[npos] > virus:
                infected[npos] = virus
    for (r, c), k in infected.items():
        matrix[r][c] = k

sys.stdout.write(str(matrix[X-1][Y-1]))