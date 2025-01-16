import sys
n = int(input())
scores = list(map(int, sys.stdin.readline().split()))

m = max(scores)
sum_ = 0
for i in range(n):
    scores[i] = scores[i] / m * 100
    sum_ += scores[i]

print(sum_ / n)
