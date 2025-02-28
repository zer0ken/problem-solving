N, M, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for _ in range(q):
    op, i, j, *k = map(int, input().split())
    if op == 0:
        matrix[i][j] = k[0]
    else:
        matrix[i], matrix[j] = matrix[j], matrix[i]
for row in matrix:
    print(' '.join(map(str, row)))
