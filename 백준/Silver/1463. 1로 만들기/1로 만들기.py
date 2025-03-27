import sys

N = int(input())

if N == 1:
    print('0')
    exit(0)

dp = {1: 0, 2: 1, 3: 1}

def solve(x):
    if x not in dp:
        dp[x] = 1 + min(solve(x//3) + x%3, solve(x//2) + x%2)
    return dp[x]

print(solve(N))