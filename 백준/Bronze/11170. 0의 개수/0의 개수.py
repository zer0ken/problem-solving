for _ in range(int(input())):
    N, M = map(int, input().split())
    zeros = 0
    for x in range(N, M + 1):
        zeros += str(x).count('0')
    print(zeros)