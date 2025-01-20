import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(range(n + 1))

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    arr[i:j+1] = arr[i:j+1][::-1]

sys.stdout.write(' '.join(map(str, arr[1:])))