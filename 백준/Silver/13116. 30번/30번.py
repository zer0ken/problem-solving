def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    results = []
    for _ in range(int(readline())):
        N, M = map(int, readline().split())
        while N != M:
            if N > M:
                N //= 2
            else:
                M //= 2
        results.append(str(10 * N))

    write('\n'.join(results))


if __name__ == '__main__':
    main()