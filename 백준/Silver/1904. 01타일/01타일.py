def main():
    import sys
    
    N = int(sys.stdin.read())
    
    dp = [0, 1]
    for _ in range(N - 1):
        dp[0], dp[1] = dp[1], sum(dp) % 15746
    
    sys.stdout.write(str(sum(dp) % 15746))


if __name__ == '__main__':
    main()