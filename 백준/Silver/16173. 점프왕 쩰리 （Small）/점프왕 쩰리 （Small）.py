def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    board = [list(map(int, readline().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    
    queue = deque([(0, 0)])
    while queue:
        row, col = queue.popleft()
        
        if row == col == N - 1:
            write('HaruHaru')
            break
        
        stride = board[row][col]
        for drow, dcol in ((stride, 0), (0, stride)):
            nrow = row + drow
            ncol = col + dcol
            
            if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N or visited[nrow][ncol]:
                continue
            
            visited[nrow][ncol] = 1
            queue.append((nrow, ncol))
    else:
        write('Hing')


if __name__ == '__main__':
    main()