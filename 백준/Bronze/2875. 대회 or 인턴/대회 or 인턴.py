N, M, K = map(int, input().split())
print(min(3*N, 6*M, 2*(N + M - K)) // 6)