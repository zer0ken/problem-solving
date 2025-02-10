def main():
    import sys

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, K = map(int, readline().split())
    purchased = 0
    while bin(N).count('1') > K:
        N += 1
        purchased += 1

    write(str(purchased))


if __name__ == '__main__':
    main()