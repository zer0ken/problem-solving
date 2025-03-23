def main():
    import sys
    
    N, *arr = map(int, sys.stdin.read().split())
    
    dp = [arr[0]]
    for i in range(1, N):
        dp.append(arr[i] if arr[i] > dp[i-1] + arr[i] else dp[i-1] + arr[i])
    
    sys.stdout.write(str(max(dp)))


if __name__ == '__main__':
    main()