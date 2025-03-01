def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    graph = [[] for _ in range(N + 1)]
    incoming = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, readline().split())
        graph[a].append(b)
        incoming[b] += 1
    
    lined_up = []
    queue = deque()
    for i in range(1, N + 1):
        if incoming[i] == 0:
            queue.append(i)
            incoming[i] = -1
    while queue:
        cur = queue.popleft()
        lined_up.append(cur)
        for next_ in graph[cur]:
            incoming[next_] -= 1
            if incoming[next_] == 0:
                queue.append(next_)

    write(' '.join(map(str, lined_up)))


if __name__ == '__main__':
    main()