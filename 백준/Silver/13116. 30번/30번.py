def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    for _ in range(int(readline())):
        N, M = map(int, readline().split())
        
        while N != M:
            if N > M:
                N //= 2
            else:
                M //= 2

        write(str(10 * N) + '\n')


if __name__ == '__main__':
    main()