def main():
    import sys
    
    sys.setrecursionlimit(int(1e+4))
    readline = sys.stdin.readline
    write = sys.stdout.write

    N, M = map(int, readline().split())
    board = [list(map(int, readline().split())) for _ in range(N + 1)]
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dp = [[-1] * M for _ in range(N)]
    dp[-1][-1] = 1
    
    def dfs(row, col, dp):
        if dp[row][col] != -1:
            return dp[row][col]
        cases = 0
        height = board[row][col]
        for drow, dcol in deltas:
            nrow, ncol = row + drow, col + dcol
            if 0 <= nrow < N and 0 <= ncol < M and board[nrow][ncol] < height:
                if dp[nrow][ncol] != -1:
                    cases += dp[nrow][ncol]
                else:
                    cases += dfs(nrow, ncol, dp)
        dp[row][col] = cases
        return cases
    
    
    write(f'{dfs(0, 0, dp)}')


if __name__ == '__main__':
    main()