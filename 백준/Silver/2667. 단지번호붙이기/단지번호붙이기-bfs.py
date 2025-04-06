def main():
    import sys
    
    N, *board = sys.stdin.read().split()
    N = int(N)
    
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * N for _ in range(N)]
    count = []
    
    def bfs(row, col, value):
        visited[row][col] = True
        count[-1] += 1
        
        queue = [(row, col)]
        while queue:
            row, col = queue.pop(0)
            for drow, dcol in deltas:
                nrow, ncol = row + drow, col + dcol
                if 0 <= nrow < N and 0 <= ncol < N and \
                        not visited[nrow][ncol] and \
                        board[nrow][ncol] == value:
                    visited[nrow][ncol] = True
                    count[-1] += 1                    
                    queue.append((nrow, ncol))

    for row in range(N):
        for col in range(N):
            value = board[row][col]
            if value == '0' or visited[row][col]:
                continue
            count.append(0)
            bfs(row, col, board[row][col])
    count.sort()
    
    print(len(count), *count, sep='\n')


if __name__ == '__main__':
    main()