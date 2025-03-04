def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    TRUE = 1
    FALSE = 0
    
    N = int(readline())
    board = [list(map(int, readline().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if board[r][c] == 9:
                board[r][c] = 0
                shark = [r, c, 2]
                break
        else:
            continue
        break
    
    deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def find_closest_food():
        visited = [[FALSE] * N for _ in range(N)]
        visited[shark[0]][shark[1]] = TRUE
        queue = deque([(shark[0], shark[1], 0)])
        size = shark[2]
        
        food = None
        
        while queue:
            row, col, time = queue.popleft()
            ntime = time + 1
            
            for drow, dcol in deltas:
                nrow, ncol = row + drow, col + dcol
                if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N or visited[nrow][ncol]:
                    continue
                visited[nrow][ncol] = TRUE
                if 0 < board[nrow][ncol] < size:
                    if food is None or food[2] == ntime and (
                        food[0] > nrow or (food[0] == nrow and food[1] > ncol)
                    ):
                        food = (nrow, ncol, ntime)
                elif board[nrow][ncol] <= size:
                    queue.append((nrow, ncol, ntime))
        
        return food
    
    time = 0
    ate = 0
    food = find_closest_food()
    while food is not None:
        board[food[0]][food[1]] = 0
        shark[0:2] = food[0:2]
        ate += 1
        if ate >= shark[2]:
            ate = 0
            shark[2] += 1
        time += food[2]
        
        food = find_closest_food()

    write(str(time))


if __name__ == '__main__':
    main()