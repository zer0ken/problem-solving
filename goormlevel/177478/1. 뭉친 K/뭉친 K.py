def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    x, y = map(int, readline().split())
    board = [list(map(int, readline().split())) for _ in range(N)]
    k = board[x - 1][y - 1]
    
    visited = [[False] * N for _ in range(N)]
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] or board[i][j] != k:
                continue
            visited[i][j] = True
            queue = deque([(i, j)])
            count = 1
            while queue:
                row, col = queue.popleft()
                for drow, dcol in deltas:
                    nrow, ncol = row + drow, col + dcol
                    if 0 <= nrow < N and 0 <= ncol < N \
                            and board[nrow][ncol] == k \
                            and not visited[nrow][ncol]:
                        visited[nrow][ncol] = True
                        count += 1
                        queue.append((nrow, ncol))
            if max_count < count:
                max_count = count
    
    write(str(max_count))


if __name__ == '__main__':
    main()