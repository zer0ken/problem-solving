N, W, H = map(int, input().split())
max_m = W ** 2 + H ** 2
for _ in range(N):
    m = int(input()) ** 2
    print('DA' if m <= max_m else 'NE')