import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())

count = 0
for coin in (40, 20, 10, 5, 1):
	count += N // coin
	N %= coin

write(str(count))