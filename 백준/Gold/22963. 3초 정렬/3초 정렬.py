def main():
    import sys
    from bisect import bisect_right
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    arr = list(map(int, readline().split()))
    
    backtrack = {}
    lis = []
    lis_i = []
    for i, v in enumerate(arr):
        idx = bisect_right(lis, v)
        if idx == len(lis):
            lis.append(v)
            lis_i.append(i)
        else:
            lis[idx] = v
            lis_i[idx] = i
        backtrack[i] = lis_i[idx - 1] if idx > 0 else None
    
    if N - len(lis) > 3:
        write('NO')
        exit(0)
    write(f'YES\n{N - len(lis)}\n')
    
    is_used = [False] * N
    cur = lis_i[-1]
    while cur is not None:
        is_used[cur] = True
        cur = backtrack[cur]
    
    for i, u in enumerate(is_used):
        if not u:
            arr[i] = arr[i - 1] if i > 0 else 1
            write(f'{i + 1} {arr[i]}\n')


if __name__ == '__main__':
    main()