def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    R, C = map(int, readline().split())
    
    board = [readline().rstrip() for _ in range(R)]
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    max_path = 1
    
    queue = set([(0, 0, board[0][0])])
    while queue:
        row, col, path = queue.pop()
        max_path = max(max_path, len(path))
        if max_path == 26:
            break
        
        for drow, dcol in deltas:
            nrow, ncol = row + drow, col + dcol
            if 0 <= nrow < R and 0 <= ncol < C and board[nrow][ncol] not in path:
                queue.add((nrow, ncol, path + board[nrow][ncol]))
    
    write(str(max_path))


if __name__ == '__main__':
    main()