def main():
    import sys
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    H, N = map(int, readline().split())
    # sum of height -> maximum of the slowest speed
    knapsack = [0] * (H + 1)
    for _ in range(N):
        height, speed = map(int, readline().split())
        for h in range(H - 1, 0, -1):
            if knapsack[h] != 0 and h + height <= H:
                knapsack[h + height] = max(knapsack[h + height], min(knapsack[h], speed))
        knapsack[height] = max(knapsack[height], speed)
    
    write(str(knapsack[-1]))


if __name__ == '__main__':
    main()