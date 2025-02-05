import sys

N, S = map(int,sys.stdin.readline().split())
min_s = None
acc = [0]
for num in map(int,sys.stdin.readline().split()):
    acc.append(acc[-1] + num)
l, r = 0, 0
while l != (N + 1) and r != (N + 1):
    if acc[r] - acc[l] < S:
        r += 1
    else:
        if min_s is None or min_s > r - l:
            min_s = r - l
        l += 1

sys.stdout.write(str(min_s) if min_s is not None else '0')