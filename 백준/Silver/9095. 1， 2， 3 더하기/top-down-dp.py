import sys

T, *test_cases = map(int, sys.stdin.read().split())

dp = {1: 1, 2: 2, 3: 4}

def dfs(x):
    if x not in dp:
        dp[x] = dfs(x-1) + dfs(x-2) + dfs(x-3)
    return dp[x]

sys.stdout.write('\n'.join(map(str, (dfs(tc) for tc in test_cases))))   