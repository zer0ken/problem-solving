import sys
from collections import deque

N, K = map(int, input().split())
queue = deque(list(range(1, N + 1)))
removed = []
while queue:
    queue.rotate(-K + 1)
    removed.append(queue.popleft())

print('<' + ', '.join(map(str, removed)) + '>')