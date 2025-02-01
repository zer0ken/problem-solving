import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] * N
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    arr[i-1:j] = [k] * (j - i + 1)

sys.stdout.write(' '.join(map(str, arr)))