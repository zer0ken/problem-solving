def main():
    import sys
    from bisect import bisect_left

    N, *arr = map(int, sys.stdin.read().split())

    dp = [1] * N
    
    for i in range(1, N):
        for j in range(i):
            if arr[j] < arr[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    
    lis_len = max(dp)
    lis = []
    t = lis_len
    for i in range(N - 1, -1, -1):
        if dp[i] == t:
            lis.append(arr[i])
            t -= 1
            if t == 0:
                break
    lis.reverse()
    
    sys.stdout.write(f'{lis_len}\n{" ".join(map(str, lis))}')


if __name__ == '__main__':
    main()