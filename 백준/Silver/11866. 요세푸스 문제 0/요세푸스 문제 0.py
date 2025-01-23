import sys
from collections import deque

readline = sys.stdin.readline
n, k = map(int, readline().split())
k -= 1
queue = deque(list(range(1, n + 1)))

removed = []
while queue:
    queue.rotate(-k)
    removed.append(str(queue.popleft()))

sys.stdout.write(f'<{", ".join(removed)}>')