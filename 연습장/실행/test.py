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
    
    
    def is_crossing(edge1, edge2):
        s1, e1 = edges[edge1]
        s2, e2 = edges[edge2]
        return (s1 - s2) * (e1 - e2) < 0

    p1 = 0 # pointer on edges1
    p2 = 0 # pointer on edges2
    chain = []
    while p1 < len(edges1) and p2 < len(edges2):
        edge1 = edges1[p1]
        edge2 = edges2[p2]
        
        if is_crossing(edge1, edge2):
            pass
        elif edges1 < edges2:
            p1 += 1
        else:
            p2 += 1

if __name__ == '__main__':
    main()