import sys
from collections import deque

readline = sys.stdin.readline
n, k = map(int, readline().split())

visited = [False] * 100001
queue = deque([n])

dist = 0
while True:
    count = 0
    newly_visited = []
    for _ in range(len(queue)):
        here = queue.popleft()
        if here == k:
            count += 1
            continue
        for there in (here * 2, here - 1 , here + 1):
            if there < 0 or there > 100000 or visited[there]:
                continue
            newly_visited.append(there)
            queue.append(there)
    if count:
        break
    dist += 1
    for visit in newly_visited:
        visited[visit] = True

sys.stdout.write(f'{dist}\n{count}')