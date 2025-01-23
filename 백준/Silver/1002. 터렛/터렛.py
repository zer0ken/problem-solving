import sys
readline = sys.stdin.readline
write = sys.stdout.write

T = int(readline().rstrip())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, readline().split())
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            write('-1\n')
        else:
            write('0\n')
        continue
        
    dx = x2 - x1
    dy = y2 - y1
    d = (dx*dx + dy*dy) ** 0.5
    
    dr = abs(r2 - r1)
    ar = r1 + r2
    
    if d < dr:
        write('0\n')
    elif d == dr:
        write('1\n')
    elif dr < d < ar:
        write('2\n')
    elif d == ar:
        write('1\n')
    else:
        write('0\n')