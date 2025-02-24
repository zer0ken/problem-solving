def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    T = int(readline())
    for _ in range(T):
        N = int(readline())
        ports = [int(readline()) for _ in range(N)]

        lis = []
        for port in ports:
            idx = bisect_left(lis, port)
            if idx == len(lis):
                lis.append(port)
            else:
                lis[idx] = port

        write(f'{len(lis)}\n')


if __name__ == '__main__':
    main()