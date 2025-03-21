def main():
    import sys
    from bisect import bisect_left

    N, *arr = map(int, sys.stdin.read().split())
    
    lis = []
    indices = []
    backtrack = [None] * N
    for i, v in enumerate(arr):
        idx = bisect_left(lis, v)
        if idx == len(lis):
            lis.append(v)
            indices.append(i)
        else:
            lis[idx] = v
            indices[idx] = i
        
        if idx != 0:
            backtrack[i] = indices[idx-1]
    
    lis = []
    cur = indices[-1]
    while cur is not None:
        lis.append(arr[cur])
        cur = backtrack[cur]
    lis.reverse()
    
    sys.stdout.write(f'{len(lis)}\n{" ".join(map(str, lis))}')


if __name__ == '__main__':
    main()