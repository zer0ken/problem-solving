def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    wires = list(map(int, readline().split()))
    
    lis = []
    for e in wires:
        idx = bisect_left(lis, e)
        if idx == len(lis):
            lis.append(e)
        else:
            lis[idx] = e
    
    write(str(N - len(lis)))


if __name__ == '__main__':
    main()