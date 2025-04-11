def main():
    import sys
    from collections import deque

    stdin = sys.stdin.read().rstrip().splitlines().__iter__()
    input = stdin.__next__
    
    
    N, M, K, X = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for line in stdin:
        A, B = map(int, line.split())
        adj[A].append(B)
        
    visited = [False] * (N + 1)
    visited[X] = True
    found = []
    queue = deque([(X, 0)])
    while queue:
        cur, dist = queue.popleft()
        if dist == K:
            found.append(cur)
            continue
        dist += 1
        for next_ in adj[cur]:
            if not visited[next_]:
                visited[next_] = True
                queue.append((next_, dist))    
    
    if found:
        found.sort()
        print(*found, sep='\n')
    else:
        print('-1')

if __name__ == '__main__':
    main()