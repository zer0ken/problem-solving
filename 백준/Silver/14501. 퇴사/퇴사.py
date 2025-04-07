def main():
    import sys
    
    N, *lines = sys.stdin.read().rstrip().splitlines()
    N = int(N)
    
    dp = [0] * (N + 1)
    
    for i, line in enumerate(lines):
        T, P = map(int, line.split())
        if i + T > N:
            continue
        dp[i+T] = max(dp[i+T], max(dp[:i+1]) + P)
    
    print(max(dp))


if __name__ == '__main__':
    main()