import sys

N, M, *A = map(int, sys.stdin.read().rstrip().split())

time = 0
for a in A:
    time += a - 1
    if time >= M:
        print('DIMI')
        exit(0)
print('OUT')