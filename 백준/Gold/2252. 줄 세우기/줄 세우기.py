def main():
    import sys
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
    newly_lined_up = []
    while len(lined_up) < N:
        for i in range(1, N + 1):
            if incoming[i] == 0:
                newly_lined_up.append(i)
                lined_up.append(i)
                incoming[i] = -1
        while newly_lined_up:
            cur = newly_lined_up.pop()
            for next_ in graph[cur]:
                incoming[next_] -= 1

    write(' '.join(map(str, lined_up)))


if __name__ == '__main__':
    main()