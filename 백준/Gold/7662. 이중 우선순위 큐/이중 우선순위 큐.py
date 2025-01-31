import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    last_id = 0
    deleted = []
    
    for id_ in range(N):
        op, num = sys.stdin.readline().split()
        num = int(num)
        if op == 'I':
            heapq.heappush(min_heap, (num, last_id))
            heapq.heappush(max_heap, (-num, last_id))
            deleted.append(False)
            last_id += 1
        elif num == 1:
            while max_heap:
                num, id_ = heapq.heappop(max_heap)
                if not deleted[id_]:
                    deleted[id_] = True
                    break
        else:
            while min_heap:
                num, id_ = heapq.heappop(min_heap)
                if not deleted[id_]:
                    deleted[id_] = True
                    break
    
    max_ = None
    while max_heap:
        num, id_ = heapq.heappop(max_heap)
        if max_ is None and not deleted[id_]:
            max_ = -num
            break
    
    min_ = None
    while min_heap:
        num, id_ = heapq.heappop(min_heap)
        if min_ is None and not deleted[id_]:
            min_ = num
            break
    
    if max_ is None:
        sys.stdout.write('EMPTY\n')
    else:
        sys.stdout.write(f'{max_} {min_}\n')