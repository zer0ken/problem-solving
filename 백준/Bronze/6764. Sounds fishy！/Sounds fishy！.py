a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a < b < c < d:
    print('Fish Rising')
elif a > b > c > d:
    print('Fish Diving')
elif a == b == c == d:
    print('Fish At Constant Depth')
else:
    print('No Fish')