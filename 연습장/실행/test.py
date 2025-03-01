def main():
    import sys
    import heapq
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, K = map(int, readline().split())
    
    jewels = [tuple(map(int, readline().split())) for _ in range(N)]
    weight_limits = [int(readline()) for _ in range(K)]
    
    jewels.sort()
    weight_limits.sort()
    
    pq = []
    stolen = 0
    bag = 0
        
    for weight, price in jewels:
        while bag < K and weight > weight_limits[bag]:
            bag += 1
            if pq:
                stolen += -heapq.heappop(pq)
        if bag == K:
            break
        heapq.heappush(pq, -price)
    else:
        while bag < K and pq:
            bag += 1
            stolen += -heapq.heappop(pq)
    
    write(str(stolen))


if __name__ == '__main__':
    main()