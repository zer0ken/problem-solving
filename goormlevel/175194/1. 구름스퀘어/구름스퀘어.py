import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
events = [tuple(map(int, readline().split())) for _ in range(N)]
events.sort(key=lambda x: x[0])
events.sort(key=lambda x: x[1])

count = 0
last = 0
for s, e in events:
	if s > last:
		count += 1
		last = e

write(str(count))