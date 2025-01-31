import sys

N, M = map(int, sys.stdin.readline().split())
matrix = []

for _ in range(N):
    row = [0]
    for num in map(int, sys.stdin.readline().split()):
        row.append(row[-1] + num)
    matrix.append(row)

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    acc = 0
    for i in range(x1 - 1, x2):
        acc += matrix[i][y2] - matrix[i][y1 - 1]
    sys.stdout.write(f'{acc}\n')
