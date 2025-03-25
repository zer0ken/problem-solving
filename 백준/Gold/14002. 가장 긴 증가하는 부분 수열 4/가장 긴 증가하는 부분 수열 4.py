def main():
    import sys

    N, *arr = map(int, sys.stdin.read().split())

    dp = [1] * N
    lis = [[arr[i]] for i in range(N)]
    
    for i in range(1, N):
        for j in range(i):
            if arr[j] < arr[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                lis[i] = lis[j] + [arr[i]]
    
    lis_len = max(dp)
    lis = lis[dp.index(lis_len)]    
    sys.stdout.write(f'{lis_len}\n{" ".join(map(str, lis))}')


if __name__ == '__main__':
    main()