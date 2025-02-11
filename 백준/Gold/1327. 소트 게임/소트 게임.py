def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, K = map(int, readline().split())
    start = tuple(map(int, readline().split()))
    end = tuple(i for i in range(1, N + 1))
    
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        here, dist = queue.popleft()
        if here == end:
            write(str(dist))
            exit(0)
        
        for i in range(0, N - K + 1):
            there = here[:i] + here[i:i+K][::-1] + here[i+K:]
            if there not in visited:
                visited.add(there)
                queue.append((there, dist + 1))
    write('-1')


if __name__ == '__main__':
    main()