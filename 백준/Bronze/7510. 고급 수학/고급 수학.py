N = int(input())

for i in range(1, N + 1):
    if i > 1:
        print()
    a, b, c = sorted(map(int, input().split()))
    print(f'Scenario #{i}:')
    print('yes' if a**2 + b**2 == c**2 else 'no')