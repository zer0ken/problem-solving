import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
board = []
dist = [[[0] * (K + 1)  for __ in range(M)] for _ in range(N)]

for _ in range(N):
    line = list(sys.stdin.readline().rstrip())
    board.append(list(line))
        
dist[0][0][0] = 1

deltas = [
    (0, 1, 0), (1, 0, 0), (0, -1, 0), (-1, 0, 0),
    (0, 1, 1), (1, 0, 1), (0, -1, 1), (-1, 0, 1),
]
queue = deque([(0, 0, 0)])
while queue:
    row, col, broke = queue.popleft()
    d = dist[row][col][broke]
    
    for drow, dcol, dbroke in deltas:
        nrow = row + drow
        ncol = col + dcol
        nbroke = broke + dbroke
        
        if nrow < 0 or nrow >= N or ncol < 0 or ncol >= M or nbroke > K:
            continue
        if board[nrow][ncol] == '0' and dbroke:
            continue
        if board[nrow][ncol] == '1' and not dbroke:
            continue
        if dist[nrow][ncol][nbroke] == 0 or dist[nrow][ncol][nbroke] > d + 1:
            dist[nrow][ncol][nbroke] = d + 1
            queue.append((nrow, ncol, nbroke))

d = dist[N-1][M-1]
if sum(d) == 0:
    sys.stdout.write('-1')
else:
    d = min(filter(lambda x: x != 0, d))
    sys.stdout.write(str(d))