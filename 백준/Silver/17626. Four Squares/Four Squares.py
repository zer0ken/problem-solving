import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * (n+1)
max_sqrt = int(n ** 0.5)
squares = [i*i for i in range(max_sqrt, 0, -1)]

for sq in squares:
    dp[sq] = 1
    for i in range(sq, n + 1):
        if i + sq > n:
            break
        if dp[i] == 0:
            continue
        if dp[i + sq] == 0:
            dp[i + sq] = dp[i] + 1
        else:
            dp[i + sq] = min(dp[i + sq], dp[i] + 1)
sys.stdout.write(str(dp[-1]))