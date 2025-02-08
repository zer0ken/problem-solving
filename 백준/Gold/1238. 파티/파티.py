def main():
    import sys
    import heapq
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M, X = map(int, readline().split())
    X -= 1
    INF = float('inf')
    edges = [[INF] * N for _ in range(N)]
    for _ in range(M):
        i, j, cost = map(int, readline().split())
        i -= 1
        j -= 1
        if edges[i][j] > cost:
            edges[i][j] = cost
    
    dist1 = [INF] * N
    dist1[X] = 0
    heap = [(0, X)]
    for _ in range(N - 1):
        cost, here = heapq.heappop(heap)
        while dist1[here] != cost:
            cost, here = heapq.heappop(heap)
        
        for there in range(N):
            next_cost = cost + edges[here][there]
            if dist1[there] > next_cost:
                dist1[there] = next_cost
                heapq.heappush(heap, (dist1[there], there))

    dist2 = [INF] * N
    dist2[X] = 0
    heap = [(0, X)]
    for _ in range(N - 1):
        cost, here = heapq.heappop(heap)
        while dist2[here] != cost:
            cost, here = heapq.heappop(heap)
        
        for there in range(N):
            next_cost = cost + edges[there][here]
            if dist2[there] > next_cost:
                dist2[there] = next_cost
                heapq.heappush(heap, (dist2[there], there))
                
    max_dist = 0
    for i in range(N):
        dist = dist1[i] + dist2[i]
        if max_dist < dist:
            max_dist = dist
    sys.stdout.write(str(max_dist))


if __name__ == '__main__':
    main()