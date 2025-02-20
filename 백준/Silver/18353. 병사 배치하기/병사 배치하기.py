def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    soldiers = list(map(int, readline().split()))
    
    lds = []
    for power in soldiers:
        idx = bisect_left(lds, -power)
        if idx == len(lds):
            lds.append(-power)
        else:
            lds[idx] = -power
    
    write(str(N - len(lds)))


if __name__ == '__main__':
    main()