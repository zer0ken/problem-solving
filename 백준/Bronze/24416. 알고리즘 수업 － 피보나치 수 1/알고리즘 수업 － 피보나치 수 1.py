def main():
    n = int(input())
    dp = [0, 1, 1]
    for _ in range(3, n + 1):
        dp[0], dp[1], dp[2] = dp[1], dp[2], dp[1] + dp[2]
    
    print(dp[2], n - 2)

if __name__ == '__main__':
    main()