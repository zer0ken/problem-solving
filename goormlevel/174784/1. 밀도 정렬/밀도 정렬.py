N = int(input())

arr = [tuple(map(int, input().split())) for _ in range(N)]

max_density = 0
max_weight = 0
max_idx = 1

for i, (w, v) in enumerate(arr, 1):
    d = w / v
    if max_density < d or (max_density == d and max_weight < w):
        max_density = d
        max_weight = w
        max_idx = i

print(max_idx)