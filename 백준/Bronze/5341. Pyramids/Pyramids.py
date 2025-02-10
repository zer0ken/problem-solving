while True:
    n = int(input())
    if n == 0:
        exit(0)
    if n == 1:
        print(1)
    elif n % 2:
        print((n // 2) * (n + 1) + n // 2 + 1)
    else:
        print((n // 2) * (n + 1))