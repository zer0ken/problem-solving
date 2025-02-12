def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, east, west, south, north = map(int, readline().split())
    board = [[0] * (2*N + 1) for _ in range(2*N + 1)]
    
    repeats = [east, west, south, north]
    deltas = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    def dfs(row, col, left):
        is_simple = not board[row][col]
        if not left:
            if is_simple:
                return 1, 1
            return 0, 1
        
        if not is_simple:
            return 0, 100 ** left
        
        simple = 0
        total = 0
        board[row][col] = 1

        for (drow, dcol), repeat in zip(deltas, repeats):
            if not repeat:
                continue
            nrow, ncol = row + drow, col + dcol
            next_simple, next_total = dfs(nrow, ncol, left - 1)
            simple += next_simple * repeat
            total += next_total * repeat
    
        board[row][col] = 0
        return simple, total

    simple, total = dfs(N, N, N)
    write(str(simple / total))

if __name__ == '__main__':
    main()