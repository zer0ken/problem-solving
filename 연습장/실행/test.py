def main():
    import sys
    from functools import cache
    
    sys.setrecursionlimit(100000000000)
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    edges = [tuple(map(int, readline().split())) for i in range(N)]
    edges.sort()
    
    edges1 = []
    edges2 = []
    
    max_end = -1
    for i, (start, end) in enumerate(edges):
        if max_end > end:
            edges2.append(i)
        else:
            edges1.append(i)
            max_end = end
    
    
    def is_crossing(p1, p2):
        nonlocal edges, edges1, edges2
        
        s1, e1 = edges[edges1[p1]]
        s2, e2 = edges[edges2[p2]]
        return (s1 - s2) * (e1 - e2) < 0
    
    
    @cache
    def get_chain(pp1, pp2, reverse=False):
        """
        If not reversed,
            (edges1 -> edges2) -> edges1 -> edges2 -> ...
        Otherwise,
            (edges2 -> edges1) -> edges2 -> edges1 -> ...
        """
        nonlocal edges1, edges2
        
        on_edges1 = reverse
        if on_edges1:
            pp2 += 1
        else:
            pp1 += 1

        if pp1 >= len(edges1) or pp2 >= len(edges2):
            return 0
        if is_crossing(pp1, pp2):
            return 1 + get_chain(pp1, pp2, not on_edges1)
        return get_chain(pp1, pp2, on_edges1)
    
    
    max_chain = 1
    p1, p2 = 0, 0
    while p1 < len(edges1) and p2 < len(edges2):
        if is_crossing(p1, p2):
            max_chain = max(max_chain, 2 + get_chain(p1, p2), 2 + get_chain(p1, p2, reverse=True))
            p1 += 1
            p2 += 1
        elif edges[edges1[p1]][0] < edges[edges2[p2]][0]:
            p1 += 1
        else:
            p2 += 1
    write(str(max_chain))


if __name__ == '__main__':
    main()