def main():
    import sys
    
    X, Y = map(int, sys.stdin.read().split())
    
    Z = Y*100 // X
    if X == Y or Z == 99:
        sys.stdout.write('-1')
        exit(0)
    
    
    lo, hi = 1, X
    while lo <= hi:
        mid = (lo + hi) // 2
        if (Y + mid)*100 // (X + mid) == Z:
            lo = mid + 1
        else:
            hi = mid - 1
    
    sys.stdout.write(str(lo))


main()