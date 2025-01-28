import sys
from collections import deque

readline = sys.stdin.readline
n, k = map(int, readline().split())

path = [None] * 100001
path[n] = n
queue = deque([n])

while queue:
    here = queue.popleft()
    if here == k:
        break
    for there in (here * 2, here - 1, here + 1):
        if there < 0 or there > 100000 or path[there] is not None:
            continue
        path[there] = here
        queue.append(there)

found = deque([k])
cur = k
while path[cur] != cur:
    found.appendleft(path[cur])
    cur = path[cur]

sys.stdout.write(f'{len(found) - 1}\n{" ".join(map(str, found))}')