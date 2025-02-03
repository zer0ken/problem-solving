import sys

N, M, B = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_time = 1e+9
for h in range(257):
    block = B
    time = 0
    for i in range(N):
        for j in range(M):
            block_delta = board[i][j] - h
            block += block_delta
            if block_delta > 0:
                time += block_delta * 2
            else:
                time -= block_delta
    if block < 0:
        break
    if min_time >= time:
        min_time = time
        best_h = h

sys.stdout.write(f'{min_time} {best_h}')