import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    lines = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    last = [0, 0, 0]
    for i in range(n):
        cur = [lines[0][i], lines[1][i], 0]
        cur[0] += max(last[1], last[2])
        cur[1] += max(last[0], last[2])
        cur[2] += max(last)
        last = cur
    sys.stdout.write(f'{max(last)}\n')