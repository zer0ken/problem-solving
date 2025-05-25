A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0:
    if B <= 0:
        print((B - A) * C)
    else:
        print(-A * C + D + B * E)
else:
    print((B - A) * E)