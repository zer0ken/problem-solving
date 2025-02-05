import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
ladder = {}
snake = {}
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    ladder[s] = e
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    snake[s] = e

dist = [None] * 101
dist[1] = 0
queue = deque([(1, 0)])

while queue:
    here, roll = queue.popleft()
    roll += 1
    for dice in range(6, 0, -1):
        there = here + dice
        if there > 100:
            continue
        if there in ladder:
            there = ladder[there]
        elif there in snake:
            there = snake[there]
        
        if dist[there] is None or roll < dist[there]:
            dist[there] = roll
            if there != 100:
                queue.append((there, roll))

sys.stdout.write(str(dist[100]))