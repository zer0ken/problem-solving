import sys
from collections import deque

N = int(sys.stdin.readline())
tree = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    l, r = map(int, sys.stdin.readline().split())
    tree[l].append(r)
    tree[r].append(l)

queue = deque([(1, None)])
parent = [None] * (N + 1)

while queue:
    cur, prev = queue.popleft()
    if parent[cur] is not None:
        continue
    parent[cur] = prev
    
    for n in tree[cur]:
        queue.append((n, cur))

sys.stdout.write('\n'.join(map(str, parent[2:])))