import sys

n, m = map(int, sys.stdin.readline().split())

matrix = []
for row in range(n):
    row_data = list(map(int, sys.stdin.readline().split()))
    matrix.append(row_data)


def get_tetromino(row, col, shape):
    value = 0
    for drow, dcol in shape:
        nrow = row + drow
        ncol = col + dcol
        if nrow >= n or ncol >= m:
            return 0
        value += matrix[nrow][ncol]
    return value


shapes = [
    [(0, 0), (1, 0), (0, 1), (1, 1)], # O
    [(0, 0), (1, 0), (2, 0), (3, 0)], # I
    [(0, 0), (0, 1), (0, 2), (0, 3)], # I 90 deg
    [(0, 0), (1, 0), (1, 1), (2, 1)], # S
    [(0, 1), (0, 2), (1, 0), (1, 1)], # S 90 deg
    [(0, 1), (1, 1), (1, 0), (2, 0)], # Z
    [(0, 0), (0, 1), (1, 1), (1, 2)], # Z 90 deg
    [(0, 0), (1, 0), (2, 0), (2, 1)], # L
    [(0, 0), (1, 0), (0, 1), (0, 2)], # L 90 deg
    [(0, 0), (0, 1), (1, 1), (2, 1)], # L 180 deg
    [(1, 0), (1, 1), (1, 2), (0, 2)], # L 270 deg
    [(0, 1), (1, 1), (2, 1), (2, 0)], # J
    [(0, 0), (1, 0), (1, 1), (1, 2)], # J 90 deg
    [(0, 0), (0, 1), (1, 0), (2, 0)], # J 180 deg
    [(0, 0), (0, 1), (0, 2), (1, 2)], # J 279 deg
    [(0, 0), (0, 1), (0, 2), (1, 1)], # T
    [(0, 1), (1, 1), (1, 0), (2, 1)], # T 90 deg
    [(0, 1), (1, 0), (1, 1), (1, 2)], # T 180 deg
    [(0, 0), (1, 0), (1, 1), (2, 0)], # T 2700 deg
]


best = max(
    max(
        get_tetromino(row, col, shape) 
        for shape in shapes
    ) 
    for col in range(m)
    for row in range(n)
)

sys.stdout.write(str(best))