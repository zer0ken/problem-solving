import sys
from functools import cache

sys.setrecursionlimit(1_000_000_000)
readline = sys.stdin.readline
write = sys.stdout.write

@cache
def F(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	return (F(n - 1) + F(n - 2)) % 1_000_000_007

K = int(readline())

for t in range(10, K, 100):
    F(t)

write(str(F(K)))