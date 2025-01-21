import sys
from collections import deque

readline = sys.stdin.readline
deltas = ((0, 1), (1, 0), (-1, 0), (0, -1))

def count_connected(points):
    count = 0
    visited = []
    for pos in points:
        if pos in visited:
            continue
        count += 1
        queue = deque([pos])
        while queue:
            row, col = queue.popleft()
            for drow, dcol in deltas:
                npos = (row + drow, col + dcol)
                if npos not in points:
                    continue
                if npos in visited:
                    continue    
                visited.append(npos)
                queue.append(npos)
    return count

t = int(readline().rstrip())
for i in range(t):
    m, n, k = map(int, readline().split())
    points = []
    for j in range(k):
        points.append(tuple(map(int, readline().split())))
    sys.stdout.write(f'{count_connected(points)}\n')