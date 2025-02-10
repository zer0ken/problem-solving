import sys

readline = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, readline().split())
has = [False] * (N + 1)
kind = 0
for i in range(1, M + 1):
	card = int(readline())
	if not has[card]:
		has[card] = True
		kind += 1
		if kind == N:
			write(str(i))
			exit(0)
write('-1')