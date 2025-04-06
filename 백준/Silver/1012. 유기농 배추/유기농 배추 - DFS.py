def main():
    import sys
    
    sys.setrecursionlimit(5000)
    
    def dfs(row, col):
        if 0 <= row < N and 0 <= col < M and \
                not visited[row][col] and board[row][col] == 1:
            visited[row][col] = True
            for drow, dcol in deltas:
                dfs(row + drow, col + dcol)
            
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
                dfs(row, col)
        
        results.append(count)
    
    print(*results, sep='\n')


if __name__ == '__main__':
    main()