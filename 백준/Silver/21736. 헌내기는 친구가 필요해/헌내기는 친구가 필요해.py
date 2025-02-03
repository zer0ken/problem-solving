import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = []
start = None
for i in range(N):
    row = list(sys.stdin.readline().rstrip())
    board.append(row)
    if start is None:
        for j in range(M):
            if row[j] == 'I':
                start = (i, j)
                row[j] = 'X'

dpos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
queue = deque([start])
meet = 0
while queue:
    r, c = queue.popleft()
    for dr, dc in dpos:
        nr, nc = r + dr, c + dc
        
        if nr < 0 or nr >= N or nc < 0 or nc >= M or board[nr][nc] == 'X':
            continue
        
        if board[nr][nc] == 'P':
            meet += 1
        
        board[nr][nc] = 'X'
        queue.append((nr, nc))

sys.stdout.write(str(meet) if meet else 'TT')