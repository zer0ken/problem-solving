import sys
from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
board = [list(map(int, readline().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
deltas = [(1, 0), (0, 1)]
queue = deque([(0, 0)])
while queue:
    row, col = queue.popleft()
    if row == col == N - 1:
        write('HaruHaru')
        break
    
    stride = board[row][col]
    for drow, dcol in deltas:
        nrow = row + drow * stride
        ncol = col + dcol * stride
        if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol]:
            visited[nrow][ncol] = True
            queue.append((nrow, ncol))
else:
    write('Hing')