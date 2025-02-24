def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    books = list(map(int, readline().split()))
    
    lis = []
    for num in books:
        idx = bisect_left(lis, num)
        if idx == len(lis):
            lis.append(num)
        else:
            lis[idx] = num
    
    write(str(N - len(lis)))


if __name__ == '__main__':
    main()