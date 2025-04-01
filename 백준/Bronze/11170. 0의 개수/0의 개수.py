for _ in range(int(input())):
    N, M = map(int, input().split())
    print(''.join(map(str, range(N, M + 1))).count('0'))