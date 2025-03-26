X, Y = map(int, input().split())

Z = Y*100 // X
if Z >= 99:
    print('-1')
    exit(0)

lo, hi = 1, X
while lo <= hi:
    mid = (lo + hi) // 2
    if (Y + mid)*100 // (X + mid) == Z:
        lo = mid + 1
    else:
        hi = mid - 1

print(lo)