def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    graph = [set() for _ in range(N + 1)]
    incomming = [0] * (N + 1)
    
    for _ in range(M):
        order = list(map(int, readline().split()))
        for i in range(1, len(order)):
            a = order[i]
            for j in range(i + 1, len(order)):
                b = order[j]
                if b not in graph[a]:
                    graph[a].add(b)
                    incomming[b] += 1
    
    queue = deque()
    for i in range(1, N + 1):
        if incomming[i] == 0:
            queue.append(i)
    
    lined_up = []
    while queue:
        cur = queue.popleft()
        lined_up.append(cur)
        
        for next_ in graph[cur]:
            incomming[next_] -= 1
            if incomming[next_] == 0:
                queue.append(next_)

    if len(lined_up) < N:
        write('0')
        exit(0)
    
    for i in lined_up:
        write(f'{i}\n')


if __name__ == '__main__':
    main()