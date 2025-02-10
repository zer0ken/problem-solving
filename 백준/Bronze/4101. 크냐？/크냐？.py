while True:
    a, b = map(int, input().split())
    if a == b == 0:
        exit(0)
    print('Yes' if a > b else 'No')