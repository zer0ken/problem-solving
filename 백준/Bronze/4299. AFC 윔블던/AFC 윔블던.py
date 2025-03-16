sum, sub = map(int, input().split())
a = (sum + sub) // 2
b = sum - a

if a - b != sub or a < 0 or b < 0:
    print('-1')
else:
    print(a, b)