N, D, K = map(int, input().split())
S = list(map(int, input().split()))

stars = [0] * N

clear = 0
for _ in range(D):
    if any(star + meteor > K for star, meteor in zip(stars, S)):
        clear += 1
        stars = [0] * N
    for i in range(N):
        stars[i] += S[i]
print(clear)