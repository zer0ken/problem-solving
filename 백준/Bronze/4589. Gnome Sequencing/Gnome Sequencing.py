print('Gnomes:')
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if c <= b <= a or a <= b <= c:
        print('Ordered')
    else:
        print('Unordered')