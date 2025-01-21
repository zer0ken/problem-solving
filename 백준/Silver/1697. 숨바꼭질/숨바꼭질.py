import sys
from collections import deque

readline = sys.stdin.readline
n, k = map(int, readline().split())

visited = [False] * 100001
queue = deque([(n, 0)])
while queue:
    here, dist = queue.popleft()
    if here == k:
        break
    nexts = (here * 2, here - 1 , here + 1)
    for there in nexts:
        if there < 0 or there > 100000:
            continue
        if visited[there]:
            continue
        if there == k:
            dist += 1
            queue = None
            break
        visited[there] = True
        queue.append((there, dist + 1))

sys.stdout.write(str(dist))