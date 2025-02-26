def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, T = map(int, readline().split())
    contents = [tuple(map(int, readline().split())) for _ in range(N)]
    contents.sort()
    knapsack = [0] * (T + 1)
    
    for time, score in contents:
        if time > T:
            continue
        for t in range(time, -1, -1):
            if (knapsack[t] != 0 or t == 0) and t + time <= T and knapsack[t + time] < knapsack[t] + score:
                knapsack[t + time] = knapsack[t] + score
    
    write(str(max(knapsack)))


if __name__ == '__main__':
    main()