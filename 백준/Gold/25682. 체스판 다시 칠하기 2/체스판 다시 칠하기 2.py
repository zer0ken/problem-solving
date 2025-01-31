import sys

N, M, K = map(int, sys.stdin.readline().split())

matches = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j, color in enumerate(sys.stdin.readline().rstrip(), 1):
        need = 'B' if i % 2 == j % 2 else 'W'
        correctness = 1 if color == need else 0
        matches[i][j] = matches[i-1][j] + matches[i][j-1] - matches[i-1][j-1] + correctness

area = K * K
min_repaint = area
for i in range(K, N + 1):
    for j in range(K, M + 1):
        matche = matches[i][j] - matches[i-K][j] - matches[i][j-K] + matches[i-K][j-K]
        min_repaint = min(min_repaint, matche, area - matche)

sys.stdout.write(str(min_repaint))