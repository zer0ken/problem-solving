N, M = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(N):
    if arr[i] % M:
        arr[i] *= M

print(' '.join(map(str, arr)))