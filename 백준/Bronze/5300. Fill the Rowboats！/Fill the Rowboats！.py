N = int(input())
for i in range(1, N + 1, 6):
    print(*range(i, min(i + 6, N + 1)), end=' Go! ')