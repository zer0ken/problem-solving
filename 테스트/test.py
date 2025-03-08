def main():
    import sys
    from bisect import bisect_right
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    A = list(map(int, readline().split()))
    M = int(readline())
    B = list(map(int, readline().split()))
    
    dlcs = []
    
    for i, x in sorted(enumerate(A), key=lambda x: (-x[1], x[0])):
        if dlcs and i < dlcs[-1][0]:
            continue
        j_start = dlcs[-1][1] + 1 if dlcs else 0
        if x in B[j_start:]:
            j = B.index(x, j_start)
            if dlcs and j <= dlcs[-1][1]:
                continue
            dlcs.append((i, j, x))

    write(str(len(dlcs)))
    if dlcs:
        write(f'\n{" ".join(str(x) for _, _, x in dlcs)}')
    

if __name__ == '__main__':
    main()