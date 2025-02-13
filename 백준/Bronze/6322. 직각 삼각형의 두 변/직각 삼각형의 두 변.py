case = 0
while True:
    case += 1
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        exit(0)
    if case > 1:
        print()
    print(f'Triangle #{case}')
    if a == -1:
        if b >= c:
            print('Impossible.')
        else:
            print(f'a = {(c**2 - b**2) ** 0.5:.3f}')
    elif b == -1:
        if a >= c:
            print('Impossible.')
        else:
            print(f'b = {(c**2 - a**2) ** 0.5:.3f}')
    else:
        print(f'c = {(a**2 + b**2) ** 0.5:.3f}')