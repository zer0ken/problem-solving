def main():
    import sys
    import heapq

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    INF = float('inf')
    
    N = int(readline())
    M = int(readline())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e, d = map(int, readline().split())
        graph[s].append((e, d))
    departure, arrival = map(int, readline().split())
    
    dist = [INF] * (N + 1)
    dist[departure] = 0
    
    path = [[] for _ in range(N + 1)]
    
    pq = [(0, departure)]
    while pq:
        d_prev, cur = heapq.heappop(pq)
        if d_prev > dist[cur]:
            continue
        for next, d_next in graph[cur]:
            if dist[next] > d_prev + d_next:
                dist[next] = d_prev + d_next
                path[next] = path[cur] + [cur]
                heapq.heappush(pq, (dist[next], next))

    path[arrival].append(arrival)
    
    write(f'{dist[arrival]}\n{len(path[arrival])}\n{" ".join(map(str, path[arrival]))}')


if __name__ == '__main__':
    main()