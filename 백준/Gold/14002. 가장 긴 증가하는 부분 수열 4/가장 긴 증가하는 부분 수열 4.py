import sys
from functools import cache

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

@cache
def len_max_ascending(idx=0):
    max_len = 0
    cur = arr[idx]
    lis = []
    for j in range(idx + 1, N):
        if arr[j] > cur:
            l, lis_ = len_max_ascending(j)
            if max_len < l:
                max_len, lis = l, lis_
    return max_len + 1, [cur] + lis

max_len = 0
lis = []
for i in range(N - 1, -1, -1):
    l, lis_ = len_max_ascending(i)
    if max_len < l:
        max_len, lis = l, lis_

sys.stdout.write(f'{max_len}\n{" ".join(map(str, lis))}')