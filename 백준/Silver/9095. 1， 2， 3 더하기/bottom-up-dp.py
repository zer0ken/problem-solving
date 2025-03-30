import sys

T, *test_cases = map(int, sys.stdin.read().split())

dp = [0, 1, 2, 4]
for x in range(max(test_cases) + 1):
    dp.append(dp[-1] + dp[-2] + dp[-3])

sys.stdout.write('\n'.join(map(str, (dp[tc] for tc in test_cases))))   