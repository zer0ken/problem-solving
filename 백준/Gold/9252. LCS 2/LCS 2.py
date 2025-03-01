def main():
    import sys
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    S1 = readline().rstrip()
    N1 = len(S1)
    S2 = readline().rstrip()
    N2 = len(S2)

    dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]
    
    for i in range(N1):
        for j in range(N2):
            dp[i + 1][j + 1] = dp[i][j] + 1 if S1[i] == S2[j] else max(dp[i][j + 1], dp[i + 1][j])
    
    write(f'{dp[-1][-1]}\n')
    
    i = N1
    j = N2
    lcs = []
    while i != 0 and j != 0:
        cur = dp[i][j]
        if dp[i - 1][j] == cur:
            i -= 1
        elif dp[i][j - 1] == cur:
            j -= 1
        else:
            lcs.append(S1[i - 1])
            i -= 1
            j -= 1
    
    for i in range(len(lcs) - 1, -1, -1):
        write(lcs[i])


if __name__ == '__main__':
    main()