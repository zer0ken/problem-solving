import sys

n, m = map(int, input().split())
matrix = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
for row in range(n):
    for i, v in enumerate(sys.stdin.readline().split()):
        sys.stdout.write(str(matrix[row][i] + int(v)) + ' ')
    sys.stdout.write('\n')
        