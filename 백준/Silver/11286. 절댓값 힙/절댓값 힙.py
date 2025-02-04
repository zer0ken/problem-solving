import heapq
input = iter(open(0).read().split('\n')).__next__

heap = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print('0')
    else:
        heapq.heappush(heap, (abs(num), num))