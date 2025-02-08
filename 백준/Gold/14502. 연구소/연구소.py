def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    
    N, M = map(int, readline().split())
    board = [list(map(int, readline().split())) for _ in range(N)]
    virus_map = [[0] * M for _ in range(N)]
    virus = []
    empty = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                virus.append((i, j))
                virus_map[i][j] = 1
            if board[i][j] == 0:
                empty.append((i, j))
    
    combinations = []
    for i in range(len(empty) - 2):
        for j in range(i, len(empty) - 1):
            for k in range(j, len(empty)):
                combinations.append((empty[i], empty[j], empty[k]))

    max_safe = 0
    for new_walls in combinations:
        for i, j in new_walls:
            board[i][j] = 1
        
        safe = len(empty) - 3
        queue = deque(virus)
        visited = [list(row) for row in virus_map]
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            row, col = queue.popleft()
            for drow, dcol in deltas:
                nrow, ncol = row + drow, col + dcol
                if nrow < 0 or nrow >= N or ncol < 0 or ncol >= M \
                        or board[nrow][ncol] or visited[nrow][ncol]:
                    continue
                visited[nrow][ncol] = True
                queue.append((nrow, ncol))
                safe -= 1
        
        for i, j in new_walls:
            board[i][j] = 0

        if max_safe < safe:
            max_safe = safe
    
    sys.stdout.write(str(max_safe))


if __name__ == '__main__':
    main()