def main():
    import sys

    def bfs(row, col):
        visited[row][col] = True
        queue = [(row, col)]
        while queue:
            row, col = queue.pop(0)
            for drow, dcol in deltas:
                nrow, ncol = row + drow, col + dcol
                if 0 <= nrow < N and 0 <= ncol < M and \
                        not visited[nrow][ncol] and board[nrow][ncol] == 1:
                    visited[nrow][ncol] = True
                    queue.append((nrow, ncol))
            
    lines = iter(sys.stdin.read().rstrip().splitlines())
    
    results = []
    for _ in range(int(next(lines))):
        M, N, K = map(int, next(lines).split())
        board = [[0] * M for _ in range(N)]
        for _ in range(K):
            X, Y = map(int, next(lines).split())
            board[Y][X] = 1
    
        visited = [[False] * M for _ in range(N)]
        deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 0
        
        for row in range(N):
            for col in range(M):
                if visited[row][col] or board[row][col] == 0:
                    continue
                count += 1
                bfs(row, col)
        
        results.append(count)
    
    print(*results, sep='\n')


if __name__ == '__main__':
    main()