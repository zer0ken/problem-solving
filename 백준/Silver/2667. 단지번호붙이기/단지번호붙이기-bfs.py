def main():
    import sys
    
    def bfs(row, col):
        visited[row][col] = True
        count = 1
        
        queue = [(row, col)]
        while queue:
            row, col = queue.pop(0)
            for drow, dcol in deltas:
                nrow, ncol = row + drow, col + dcol
                if 0 <= nrow < N and 0 <= ncol < N and \
                        not visited[nrow][ncol] and \
                        board[nrow][ncol] == '1':
                    visited[nrow][ncol] = True
                    count += 1                    
                    queue.append((nrow, ncol))
        
        return count
             
    N, *board = sys.stdin.read().split()
    N = int(N)
    
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * N for _ in range(N)]
    counts = []

    for row in range(N):
        for col in range(N):
            if board[row][col] == '0' or visited[row][col]:
                continue
            counts.append(bfs(row, col))
    counts.sort()
    
    print(len(counts), *counts, sep='\n')


if __name__ == '__main__':
    main()