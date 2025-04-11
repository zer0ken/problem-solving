def main():
    import sys

    stdin = sys.stdin.read().rstrip().splitlines().__iter__()
    input = stdin.__next__
    
    
    N, M, K, X = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for line in stdin:
        A, B = map(int, line.split())
        adj[A].append(B)
        
    found = [0] * (N + 1)
    
    visited = [0] * (N + 1)
    visited[X] = 1
    queue = [(X, 0)]
    while queue:
        cur, dist = queue.pop(0)
        if dist == K:
            found[cur] = 1
            continue
        dist += 1
        for next_ in adj[cur]:
            if not visited[next_]:
                visited[next_] = 1
                queue.append((next_, dist))    
    
    if any(found):
        print(*(i for i in range(1, N + 1) if found[i]), sep='\n')
    else:
        print('-1')

if __name__ == '__main__':
    main()