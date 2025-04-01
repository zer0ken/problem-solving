for _ in range(int(input())):
    E, N = map(int, input().split())
    print(sum(int(input()) > E for _ in range(N)))