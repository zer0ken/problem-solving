def main():
    import sys
    from bisect import bisect_left

    N, *arr = map(int, sys.stdin.read().split())
    
    lis = []
    for v in arr:
        idx = bisect_left(lis, v)
        if idx == len(lis):
            lis.append(v)
        else:
            lis[idx] = v
    
    sys.stdout.write(str(len(lis)))


if __name__ == '__main__':
    main()