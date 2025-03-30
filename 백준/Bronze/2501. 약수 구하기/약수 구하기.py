N, K = map(int, input().split())

front = []
back = []
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        front.append(i)
        j = N // i
        if j != i:
            back.append(j)
    if len(front) == K:
        print(front[-1])
        exit(0)

front.extend(reversed(back))
if K > len(front):
    print('0')
    exit(0)

print(front[K-1])