N = int(input())
if N == 0:
    print('1')
else:
    for num in range(1, N):
        N *= num
    print(N)