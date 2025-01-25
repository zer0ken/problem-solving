import sys

n = int(sys.stdin.readline().rstrip())
dp = [-1] * (n + 1)

for w in (5, 3):
    if w > n:
        continue
    dp[w] = 1 
    for i in range(3, n - w + 1):
        if dp[i] == -1:
            continue
        if dp[i + w] == -1:
            dp[i + w] = dp[i] + 1
        else:
            dp[i + w] = min(dp[i + w], i + w + 1)
sys.stdout.write(str(dp[-1]))