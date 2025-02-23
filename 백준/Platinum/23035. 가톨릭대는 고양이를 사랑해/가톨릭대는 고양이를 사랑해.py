def main():
    import sys
    from bisect import bisect_right
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    C = int(readline())
    cats = []
    for _ in range(C):
        r, c = map(int, readline().split())
        if r <= N and c <= M:
            cats.append((r, c))
    cats.sort()
    
    lis = []
    for r, c in cats:
        idx = bisect_right(lis, c)
        if idx == len(lis):
            lis.append(c)
        else:
            lis[idx] = c
    write(str(len(lis)))


if __name__ == '__main__':
    main()