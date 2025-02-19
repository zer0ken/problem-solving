def main():
    import sys
<<<<<<< HEAD
=======
    from bisect import bisect_left
>>>>>>> f1ff55406781d85a9286ee6add36712209b1a04f
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
<<<<<<< HEAD
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
=======
    edges = [tuple(map(int, readline().split()))for _ in range(N)]
    edges.sort(key=lambda x: x[1])
    edges.sort()
    
    as_arm = [None] * N
    arm_of = [None] * N 
    end = []
    for i, (s, e) in enumerate(edges):
        k = bisect_left(end, (e, i))
        if k == len(end):
            end.append((e, i))
        else:
            for j in range(k, len(end)):
                _, e_ = end[j]
                if arm_of[e_] is None or len(as_arm[arm_of[e_]]) ==  0:
                    break
            arm_of[e_] = i
            as_arm[i] = [end[jj][1] for jj in range(j + 1, len(end))]
            if k != 0:
                end = end[k:]

    chain = 1
    max_chain = 1
    i = 0
    while i < N:
        if arm_of[i] is None:
            if max_chain < chain:
                max_chain = chain
            chain = 1
            i += 1
        else:
            best_next = None
            chain += 1
            for next_ in as_arm[arm_of[i]]:
                if best_next is None or arm_of[best_next] is None:
                    best_next = next_
            if best_next is None:
                i += 2
            else:
                chain += 1
                i = best_next
            
    if max_chain < chain:
        max_chain = chain
        
>>>>>>> f1ff55406781d85a9286ee6add36712209b1a04f
    write(str(max_chain))


if __name__ == '__main__':
    main()