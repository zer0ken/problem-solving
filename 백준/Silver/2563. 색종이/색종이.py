import sys
readline = sys.stdin.readline

N = int(readline().rstrip())

covered = set()

for _ in range(N):
    x, y = map(int, readline().split())
    for nx in range(x, x + 10):
        for ny in range(y, y + 10):
            covered.add((nx, ny))

sys.stdout.write(str(len(covered)))