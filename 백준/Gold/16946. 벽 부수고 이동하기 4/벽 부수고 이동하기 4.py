def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write

    N, M = map(int, readline().split())
    wall = [list(map(int, readline().rstrip())) for _ in range(N)]
    cc = [list(wall[i]) for i in range(N)]

    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] or wall[i][j]:
                continue
            visited[i][j] = 1
            count = 1
            queue = deque([(i, j)])
            touched_walls = set()
            while queue:
                row, col = queue.popleft()
                for drow, dcol in deltas:
                    nrow, ncol = row + drow, col + dcol
                    if 0 <= nrow < N and 0 <= ncol < M:
                        if wall[nrow][ncol]:
                            touched_walls.add((nrow, ncol))
                        elif not visited[nrow][ncol]:
                            visited[nrow][ncol] = 1
                            count += 1
                            queue.append((nrow, ncol))
            for row, col in touched_walls:
                cc[row][col] = (cc[row][col] + count) % 10
    
    for row in cc:
        write(''.join(map(str, row)) + '\n')


if __name__ == '__main__':
    main()