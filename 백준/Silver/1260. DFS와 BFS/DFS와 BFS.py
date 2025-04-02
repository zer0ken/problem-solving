def main():
    import sys
    from collections import deque
    
    N, M, V = map(int, sys.stdin.readline().split())
    adj = [set() for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].add(b)
        adj[b].add(a)
    adj = [sorted(adj[x]) for x in range(N + 1)]
    
    visited = [0] * (N + 1)
    dfs_results = [V]
    
    def dfs(cur):
        nonlocal N, M, V, adj, visited, dfs_results
        
        visited[cur] = 1
        for next in adj[cur]:
            if not visited[next]:
                dfs_results.append(next)
                dfs(next)
    
    dfs(V)
    
    bfs_results = []
    visited = [0] * (N + 1)
    visited[V] = 1
    queue = deque([V])
    
    while queue:
        cur = queue.popleft()
        bfs_results.append(cur)
        
        for next in adj[cur]:
            if not visited[next]:
                visited[next] = 1
                queue.append(next)
    
    print(*dfs_results)
    print(*bfs_results)


if __name__ == '__main__':
    main()