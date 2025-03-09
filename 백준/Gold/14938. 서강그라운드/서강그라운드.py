def main():
    import sys

    sys.setrecursionlimit(100)
    readline = sys.stdin.readline
    write = sys.stdout.write

    INF = float('inf')
    N, M, R = map(int, readline().split())
    values = list(map(int, readline().split()))
    graph = [[0 if i == j else INF for j in range(N)] for i in range(N)]
    for _ in range(R):
        a, b, l = map(int, readline().split())
        a -= 1
        b -= 1
        if graph[a][b] > l:
            graph[a][b] = l
        if graph[b][a] > l:
            graph[b][a] = l
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    max_value = 0
    for i in range(N):
        value = 0
        for j in range(N):
            if graph[i][j] <= M:
                value += values[j]
        if max_value < value:
            max_value = value
    
    write(str(max_value))        


if __name__ == '__main__':
    main()