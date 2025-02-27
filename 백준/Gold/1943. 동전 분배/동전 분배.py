def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    T, F = 1, 0
    
    def solve():
        N = int(readline())
        coins = [tuple(map(int, readline().split())) for _ in range(N)]
        total = sum(p * c for p, c in coins)
        
        if total % 2:
            write('0\n')
            return
        
        MAX = total // 2
        combinations = {0}

        coins.sort(key=lambda c: c[1], reverse=True)

        for price, count in coins:
            if price > MAX:
                write('0\n')
                return
            
            new_combinations = set()
            for comb in combinations:
                for c in range(1, count + 1):
                    x = comb + price * c
                    if x == MAX:
                        write('1\n')
                        return
                    if x > MAX or x in combinations:
                        break
                    new_combinations.add(x)
            combinations |= new_combinations
        
        write('0\n')
    
    for _ in range(3):
        solve()


if __name__ == '__main__':
    main()