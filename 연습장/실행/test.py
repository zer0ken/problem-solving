def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write

    N = int(readline())
    edges = [tuple(map(int, readline().split())) for _ in range(N)]
    edges.sort()    
    cross = [[0] * N for _ in range(N)]
    
    for i in range(1, N):
        for j in range(i):
            if edges[j][1] > edges[i][1]:
                cross[i][j] = 1
                cross[j][i] = 1
    
    visited = [False] * N
    queue = deque([0])
    max_count = 0
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        queue = deque([i])
        count = 1
        while queue:
            here = queue.popleft()
            for there in range(N):
                if cross[here][there] and not visited[there]:
                    visited[there] = True
                    queue.append(there)
                    count += 1
        if max_count < count:
            max_count = count
    write(str(max_count))


if __name__ == '__main__':
    main()