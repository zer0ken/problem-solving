import sys
from collections import deque

readline = sys.stdin.readline
n = int(readline().rstrip())
queue = deque([i + 1 for i in range(n)])

while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)

sys.stdout.write(str(queue.popleft()))