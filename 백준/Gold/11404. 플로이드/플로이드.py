def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    M = int(readline())
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    
    for _ in range(M):
        i, j, cost = map(int, readline().split())
        i -= 1
        j -= 1
        if dist[i][j] > cost:
            dist[i][j] = cost
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    dist[i][j] = 0
                elif dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    for i in range(N):
        for d in dist[i]:
            if d >= INF:
                write(f'0 ')
            else:
                write(f'{d} ')
        write('\n')


if __name__ == '__main__':
    main()