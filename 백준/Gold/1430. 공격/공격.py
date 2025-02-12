def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, R, D, X, Y = map(int, readline().split())
    towers = [tuple(map(int, readline().split())) for _ in range(N)]
    
    dist = [0] * N
    queue = deque([(X, Y, 0)])
    
    while queue:
        x, y, d = queue.popleft()

        for i, (nx, ny) in enumerate(towers):
            if not dist[i] and ((x - nx) ** 2 + (y - ny) ** 2) ** 0.5 <= R:
                dist[i] = d + 1
                queue.append((nx, ny, d + 1))
    
    damage = 0
    for i in range(N):
        if dist[i]:
            damage += D / (2 ** (dist[i] - 1))

    write(str(damage))


if __name__ == '__main__':
    main()