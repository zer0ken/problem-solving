def main():
    import sys
    from collections import deque

    readline = sys.stdin.readline
    write = sys.stdout.write

    N, M = map(int, readline().split())

    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b, d = map(int, readline().split())
        tree[a].append((b, d))
        tree[b].append((a, d))


    for _ in range(M):
        start, target = map(int, readline().split())
        
        queue = deque([(start, 0)])
        visited = [0] * (N + 1)
        visited[start] = 1
        while queue:
            here, dist = queue.popleft()
            if here == target:
                write(f'{dist}\n')
                break
            for there, delta_dist in tree[here]:
                if not visited[there]:
                    visited[there] = 1
                    queue.append((there, dist + delta_dist))


if __name__ == '__main__':
    main()