def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, Q = map(int, readline().split())
    difficulties = list(map(int, readline().split()))
    
    lis = []
    lis_of = [0] * N
    for i, d in enumerate(difficulties):
        idx = bisect_left(lis, d)
        if idx == len(lis):
            lis.append(d)
        else:
            lis[idx] = d
        lis_of[i] = idx
        
    lds = []
    lds_of = [0] * N
    for i in range(N - 1, -1, -1):
        d = -difficulties[i]
        idx = bisect_left(lds, d)
        if idx == len(lds):
            lds.append(d)
        else:
            lds[idx] = d
        lds_of[i] = idx
        
    for _ in range(Q):
        must_solve = int(readline()) - 1
        write(f'{1 + lis_of[must_solve] + lds_of[must_solve]}\n')


if __name__ == '__main__':
    main()