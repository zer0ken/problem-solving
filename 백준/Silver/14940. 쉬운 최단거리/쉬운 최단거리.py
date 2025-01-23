import sys
from collections import deque

readline = sys.stdin.readline
n, m = map(int, readline().split())

matrix = []
for r in range(n):
    row = readline().split()
    for c in range(m):
        if row[c] == '0':
            row[c] = 0
        elif row[c] == '1':
            row[c] = -1
        else: # 2
            row[c] = 0
            target = (r, c)
    matrix.append(row)
    
deltas = ((0, 1), (1, 0), (0, -1), (-1, 0))

queue = deque([(target, 0)])
while queue:
    (r, c), dist = queue.popleft()
    
    for dr, dc in deltas:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if matrix[nr][nc] != -1:
            continue
        matrix[nr][nc] = dist + 1
        queue.append(((nr, nc), dist + 1))

for i in range(n):
    sys.stdout.write(f'{" ".join(map(str, matrix[i]))}\n')