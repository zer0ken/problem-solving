import sys

lines = sys.stdin.read().rstrip().splitlines()

K, N = map(int, lines[0].split())
wires = list(map(int, lines[1:]))

l = 1
r = sum(wires) // N

while l <= r:
    mid = (l + r) // 2
    if sum(w//mid for w in wires) >= N:
        l = mid + 1
    else:
        r = mid - 1

sys.stdout.write(str(l - 1))