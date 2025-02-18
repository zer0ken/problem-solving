def main():
    import sys
    
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
    
    for p1 in range(len(edges1)):
        for p2 in range(len(edges2)):
            get_chain(p1, p2)
            get_chain(p1, p2, reverse=True)
    
    
    def is_crossing(p1, p2):
        s1, e1 = edges[edges1[p1]]
        s2, e2 = edges[edges2[p2]]
        return (s1 - s2) * (e1 - e2) < 0

    def get_chain(p1, p2, reverse=False):
        """
        If not reversed,
            edges1 -> edges2 -> edges1 -> edges2 -> ...
        Otherwise,
            edges2 -> edges1 -> edges2 -> edges1 -> ...
        """
        on_edges1 = not reverse
        chain = 2
        while p1 < len(edges1) and p2 < len(edges2):
            if on_edges1:
                if not is_crossing(p1, p2 + 1):
                    break
                p2 += 1
            elif not is_crossing(p1 + 1, p2):
                break
            else:
                p1 += 1
            chain += 1
            on_edges1 = not on_edges1


if __name__ == '__main__':
    main()