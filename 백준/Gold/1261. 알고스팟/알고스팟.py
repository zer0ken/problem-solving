def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    M, N = map(int, readline().split())
    board = [list(map(int, readline().rstrip())) for _ in range(N)]
    
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    broke_to_reach = [[-1] * M for _ in range(N)]
    broke_to_reach[0][0] = 0
    queue = deque([(0, 0, 0)])
    while queue:
        row, col, broke = queue.popleft()
        if row == N - 1 and col == M - 1:
            continue
        if broke_to_reach[row][col] < broke:
            continue
        
        for drow, dcol in deltas:
            nrow, ncol = row + drow, col + dcol
            if 0 <= nrow < N and 0 <= ncol < M:
                next_broke = broke + int(board[nrow][ncol])
                if broke_to_reach[nrow][ncol] == -1:
                    broke_to_reach[nrow][ncol] = next_broke
                    queue.append((nrow, ncol, next_broke))
                elif broke_to_reach[nrow][ncol] > next_broke:
                    broke_to_reach[nrow][ncol] = next_broke
                    queue.appendleft((nrow, ncol, next_broke))
    
    write(str(broke_to_reach[-1][-1]))


if __name__ == '__main__':
    main()