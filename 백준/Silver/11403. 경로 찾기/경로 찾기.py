def main():
    import sys
    
    input = sys.stdin.readline
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    dist = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                dist[i][j] = 1
            else:
                dist[i][j] = INF
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    for i in range(N):
        for j in range(N):
            sys.stdout.write('1 ' if dist[i][j] != INF else '0 ')
        sys.stdout.write('\n')


if __name__ == '__main__':
    main()