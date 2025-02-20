def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    T = int(readline())
    for t in range(1, T + 1):
        N, K = map(int, readline().split())
        stocks = list(map(int, readline().split()))

        lis = []
        for stock in stocks:
            idx = bisect_left(lis, stock)
            if idx == len(lis):
                lis.append(stock)
            else:
                lis[idx] = stock

        write(f'Case #{t}\n{int(K <= len(lis))}\n')


if __name__ == '__main__':
    main()