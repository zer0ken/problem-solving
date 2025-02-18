def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    edges = [tuple(map(int, readline().split()))for _ in range(N)]
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
        
    write(str(max_chain))


if __name__ == '__main__':
    main()