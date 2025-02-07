import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [list(map(lambda x: x == '1', input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

groups = []
for i in range(N):
    for j in range(N):
        if visited[i][j] or not board[i][j]:
            continue
        visited[i][j] = True
        count = 0
        queue = deque([(i, j)])
        while queue:
            row, col = queue.popleft()
            count += 1
            for drow, dcol in deltas:
                nrow = row + drow
                ncol = col + dcol
                if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N or visited[nrow][ncol] or not board[nrow][ncol]:
                    continue
                visited[nrow][ncol] = True
                queue.append((nrow, ncol))
        groups.append(count)
groups.sort()
sys.stdout.write(f'{len(groups)}\n')
sys.stdout.write('\n'.join(map(str, groups)))