def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    wires = [tuple(map(int, readline().split())) for _ in range(N)]
    wires.sort()
    
    lis = []
    for s, e in wires:
        if not lis or lis[-1] < e:
            lis.append(e)
            continue
        lis[bisect_left(lis, e)] = e
    
    write(str(N - len(lis)))


if __name__ == '__main__':
    main()