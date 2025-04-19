def main():
    from heapq import heappush, heappop, heapify
    import sys
    
    readline = sys.stdin.readline
    
    N, D = map(int, readline().split())
    adj = {0: {}, D: {}}
    for _ in range(N):
        u, v, d = map(int, readline().split())
        if v > D or d >= v - u:
            continue

        if u not in adj:
            adj[u] = {}
        if v not in adj:
            adj[v] = {}
            
        if v in adj[u]:
            adj[u][v] = min(adj[u][v], d)
        else:
            adj[u][v] = d
            
    dist = {v: v for v in adj}
    dist[0] = 0
    pq = [(v, v) for v in adj]
    heapify(pq)
    while pq:
        d1, u = heappop(pq)
        if d1 > dist[u]:
            continue
        for v in adj:
            if v <= u:
                continue
            d2 = v - u if v not in adj[u] else adj[u][v]
            if dist[v] > d1 + d2:
                dist[v] = d1 + d2
                heappush(pq, (dist[v], v))
    
    print(dist[D])


if __name__ == "__main__":
    main()