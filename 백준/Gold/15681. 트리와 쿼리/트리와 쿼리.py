def main():
    import sys
    
    sys.setrecursionlimit(10**6)
    
    lines = iter(sys.stdin.read().rstrip().splitlines())
    
    N, R, Q = map(int, next(lines).split())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        U, V = map(int, next(lines).split())
        tree[U].append(V)
        tree[V].append(U)
    
    dp = [0] * (N + 1)
    
    def size_subtree(root):
        dp[root] = 1
        for child in tree[root]:
            if dp[child] == 0:
                size_subtree(child)
                dp[root] += dp[child]
        
    size_subtree(R)
    
    sys.stdout.write('\n'.join(str(dp[int(query)]) for query in lines))


if __name__ == '__main__':
    main()