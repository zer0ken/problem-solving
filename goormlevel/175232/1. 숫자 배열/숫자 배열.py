N = int(input())

for i in range(N):
    print(' '.join(map(str, (v for v in range(N*i + 1, N*(i+1) + 1)))))