def main():
    import sys
    from bisect import bisect_left
    
    N, *arr = map(int, sys.stdin.read().split())
    
    lis_ends_with = [1] * N
    lis = []
    for i, v in enumerate(arr):
        idx = bisect_left(lis, v)
        if idx == len(lis):
            lis.append(v)
        else:
            lis[idx] = v
        lis_ends_with[i] = idx + 1
    
    lds_starts_with = [1] * N
    lds = []
    for i in range(N - 1, -1, -1):
        v = arr[i]
        idx = bisect_left(lds, v)
        if idx == len(lds):
            lds.append(v)
        else:
            lds[idx] = v
        lds_starts_with[i] = idx + 1
    
    sys.stdout.write(str(max(map(sum, zip(lis_ends_with, lds_starts_with))) - 1))


if __name__ == '__main__':
    main()