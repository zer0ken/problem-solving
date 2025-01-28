import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = []
dist = [[[0, 0] for __ in range(M)] for _ in range(N)]

for _ in range(N):
    line = list(sys.stdin.readline().rstrip())
    board.append(list(line))
        
dist[0][0][0] = 1

deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
queue = deque([(0, 0, 0)])
while queue:
    row, col, broke = queue.popleft()
    d = dist[row][col][broke]
    
    for drow, dcol in deltas:
        nrow = row + drow
        ncol = col + dcol
        
        if nrow < 0 or nrow >= N or ncol < 0 or ncol >= M:
            continue
        
        if board[nrow][ncol] == '0' \
                and (dist[nrow][ncol][broke] == 0 or dist[nrow][ncol][broke] > d + 1):
            dist[nrow][ncol][broke] = d + 1 
            queue.append((nrow, ncol, broke))
        elif board[nrow][ncol] == '1' and broke == 0 \
                and (dist[nrow][ncol][1] == 0 or dist[nrow][ncol][1] > d + 1):
            dist[nrow][ncol][1] = d + 1
            queue.append((nrow, ncol, 1))

d, d_with_break = dist[N-1][M-1]
if d == d_with_break == 0:
    sys.stdout.write('-1')
else:
    if d == 0 or d_with_break == 0:
        min_d = d if d != 0 else d_with_break
    else:
        min_d = d if d < d_with_break else d_with_break
    
    sys.stdout.write(str(min_d))