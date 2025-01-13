a, b, c = input().split()
if a == b == c:
    print(10000 + int(a) * 1000)
elif a == b or a == c:
    print(1000 + int(a) * 100)
elif b == c:
    print(1000 + int(b) * 100)
else:
    print(max(int(a), int(b), int(c)) * 100)