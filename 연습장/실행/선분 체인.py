def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    edges = [tuple(map(int, readline().split()))for _ in range(N)]
    edges.sort()
    
    as_arm = [None] * N
    arms = [None] * N 
    end = []
    for i, (s, e) in enumerate(edges):
        k = bisect_left(end, (e, i))
        if k == len(end):
            end.append((e, i))
        else:
            for j in range(k, len(end)):
                _, e_ = end[j]
                if arms[e_] is None or len(as_arm[arms[e_]]) ==  0:
                    break
            arms[e_] = i
            as_arm[i] = [end[jj][1] for jj in range(j + 1, len(end))]
            if k != 0:
                end = end[k:]

    for i, interval in enumerate(edges):
        print(f'#{i} {interval}')
        if as_arm[i] is not None:
            print(f'\tit is arm: {as_arm[i]}')
        elif arms[i] is not None:
            print(f'\tit has arm: {arms[i]}, {as_arm[arms[i]]}')
        else:
            print(f'\tno arm...')
            
    print('-'*30)
    
    chain = 1
    max_chain = 1
    i = 0
    while i < N:
        print(f'#{i} {edges[i]}')
        if arms[i] is None:
            if max_chain < chain:
                max_chain = chain
            chain = 1
            i += 1
            print(f'\t.')
        else:
            best_next = None
            chain += 1
            for next_ in as_arm[arms[i]]:
                if best_next is None or (arms[best_next] is None and arms[next_] is not None):
                    best_next = next_
            if best_next is None:
                i += 2
            else:
                chain += 1
                i = best_next
            print(f'\t-> {best_next}')
            
    if max_chain < chain:
        max_chain = chain
        
    print(max_chain)


if __name__ == '__main__':
    main()