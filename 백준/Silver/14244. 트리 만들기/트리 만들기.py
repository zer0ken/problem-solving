def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    
    write(f'{0} {1}\n')
    i = 1
    if M > 2:
        delta = -1
        for i in range(2, M + 1):
            delta += 1
            write(f'0 {i}\n')
            
    for i in range(i + 1, N):
        write(f'{i - 1} {i}\n')


if __name__ == '__main__':
    main()