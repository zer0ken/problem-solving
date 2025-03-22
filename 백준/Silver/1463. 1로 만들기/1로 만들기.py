def main():
    import sys
    
    N = int(sys.stdin.read())
    
    if N == 1:
        sys.stdout.write('0')
        exit(0)
    
    dp = set([N])
    for i in range(1, N):
        next_dp = set()
        for v in dp:
            if v % 3 == 0:
                next_dp.add(v // 3)
            if v % 2 == 0:
                next_dp.add(v // 2)
            next_dp.add(v - 1)
        dp = next_dp

        if 1 in dp:
            break
    
    sys.stdout.write(str(i))


if __name__ == '__main__':
    main()