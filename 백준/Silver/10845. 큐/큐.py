import sys
from collections import deque

readline = sys.stdin.readline
n = int(readline().rstrip())

queue = deque()
for _ in range(n):
    op, *args = readline().split()
    if op == 'push':
        queue.append(args[0])
    elif op == 'pop':
        sys.stdout.write(f'{queue.popleft() if queue else -1}\n')
    elif op == 'size':
        sys.stdout.write(f'{len(queue)}\n')
    elif op == 'empty':
        sys.stdout.write(f'{1 if not queue else 0}\n')
    elif op == 'front':
        sys.stdout.write(f'{queue[0] if queue else -1}\n')
    elif op == 'back':
        sys.stdout.write(f'{queue[-1] if queue else -1}\n')