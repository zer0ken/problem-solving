def main():
    import sys

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    R, C, T = map(int, readline().split())
    board = [list(map(int, readline().split())) for _ in range(R)]
    
    for r in range(R):
        if board[r][0] == -1:
            purifier1 = r
            purifier2 = r + 1
            break
    
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for t in range(T):
        next_board = [list(row) for row in board]
        for r in range(R):
            for c in range(C):
                if board[r][c] > 0:
                    spreading_amount = board[r][c] // 5
                    for dr, dc in neighbors:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                            next_board[r][c] -= spreading_amount
                            next_board[nr][nc] += spreading_amount
            
        # purifier1
        for r in range(purifier1 - 1, 0, -1):
            next_board[r][0] = next_board[r - 1][0]
        for c in range(C - 1):
            next_board[0][c] = next_board[0][c + 1]
        for r in range(purifier1):
            next_board[r][-1] = next_board[r + 1][-1]
        for c in range(C - 1, 1, -1):
            next_board[purifier1][c] = next_board[purifier1][c - 1]
        next_board[purifier1][1] = 0
        
        # purifier2
        for r in range(purifier2 + 1, R - 1):
            next_board[r][0] = next_board[r + 1][0]
        for c in range(C - 1):
            next_board[-1][c] = next_board[-1][c + 1]
        for r in range(R - 1, purifier2, -1):
            next_board[r][-1] = next_board[r - 1][-1]
        for c in range(C - 1, 1, -1):
            next_board[purifier2][c] = next_board[purifier2][c - 1]
        next_board[purifier2][1] = 0
        
        board = next_board
        
    dust = sum(map(sum, board)) + 2
    write(str(dust))


if __name__ == '__main__':
    main()