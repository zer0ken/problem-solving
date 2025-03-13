def main():
    import sys

    write = sys.stdout.write
    lines = iter(sys.stdin.read().rstrip().splitlines())
    
    for _ in range(int(next(lines))):
        N = int(next(lines))
        kinds = list(map(int, next(lines).split()))
        M = int(next(lines))
        
        knapsack = [0] * (M + 1)
        knapsack[0] = 1
    
        for kind in kinds:
            for i in range(M + 1):
                if knapsack[i] != 0 and i + kind <= M:
                    knapsack[i + kind] += knapsack[i]
        
        write(f'{knapsack[M]}\n')


if __name__ == '__main__':
    main()
