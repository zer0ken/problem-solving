def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    for _ in range(int(readline())):
        N, M = map(int, readline().split())
        for _ in range(M):
            readline()
        write(str(N - 1) + '\n')


if __name__ == '__main__':
    main()