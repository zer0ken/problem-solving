def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    weights = [int(readline()) for _ in range(N)]

    max_train = 0
    for i in range(N):
        base_w = weights[i]
        lis = []
        lds = []
        for j in range(i + 1, N):
            w = weights[j]
            if w > base_w:
                idx = bisect_left(lis, w)
                if idx == len(lis):
                    lis.append(w)
                else:
                    lis[idx] = w
            elif w < base_w:
                idx = bisect_left(lds, -w)
                if idx == len(lds):
                    lds.append(-w)
                else:
                    lds[idx] = -w
        train = len(lis) + len(lds) + 1
        if max_train < train:
            max_train = train
    
    write(str(max_train))


if __name__ == '__main__':
    main()