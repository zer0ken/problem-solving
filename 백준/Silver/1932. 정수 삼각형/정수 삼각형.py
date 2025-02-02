import sys

N = int(sys.stdin.readline())
last = [0]
for i in range(1, N + 1):
    cur = list(map(int, sys.stdin.readline().split()))
    for j in range(i):
        cur[j] += max(last[max(j - 1, 0):j + 1])
    last = cur
sys.stdout.write(str(max(last)))