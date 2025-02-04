from collections import deque
input = iter(open(0).read().split('\n')).__next__

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dpos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board[0][0] = 1
queue = deque([(0, 0)])
while queue:
    r, c = queue.popleft()
    if r == N - 1 and c == M - 1:
        print(board[r][c])
        break
    d = board[r][c] + 1
    
    for dr, dc in dpos:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr > N - 1 or nc < 0 or nc > M - 1 \
                or type(board[nr][nc]) is not str or board[nr][nc] == '0':
            continue
        board[nr][nc] = d
        queue.append((nr, nc))