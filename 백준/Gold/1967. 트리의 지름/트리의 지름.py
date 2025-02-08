def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    
    N = int(readline())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        i, j, w = map(int, readline().split())
        tree[i].append((j, w))
        tree[j].append((i, w))
    
    queue = deque([(1, 0)])
    visited = [0] * (N + 1)
    visited[1] = 1
    farthest = 0
    farthest_node = 0
    while queue:
        here, dist = queue.popleft()
        is_terminal = 1
        for there, weight in tree[here]:
            if visited[there]:
                continue
            is_terminal = 0
            visited[there] = 1
            queue.append((there, dist + weight))
        if is_terminal and farthest < dist:
            farthest = dist
            farthest_node = here
    
    queue.append((farthest_node, 0))
    visited = [0] * (N + 1)
    visited[farthest_node] = 1
    farthest = 0
    while queue:
        here, dist = queue.popleft()
        is_terminal = 1
        for there, weight in tree[here]:
            if visited[there]:
                continue
            is_terminal = 0
            visited[there] = 1
            queue.append((there, dist + weight))
        if is_terminal and farthest < dist:
            farthest = dist
            
    sys.stdout.write(str(farthest))


if __name__ == '__main__':
    main()