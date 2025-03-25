def main():
    import sys
    from bisect import bisect_left

    N, *arr = map(int, sys.stdin.read().split())

    lis = []
    for v in arr:
        if not lis or lis[-1] < v:
            lis.append(v)
        else:
            lis[bisect_left(lis, v)] = v

    sys.stdout.write(str(len(lis)))


if __name__ == '__main__':
    main()