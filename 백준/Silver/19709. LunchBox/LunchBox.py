import sys

N, M = map(int, sys.stdin.readline().split())
K = sorted(map(int, sys.stdin.read().split()))

acc = 0
count = 0
for k in K:
    if acc + k <= N:
        acc += k
        count += 1
    else:
        break

sys.stdout.write(str(count))