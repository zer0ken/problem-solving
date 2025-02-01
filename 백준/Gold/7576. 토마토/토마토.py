import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = []
queue = deque()
left = 0

for n in range(N):
    line = []
    raw = sys.stdin.readline().rstrip().split()
    for m in range(M):
        tomato = int(raw[m])
        
        if tomato == 0:
            left += 1
        elif tomato == 1:
            queue.append((n, m))
        line.append(tomato)
    box.append(line)

dns = (1, -1, 0, 0)
dms = (0, 0, 1, -1)

timestamp = 0
while queue and left > 0:
    n, m = queue.popleft()
    timestamp = box[n][m]
    for dn, dm in zip(dns, dms):
        nn, nm = (n + dn, m + dm)
        
        if any((
            nn < 0, nm < 0,
            nn >= N, nm >= M
        )):
            continue
            
        if box[nn][nm] == 0:
            box[nn][nm] = timestamp + 1
            left -= 1
            queue.append((nn, nm))
            
if left:
    sys.stdout.write('-1')
else:
    sys.stdout.write(str(timestamp))