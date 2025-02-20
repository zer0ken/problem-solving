def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    while True:
        try:
            N = int(readline())
        except:
            exit(0)
        stocks = list(map(int, readline().split()))
        
        lis = []
        for stock in stocks:
            idx = bisect_left(lis, stock)
            if idx == len(lis):
                lis.append(stock)
            else:
                lis[idx] = stock
        
        write(f'{len(lis)}\n')


if __name__ == '__main__':
    main()