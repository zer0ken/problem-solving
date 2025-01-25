import sys

n = int(sys.stdin.readline().rstrip())

dp = [-1] * (n + 1)

max_sqrt = int(n ** 0.5)
for i in range(max_sqrt, 0, -1):
    sq = i * i
    dp[sq] = 1
    for i in range(sq, n - sq + 1):
        if dp[i] == -1:
            continue
        if dp[i + sq] == -1:
            dp[i + sq] = dp[i] + 1
        else:
            dp[i + sq] = min(dp[i + sq], dp[i] + 1)
sys.stdout.write(str(dp[-1]))