def main():
    import sys
    from collections import deque
    
    input = sys.stdin.readline
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    path = [[0] * N for _ in range(N)]
    visited = [0] * N
    
    for i in range(N):
        visited = [0] * N
        queue = deque()
        for j in range(N):
            if graph[i][j]:
                queue.append(j)
                visited[j] = 1
                path[i][j] = 1
        while queue:
            k = queue.popleft()
            for j in range(N):
                if graph[k][j] and not visited[j]:
                    queue.append(j)
                    visited[j] = 1
                    path[i][j] = 1
        sys.stdout.write(' '.join(map(str, path[i])) + '\n')


if __name__ == '__main__':
    main()