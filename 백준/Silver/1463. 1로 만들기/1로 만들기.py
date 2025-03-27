dp = {1: 0, 2: 1, 3: 1}
def solve(x):
    global dp
    if x in dp:
        return dp[x]
    dp[x] = 1 + min(solve(x // 3) + x % 3, solve(x // 2) + x % 2)
    return dp[x]

print(solve(int(input())))