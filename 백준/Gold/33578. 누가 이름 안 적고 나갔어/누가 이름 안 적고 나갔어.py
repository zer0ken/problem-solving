def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    raw = [readline().rstrip() for _ in range(N)]
    board = [[0]*M for _ in range(N)]
    
    TARGET = -1
    EMPTY = 0
    TEACHER = 1
    WALL = -999
    
    for row in range(N):
        for col in range(M):
            if raw[row][col] == 'S':
                board[row][col] = TARGET
            elif raw[row][col] == 'T':
                board[row][col] = TEACHER
            elif raw[row][col] == '#':
                board[row][col] = WALL
            elif raw[row][col] == 'J':
                board[row][col] = EMPTY
                ME = (row, col)
            else:
                board[row][col] = EMPTY
    
    visited = [[0]*M for _ in range(N)]
    visited[ME[0]][ME[1]] = 1
    
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    queue = deque([(ME[0], ME[1], 1, 0, 0)])
    while queue:
        row, col, is_me, waited, time = queue.popleft()
        
        if board[row][col] == -1:
            write(str(time))
            exit(0)
            
        if is_me and board[row][col] == TEACHER:
            board[row][col] = 0
            queue.appendleft((row, col, 0, 0, time))
        
        if is_me and not waited:
            queue.append((row, col, is_me, 1, time + 1))
            continue
        
        for drow, dcol in deltas:
            nrow, ncol = row + drow, col + dcol
            
            if 0 <= nrow < N and 0 <= ncol < M and board[nrow][ncol] != WALL:
                if is_me and not visited[nrow][ncol]:
                    visited[nrow][ncol] = 1
                    queue.append((nrow, ncol, is_me, 0, time + 1))
                elif not is_me and visited[nrow][ncol] != 2:
                    visited[nrow][ncol] = 2
                    queue.append((nrow, ncol, is_me, 0, time + 1))
                    
    write('-1')


if __name__ == '__main__':
    main()