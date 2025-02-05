import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    
    backtrack = [None for _ in range(10000)]
    last_op = [None for _ in range(10000)]
    last_op[A] = -1
    
    queue = deque([A])
    
    while queue:
        here = queue.popleft()
        for op in range(4):
            if op == 0:
                there = here * 2 % 10000
            elif op == 1:
                there = here - 1 if here != 0 else 9999
            elif op == 2:
                there = here % 1000 * 10 + here // 1000
            elif op == 3:
                there = here // 10 + here % 10 * 1000
            
            if last_op[there] is not None:
                continue
            
            last_op[there] = op
            backtrack[there] = here
            
            if there == B:
                break
            
            queue.append(there)
            
        if there == B:
            break
    ops = []
    cur = B
    while cur != A:
        ops.append('DSLR'[last_op[cur]])
        cur = backtrack[cur]
    sys.stdout.write(''.join(ops[::-1]) + '\n')