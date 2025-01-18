import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    flip = False
    ops = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip()
    arr = arr[1:-1].split(',')
    err = False
    
    for op in ops:
        if op == 'R':
            flip = not flip
            continue
        
        if n == 0:
            err = True
            break
        
        if flip:
            arr.pop(-1)
        else:
            arr.pop(0)
        n -= 1
        
    if err:
        sys.stdout.write('error\n')
    elif flip:
        sys.stdout.write('[' + ','.join(arr[::-1]) + ']\n')
    else:
        sys.stdout.write('[' + ','.join(arr) + ']\n')