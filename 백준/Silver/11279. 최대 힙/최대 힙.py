import sys
import heapq

heap = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        sys.stdout.write(f'{-heapq.heappop(heap)}\n' if heap else '0\n')
    else:
        heapq.heappush(heap, -num)