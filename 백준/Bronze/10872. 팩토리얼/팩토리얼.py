import sys
from bisect import bisect_left

N = int(sys.stdin.readline().rstrip())

if N == 0:
    N = 1
else:
    for num in range(1, N):
        N *= num

sys.stdout.write(str(N))