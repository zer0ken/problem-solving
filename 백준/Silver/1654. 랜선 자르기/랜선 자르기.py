import sys

k, n = map(int, sys.stdin.readline().split())
cables = [int(sys.stdin.readline()) for _ in range(k)]
l = answer = 1
r = sum(cables) // n
while l <= r:
    mid = (l + r) // 2
    if sum([c // mid for c in cables]) >= n:
        answer = mid
        l = mid + 1
    else:
        r = mid - 1
sys.stdout.write(str(answer))