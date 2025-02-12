def main():
    import sys
    import heapq
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    INF = float('inf')
    
    N, E = map(int, readline().split())
    edges = [[0 if i == j else INF for j in range(N)] for i in range(N)]
    for _ in range(E):
        u, v, d = map(int, readline().split())
        u -= 1
        v -= 1
        edges[u][v] = min(edges[u][v], d)
        edges[v][u] = min(edges[v][u], d)
    V1, V2 = map(int, readline().split())
    V1 -= 1
    V2 -= 1
    
    S = 0
    E = N - 1
    
    def dijkstra(start, end):
        if start == end:
            return 0
        dist = [INF] * N
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            d, i = heapq.heappop(heap)
            if dist[i] < d:
                continue
            for j in range(N):
                if dist[j] > d + edges[i][j]:
                    dist[j] = d + edges[i][j]
                    heapq.heappush(heap, (dist[j], j))
        return dist[end]
            
    dist1 = dijkstra(S, V1) + dijkstra(V1, V2) + dijkstra(V2, E)
    dist2 = dijkstra(S, V2) + dijkstra(V2, V1) + dijkstra(V1, E)
    dist = dist1 if dist1 < dist2 else dist2
    if dist >= INF:
        dist = -1
    write(str(dist))


if __name__ == '__main__':
    main()