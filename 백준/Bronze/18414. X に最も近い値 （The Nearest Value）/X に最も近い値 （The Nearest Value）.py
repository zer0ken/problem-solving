X, L, R = map(int, input().split())

if X <= L:
    print(L)
elif X <= R:
    print(X)
else:
    print(R)