def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    T, F = 1, 0
    
    for _ in range(3):
        N = int(readline())
        coins = [tuple(map(int, readline().split())) for _ in range(N)]
        total = sum(p * c for p, c in coins)
        if total % 2:
            write('0\n')
            continue
        
        MAX = total // 2
        if any(p > MAX for p, _ in coins):
            write('0\n')
            continue
        
        is_possible = [F] * (MAX + 1)
        for price, count in coins:
            for p in range(MAX, 0, -1):
                if is_possible[p]:
                    for c in range(1, count + 1):
                        x = p + price * c
                        if x > MAX:
                            break
                        is_possible[x] = T
            
            for c in range(1, count + 1):
                x = price * c
                if x > MAX:
                    break
                is_possible[x] = T
            
            if is_possible[MAX]:
                break

        write('1\n' if is_possible[MAX] else '0\n')


if __name__ == '__main__':
    main()