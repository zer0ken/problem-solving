def main():
    import sys

    sys.setrecursionlimit(9*9*9)
    write = sys.stdout.write

    board = [list(map(int, line))
             for line in sys.stdin.read().rstrip().splitlines()]

    empties = [(row, col) for row in range(9)
               for col in range(9) if board[row][col] == 0]

    count = 0

    def solve(cur):
        nonlocal board, count
        count += 1
        
        if len(empties) == cur:
            for row in range(9):
                for col in range(9):
                    write(str(board[row][col]))
                write('\n')
            exit(0)

        row, col = empties[cur]
        possibles = set(range(1, 10))

        possibles -= set(board[row])
        possibles -= {board[r][col] for r in range(9)}

        row_block = row // 3
        col_block = col // 3
        possibles -= {board[r][c]
                      for r in range(3*row_block, 3*row_block + 3)
                      for c in range(3*col_block, 3*col_block + 3)}

        if not possibles:
            return

        for p in possibles:
            board[row][col] = p
            solve(cur + 1)
        board[row][col] = 0

    solve(0)


if __name__ == '__main__':
    main()
