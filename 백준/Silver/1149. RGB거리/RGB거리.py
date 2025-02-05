import sys

N = int(sys.stdin.readline())
last = [0, 0, 0]
for _ in range(N):
    cur = list(map(int, sys.stdin.readline().split()))
    cur[0] += min(last[1], last[2])
    cur[1] += min(last[0], last[2])
    cur[2] += min(last[0], last[1])
    last = cur
sys.stdout.write(str(min(last)))