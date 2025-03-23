def main():
    import sys
    
    N, *arr = map(int, sys.stdin.read().split())
    
    dp = arr[:]
    for i in range(N):
        if i != 0 and dp[i] < dp[i-1] + arr[i]:
            dp[i] = dp[i-1] + arr[i]
    
    sys.stdout.write(str(max(dp)))


if __name__ == '__main__':
    main()