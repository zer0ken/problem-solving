def solution(n, results):
    graph = [[] for _ in range(n + 1)]
    
    for a, b in results:
        graph[a].append(b)
    
    dp = [None] * (n + 1)
    
    def get_subnodes(x):
        if dp[x] is not None:
            return dp[x]
        
        subnodes = set()
        for child in graph[x]:
            subnodes.add(child)
            subnodes.update(get_subnodes(child))
        
        subnodes = frozenset(subnodes)
        dp[x] = subnodes
        return subnodes
        
    compared_count = [0] * (n + 1)
    
    for i in range(1, n + 1):
        subnodes = get_subnodes(i)
        compared_count[i] += len(subnodes)

        for subnode in get_subnodes(i):
            compared_count[subnode] += 1
    
    ranked = len(list(filter(lambda c: c == n - 1, compared_count)))
    
    print('\n'.join(map(str, dp)))
    return ranked

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))