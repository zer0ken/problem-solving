N = int(input())
scores = list(map(int, input().split()))

series = []
stack = []
for score in scores:
    if stack and stack[-1] + 1 != score:
        series.append(sum(stack))
        stack.clear()
    stack.append(score)
series.append(sum(stack))

print(max(*scores, *series))
