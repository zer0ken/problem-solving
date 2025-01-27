import sys
from functools import cache

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

@cache
def len_max_ascending(idx=0):
    max_acc = 0
    cur = arr[idx]
    for j in range(idx + 1, N):
        if cur < arr[j]:
            max_acc = max(max_acc, len_max_ascending(j))
    return max_acc + cur

max_acc = 0
for i in range(N - 1, -1, -1):
    max_acc = max(max_acc, len_max_ascending(i))

sys.stdout.write(str(max_acc))