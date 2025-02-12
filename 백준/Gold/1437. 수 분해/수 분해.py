def main():
    import sys
    from functools import cache
    
    sys.setrecursionlimit(100000)
    readline = sys.stdin.readline   
    write = sys.stdout.write
    
    N = int(readline())

    if N <= 4:
        write(str(N))
        exit(0)

    q = N % 3
    if q == 0:
        write(str(3 ** (N // 3) % 10007))
    elif q == 1:
        write(str(3 ** (N // 3 - 1) * 4 % 10007))
    else:
        write(str(3 ** (N // 3) * 2 % 10007))


if __name__ == '__main__':
    main()