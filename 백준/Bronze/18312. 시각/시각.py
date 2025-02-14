def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, K = readline().split()
    N = int(N)
    
    h, m, s = 0, 0, 0
    count = 0
    while h <= N:
        if K in f'{h*10000 + m*100 + s:-06}':
            count += 1
        s += 1
        if s >= 60:
            m += 1
            s = 0
            if m >= 60:
                h += 1
                m = 0

    write(str(count))


if __name__ == '__main__':
    main()