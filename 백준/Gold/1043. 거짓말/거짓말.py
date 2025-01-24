import sys
from collections import deque

readline = sys.stdin.readline

N, M = map(int, readline().split())
K, *informed = map(int, readline().split())

parties = {i: list() for i in range(1, N + 1)}
graph = {i: set() for i in range(1, N + 1)}
for party in range(M):
    __, *participants = map(int, readline().split())
    for i, person in enumerate(participants):
        parties[person].append(party)
        graph[person].update(participants[:i])
        graph[person].update(participants[i + 1:])

def count_informed_party():
    visited = []
    informed_parties = set()
    for i in range(1, N + 1):
        if i in visited:
            continue
        group = []
        is_informed_group = False
        queue = deque([i])
        while queue:
            here = queue.popleft()
            if here in informed:
                is_informed_group = True
                group.append(here)
            for there in graph[here]:
                if there in visited:
                    continue
                visited.append(there)
                queue.append(there)
                group.append(there)
        if is_informed_group:
            for person in group:
                informed_parties.update(parties[person])
    return len(informed_parties)

sys.stdout.write(str(M - count_informed_party()))