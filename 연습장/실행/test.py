def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    INF = float('inf')
    
    for _ in range(int(readline())):
        N, M, W = map(int, readline().split())
        edges = []
        for _ in range(M):
            s, e, t = map(int, readline().split())
            s -= 1
            e -= 1
            edges.append((s, e, t))
            edges.append((e, s, t))
        for _ in range(W):
            s, e, t = map(int, readline().split())
            s -= 1
            e -= 1
            edges.append((s, e, -t))

        visited = [0] * N
        for start in range(N):
            if visited[start]:
                continue
            visited[start] = 1
            dist = [INF] * N
            dist[start] = 0
            for loop in range(N):
                for s, e, t in edges:
                    if dist[s] < INF and dist[e] > dist[s] + t:
                        visited[e] = 1
                        dist[e] = dist[s] + t
                        if loop == N - 1:
                            write('YES\n')
                            break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            write('NO\n')


if __name__ == '__main__':
    main()