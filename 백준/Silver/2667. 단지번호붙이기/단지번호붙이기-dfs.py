def main():
    import sys
    
    N, *board = sys.stdin.read().split()
    N = int(N)
    
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * N for _ in range(N)]
    count = []
    
    def dfs(row, col, value):
        if row < 0 or row >= N or \
                col < 0 or col >= N or \
                visited[row][col] or \
                board[row][col] != value:
            return
        
        visited[row][col] = True
        if value != '0':
            count[-1] += 1
            
        for drow, dcol in deltas:
            dfs(row + drow, col + dcol, value)

    for row in range(N):
        for col in range(N):
            value = board[row][col]
            if value == '0' or visited[row][col]:
                continue
            count.append(0)
            dfs(row, col, board[row][col])
    count.sort()
    
    print(len(count), *count, sep='\n')


if __name__ == '__main__':
    main()