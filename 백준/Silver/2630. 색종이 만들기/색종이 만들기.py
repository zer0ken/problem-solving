import sys
n = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(n):
    matrix.append(sys.stdin.readline().split())

def count_white_blue(row=0, col=0, size=n):
    perfect = True
    color = matrix[row][col]
    
    for r in range(row, row + size):
        for c in range(col, col + size):
            if matrix[r][c] != color:
                perfect = False
                break
   
    if perfect:
        if color == '0':
            return 1, 0
        return 0, 1

    half = size // 2
    dpos = ((0, 0), (half, 0), (0, half), (half, half))
    acc_white, acc_blue = 0, 0
    for drow, dcol in dpos:
        nrow = row + drow
        ncol = col + dcol
        white, blue = count_white_blue(nrow, ncol, half)
        acc_white += white
        acc_blue += blue
    return acc_white, acc_blue 

white, blue = count_white_blue()
sys.stdout.write(f'{white}\n{blue}')