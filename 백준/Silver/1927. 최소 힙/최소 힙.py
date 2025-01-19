import sys
import heapq

n = int(sys.stdin.readline().rstrip())

heap = []
for _ in range(n):
    op = int(sys.stdin.readline().rstrip())
    if op == 0:
        if heap:
            sys.stdout.write(f'{heapq.heappop(heap)}\n')
        else:
            sys.stdout.write('0\n')
    else:
        heapq.heappush(heap, op)