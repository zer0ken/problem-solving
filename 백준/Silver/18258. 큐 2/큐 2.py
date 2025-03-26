import sys
from collections import deque

def main():
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    queue = deque()
    results = []
    for _ in range(N):
        op = next(tokens)
        if op == 'push':
            queue.append(int(next(tokens)))
        elif op == 'pop':
            results.append(queue.popleft() if queue else -1)
        elif op == 'size':
            results.append(len(queue))
        elif op == 'empty':
            results.append(int(not queue))
        elif op == 'front':
            results.append(queue[0] if queue else -1)
        else:
            results.append(queue[-1] if queue else -1)
    
    sys.stdout.write('\n'.join(map(str, results)))


main()