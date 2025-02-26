def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    T, F = 1, 0
    
    for _ in range(3):
        N = int(readline())
        is_possible = [F] * 50001
        total = 0
        
        for _ in range(N):
            price, count = map(int, readline().split())
            if price > 50000:
                write('0\n')
                break
            total += price * count
            for p in range(49999, 0, -1):
                if not is_possible[p]:
                    continue
                for c in range(1, count + 1):
                    x = p + c*price
                    if x > 50000:
                        break
                    is_possible[x] = T
            for c in range(1, count + 1):
                x = c * price
                if x <= 50000:
                    is_possible[x] = T
        else:
            if total % 2:
                write('0\n')
            else:
                write('1\n' if is_possible[total // 2] else '0\n')


if __name__ == '__main__':
    main()