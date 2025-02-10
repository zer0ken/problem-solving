def main():
    import sys

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, K = map(int, readline().split())
    purchased = 0
    while (b := bin(N)).count('1') > K:
        for i in range(1, len(b) - 1):
            if b[-i] == '1':
                add = 1 << (i - 1)
                N += add
                purchased += add
                break
        
    write(str(purchased))


if __name__ == '__main__':
    main()