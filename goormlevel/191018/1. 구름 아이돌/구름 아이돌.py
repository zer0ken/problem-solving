n = int(input())
scores = list(map(int, input().split()))
indices = sorted(range(n), key=lambda i: scores[i])

for i in indices[-3:][::-1]:
    print(i + 1, end=' ')
