def main():
    import sys
    from bisect import bisect_right
    
    lines = iter(sys.stdin.read().rstrip().splitlines())
    
    N = next(lines)
    animals = list({tuple(map(int, line.split()))[1:] for line in lines})
    animals.sort(key=lambda a: a[1], reverse=True)
    animals.sort(key=lambda a: a[0])
    
    lds = []
    for l, r in animals:
        idx = bisect_right(lds, -r)
        if idx == len(lds):
            lds.append(-r)
        else:
            lds[idx] = -r
    sys.stdout.write(str(len(lds)))


if __name__ == '__main__':
    main()