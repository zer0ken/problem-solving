def main():
    import sys
    
    def dfs(row, col):
        nonlocal count
        
        if row < 0 or row >= N or \
                col < 0 or col >= N or \
                visited[row][col] or \
                board[row][col] == '0':
            return
        
        visited[row][col] = True
        count += 1
        for drow, dcol in deltas:
            dfs(row + drow, col + dcol)

    N, *board = sys.stdin.read().split()
    N = int(N)
    
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * N for _ in range(N)]
    counts = []
    
    for row in range(N):
        for col in range(N):
            if board[row][col] == '0' or visited[row][col]:
                continue
            count = 0
            dfs(row, col)
            counts.append(count)
    counts.sort()
    
    print(len(counts), *counts, sep='\n')


if __name__ == '__main__':
    main()