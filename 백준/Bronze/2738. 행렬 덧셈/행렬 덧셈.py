n, m = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
for row in range(n):
    for i, v in enumerate(input().split()):
        print(matrix[row][i] + int(v), end=' ')
    print()
        