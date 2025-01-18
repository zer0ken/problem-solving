import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
box = []
queue = deque()
left = 0

for h in range(H):
    pallete = []
    for n in range(N):
        line = []
        raw = sys.stdin.readline().rstrip().split()
        for m in range(M):
            tomato = int(raw[m])
            
            if tomato == 0:
                left += 1
            elif tomato == 1:
                queue.append((h, n, m))
            
            line.append(tomato)
        pallete.append(line)
    box.append(pallete)

dhs = (1, -1, 0, 0, 0, 0)
dns = (0, 0, 1, -1, 0, 0)
dms = (0, 0, 0, 0, 1, -1)

timestamp = 0
while queue and left > 0:
    h, n, m = queue.popleft()
    timestamp = box[h][n][m]
    for dh, dn, dm in zip(dhs, dns, dms):
        nh, nn, nm = (h + dh, n + dn, m + dm)
        
        if any((
            nh < 0, nn < 0, nm < 0,
            nh >= H, nn >= N, nm >= M
        )):
            continue
          
        if box[nh][nn][nm] == 0:
            box[nh][nn][nm] = timestamp + 1
            left -= 1
            queue.append((nh, nn, nm))
            
if left:
    sys.stdout.write('-1')
else:
    sys.stdout.write(str(timestamp))