def main():
    import sys
    from functools import cache
    
    sys.setrecursionlimit(100000)
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    WALL = 1
    
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL = 2
    
    N = int(readline())
    board = [list(map(int, readline().split())) for _ in range(N)]
    
    deltas = [
        [(0, 1, HORIZONTAL), (1, 1, DIAGONAL)],
        [(1, 0, VERTICAL), (1, 1, DIAGONAL)],
        [(0, 1, HORIZONTAL), (1, 0, VERTICAL), (1, 1, DIAGONAL)]
    ]
    
    @cache
    def dfs(row, col, shape):
        if row == col == N - 1:
            return 1
        
        cases = 0
        for drow, dcol, next_shape in deltas[shape]:
            nrow, ncol = row + drow, col + dcol
            if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N:
                continue
            is_wall = 1
            
            if next_shape == DIAGONAL:
                is_wall = board[nrow][ncol] + board[nrow-1][ncol] + board[nrow][ncol-1]
            else:
                is_wall = board[nrow][ncol]
            
            if not is_wall:
                cases += dfs(nrow, ncol, next_shape)
        
        return cases
    
    write(str(dfs(0, 1, HORIZONTAL)))


if __name__ == '__main__':
    main()