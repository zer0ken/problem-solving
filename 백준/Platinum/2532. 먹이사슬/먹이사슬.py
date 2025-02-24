def main():
    import sys
    from bisect import bisect_right
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    animals = list({tuple(map(int, readline().split()))[1:] for _ in range(N)})
    animals.sort(key=lambda a: a[1], reverse=True)
    animals.sort(key=lambda a: a[0])
    
    lds = []
    for l, r in animals:
        idx = bisect_right(lds, -r)
        if idx == len(lds):
            lds.append(-r)
        else:
            lds[idx] = -r
    write(str(len(lds)))


if __name__ == '__main__':
    main()