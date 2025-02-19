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
    
    max_chain = 1
    p1, p2 = 0, 0
    while p1 < len(edges1) and p2 < len(edges2) and (N - p1 - p2 > max_chain): # 남은 선분 수가 최대 체인보다 적으면 종료
        s1, e1 = edges[edges1[p1]]
        s2, e2 = edges[edges2[p2]]
        if (s1 - s2) * (e1 - e2) < 0:
            chain = 2
            on_edges1 = True
            pp1 = p1
            pp2 = p2 + 1
            while pp1 < len(edges1) and pp2 < len(edges2):
                s1, e1 = edges[edges1[pp1]]
                s2, e2 = edges[edges2[pp2]]
                if (s1 - s2) * (e1 - e2) < 0:
                    chain += 1
                    on_edges1 = not on_edges1
                if on_edges1:
                    pp2 += 1
                else:
                    pp1 += 1
            if max_chain < chain:
                max_chain = chain
            
            chain = 2
            on_edges1 = False
            pp1 = p1 + 1
            pp2 = p2
            while pp1 < len(edges1) and pp2 < len(edges2):
                s1, e1 = edges[edges1[pp1]]
                s2, e2 = edges[edges2[pp2]]
                if (s1 - s2) * (e1 - e2) < 0:
                    chain += 1
                    on_edges1 = not on_edges1
                if on_edges1:
                    pp2 += 1
                else:
                    pp1 += 1
            if max_chain < chain:
                max_chain = chain
            
            p1 += 1
            p2 += 1
        elif edges[edges1[p1]][0] < edges[edges2[p2]][0]:
            p1 += 1
        else:
            p2 += 1
    write(str(max_chain))


if __name__ == '__main__':
    main()