def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, T = map(int, readline().split())

    knapsack = [0] * (T + 1)
    for _ in range(N):
        K, S = map(int, readline().split())
        if K > T:
            continue
        for t in range(T, 0, -1):
            if knapsack[t] != 0 and K + t <= T:
                knapsack[t + K] = max(knapsack[K + t], knapsack[t] + S)
        knapsack[K] = max(knapsack[K], S)
    
    write(str(max(knapsack)))


if __name__ == '__main__':
    main()