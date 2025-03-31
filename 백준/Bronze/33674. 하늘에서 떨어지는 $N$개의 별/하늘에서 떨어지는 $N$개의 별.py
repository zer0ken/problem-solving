N, D, K = map(int, input().split())
S = list(map(int, input().split()))

stars = [0] * N

clear = 0
for _ in range(D):
    if any(a + b > K for a, b in zip(stars, S)):
        clear += 1
        for i in range(N):
            stars[i] = 0
    for i in range(N):
        stars[i] += S[i]
print(clear)